import pandas as pd
import ast
import numpy as np

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
    if year < event_row['Year']:
        return 'Before'
    elif year >= event_row['Year']:
        return 'After'
    return 'No Event'

# Function to process movies for a specific event
def process_event(event_row,movies):
    temp_df = movies.copy()
    temp_df['Period'] = temp_df['Year'].apply(lambda y: get_event_period(y, event_row))
    temp_df = temp_df[temp_df['Period'].isin(['Before', 'After'])]
    result = temp_df.groupby(['Period', 'Filtered_Genres']).size().reset_index(name='Count')
    result['Proportion'] = result.groupby('Period')['Count'].transform(lambda x: x / x.sum())
    return result

