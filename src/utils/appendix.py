import pandas as pd
import ast
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.formula.api import ols
import pingouin as pg
from sklearn.metrics import r2_score
from sklearn.preprocessing import MultiLabelBinarizer

def extract_names(cell):
    #Transform the string of dictionaries into a list of real dictionaries with the id referring to the key and the name referring to the value
    #Then only extract the names from the dictionaries
    try:
        data_dict = ast.literal_eval(cell)
        return ", ".join(data_dict.values())
    except (ValueError, SyntaxError):
        return cell
    
def extract_year(date_str):
    if isinstance(date_str, str) and len(date_str) == 4 and date_str.isdigit():
        return int(date_str)
    else:
        #for other formats 
        try:
            return pd.to_datetime(date_str, errors='coerce').year
        except Exception:
            return None
    
def outliers_bounds(data, low_factor, up_factor):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - low_factor * IQR
    upper_bound = Q3 + up_factor * IQR
    return lower_bound, upper_bound

def replace_in_columns(data, column, old, new):
    data[column] = data[column].replace(old, new)
    return data

def filter_genres(genre_list, unwanted_genres):
    if isinstance(genre_list, str):
        genres = genre_list.split(', ')
        filtered_genres = [genre for genre in genres if genre not in unwanted_genres]
        return ', '.join(filtered_genres)
    return genre_list

def keep_only_the_most_common_genres(genre_list, genre_counts):
    if isinstance(genre_list, str):
        genres = genre_list.split(', ')
        filtered_genres = [genre for genre in genres if genre in genre_counts['Genres'].values]
        return ', '.join(filtered_genres)
    return genre_list

def most_common_genres(movies, genre_counts, top_n):
    movies_common_genre = movies.copy()

    #keep only the n top genres and replace the empty line by nan values
    movies_common_genre['Genres'] = movies_common_genre['Genres'].apply(lambda x: keep_only_the_most_common_genres(x, genre_counts=genre_counts))
    movies_common_genre['Genres'] = movies_common_genre['Genres'].apply(lambda x: np.nan if x == '' else x)
    
    #compute the portion of film qualified by the top n genre
    total = len(movies)
    covered = total - movies_common_genre['Genres'].isna().sum()
    coverage = (covered / total) * 100
    
    return movies_common_genre, coverage

def calculate_genre_coverages(movies, genre_counts, top_n_values=[100, 30, 10, 3]):
    genre_counts_list = [genre_counts.iloc[:n] for n in top_n_values]
    coverages = {}
    for top_n, genre_counts_subset in zip(top_n_values, genre_counts_list):
        _, coverage = most_common_genres(movies, genre_counts_subset, top_n)
        coverages[top_n] = coverage
    
    for top_n, coverage in coverages.items():
        print(f"Number of films covered by the {top_n} major genres: {coverage:.2f}%")


def anova_pairwise_turkey(data):
    anova_table = sm.stats.anova_lm(ols('Proportion ~ Group', data=data).fit(), typ=2)
    print(anova_table)

    # Check ANOVA significance and perform Tukey post-hoc test
    if anova_table['PR(>F)'].iloc[0] < 0.05:
        print("There is a significant difference between at least one pair of groups.")
        print(pg.pairwise_tukey(data=data, dv='Proportion', between='Group'))
    else:
        print("There is no significant difference between the proportions of war movies.")

def evaluate_models(war_movies, models):
    model_list = []
    predicted_proportions_list = []
    summary_list = []
    
    for i, (predictors, description) in enumerate(models, start=1):
        X = war_movies[predictors]  # Select predictor variables
        y = war_movies['Proportion'].values  # Select target variable

        # Fit model and get predictions + summary
        model, predicted_proportions, summary = fit_and_evaluate_model(X, y)

        # Store results
        model_list.append(model)
        predicted_proportions_list.append(predicted_proportions)
        summary_list.append(summary)

        # Calculate and print R-squared
        r2 = r2_score(y, predicted_proportions)
        print(f"R-squared for model {i} with {description}: {r2:.4f}")
    
    return model_list, predicted_proportions_list, summary_list


def fit_and_evaluate_model(X, y):
    """
    Fits a linear regression model, predicts values, handles NaN values, 
    and prints a statistical summary using statsmodels.
    """
    mask = ~np.isnan(y)
    X = X[mask]
    y = y[mask]
    
    model = LinearRegression()
    model.fit(X, y)
    
    predicted = model.predict(X)
    
    X_sm = sm.add_constant(X) 
    model_sm = sm.OLS(y, X_sm).fit()

    return model, predicted, model_sm.summary()


# Function to filter movies by genre and country
def filter_genre_country(df, genre_pattern, country="United States of America"):
    return df[df['Countries'].str.contains(country) & df['Genres'].str.contains(genre_pattern, case=False, na=False)]

# Function to group data by decade
def group_by_decade(df):
    df = df.copy()
    df['Decade'] = (df['Year'] // 10) * 10
    return df.groupby('Decade').size()

def get_country_events(historical_data, country):
    return historical_data[(historical_data['Location'] == country) | (historical_data['Location'] == "Global")]

# Function to filter movie genres based on a predefined list
def genre_filter(genre_string, genres_list):
    if pd.isna(genre_string):
        return []
    return [g for g in genres_list if g in genre_string]

# Function to determine if a movie year is before or after an event
def get_event_period(year, event_row):
    event_year = event_row['Year']
    if event_year - 5 <= year < event_year:  # 5 years before the event until the event year
        return 'Before'
    elif event_year + 1 <= year:  # From 1 year after the event to 6 years after
        return 'After'
    return 'No Event'  # Exclude other years

# Function to process movies for a specific event
def process_event(event_row,movies):
    temp_df = movies.copy()
    temp_df['Period'] = temp_df['Year'].apply(lambda y: get_event_period(y, event_row))
    temp_df = temp_df[temp_df['Period'].isin(['Before', 'After'])]
    result = temp_df.groupby(['Period', 'Filtered_Genres']).size().reset_index(name='Count')
    result['Proportion'] = result.groupby('Period')['Count'].transform(lambda x: x / x.sum())
    return result