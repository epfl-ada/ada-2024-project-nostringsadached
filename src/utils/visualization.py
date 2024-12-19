import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from src.utils.appendix import *
import matplotlib.patches as mpatches
import pandas as pd
from scipy.stats import chisquare
from sklearn.neighbors import KernelDensity
from scipy.stats import norm

def plot_war_movies(war_movies, all_movies):
    plt.figure(figsize=(8,4))
    war_movies["Year"].hist(bins=50, range=(all_movies["Year"].min(), all_movies["Year"].max()), color = 'salmon', edgecolor = 'black')
    plt.xlabel("Year")
    plt.ylabel("Number of war movies")
    plt.title("Number of war movies per year")
    plt.show()

def analyze_war_movies(region_name, countries, war_comedy_df, war_drama_df, total_movies_per_year):
    region_pattern = '|'.join(countries)
    
    comedy_filtered = war_comedy_df[war_comedy_df['Countries'].str.contains(region_pattern, case=False, na=False)]
    drama_filtered = war_drama_df[war_drama_df['Countries'].str.contains(region_pattern, case=False, na=False)]
    
    comedy_per_year = comedy_filtered.groupby('Year').size()
    drama_per_year = drama_filtered.groupby('Year').size()
    comedy_proportion = (comedy_per_year / total_movies_per_year) * 100
    drama_proportion = (drama_per_year / total_movies_per_year) * 100
    
    plt.figure(figsize=(8, 4))
    plt.bar(comedy_proportion.index, comedy_proportion.values, label=f'{region_name} War Comedy Movies Proportion %', color='red', alpha=0.6)
    plt.bar(drama_proportion.index, drama_proportion.values, label=f'{region_name} War Drama Movies Proportion %', color='limegreen', alpha=0.6)
    plt.xlabel('Year')
    plt.ylabel('Proportion of Movies %')
    plt.title(f'War Comedy Movies and War Drama Movies in {region_name} Over Time')
    plt.legend(loc='upper right')
    plt.show()
    

def plot_bar(x, y, ylabel, title, xlabel='Year', label=None, color='red', orientation='vertical'):
    plt.figure(figsize=(8, 4))
    if orientation == 'vertical':
        plt.bar(x, y, color=color, label=label, alpha=0.6)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    elif orientation == 'horizontal':
        plt.barh(x, y, color=color, label=label, alpha=0.6)
        plt.xlabel(ylabel)
        plt.ylabel(xlabel)
    plt.title(title)
    if label:
        plt.legend(loc='upper right')
    plt.show()

def plot_bar_and_event(events, movies_proportion, title, color='lightgreen'): 
    plt.figure(figsize=(8, 4))
    for year in events['Year']:
        plt.axvline(x=year,color='red',linestyle='--',alpha=0.6)
        event_name = events[events['Year'] == year]['Name of Incident']
        plt.text(year, 0, event_name .values[0], rotation=-40, verticalalignment='top')  
        
    plt.bar(movies_proportion.index, movies_proportion.values, color= color)
    plt.xlabel('Year')
    plt.ylabel('Proportion of Movies %')
    plt.title(title)
    plt.show()

def plot_lgbt_movie_trend(df, pred):
    plt.figure(figsize=(8,4))
    plt.scatter(df['Year'], df['Counts'], label='Data', alpha=0.6, color='purple')

    # Plot the trend line
    plt.plot(df['Year'], pred, color='red', linewidth=2, label='Trend Line')

    plt.xlabel('Year')
    plt.ylabel('Counts of Movies')
    plt.title('LGBT Movie Counts Over Time')
    plt.legend()
    plt.show()
    
def plot_events_map(dataset):
    shapefile_path = 'data/geopandas/ne_110m_admin_0_countries.shp'
    world = gpd.read_file(shapefile_path)
    world = world.rename(columns={'NAME': 'Country'})  #adjust if necessary depending on the shapefile 

    #aggregate the number of events per country
    event_counts = dataset['Country'].value_counts()
    event_counts = event_counts.reset_index()  #convert to DataFrame for easier merging
    event_counts.columns = ['Country', 'Event_Count'] 

    # merge the event counts with the world map by using 'Country' as the key for both DataFrames
    merged = world.merge(event_counts, on='Country', how='left')

    # plot the map
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))

    # plot country boundaries
    world.boundary.plot(ax=ax, linewidth=1)
    merged.plot(column='Event_Count', ax=ax, legend=True,
            legend_kwds={'label': "Number of Events by Country",
                         'orientation': "horizontal"},
            cmap='Oranges')
    plt.title("Number of Events per Country")
    plt.show()
    
def plot_movies_map(dataset, movies_per_country):
       #Load a geopandas dataframe with the world map
    shapefile_path = 'data/geopandas/ne_110m_admin_0_countries.shp'
    world_for_movie = gpd.read_file(shapefile_path)
    world_for_movie = world_for_movie.rename(columns={'NAME': 'Countries'})

    #Merged the geopandas dataframe with the movie count dataframe to display the number of movies per country on the world map                                        
    merged = world_for_movie.merge(movies_per_country, on='Countries', how='left')
    fig, ax = plt.subplots(1, 1, figsize=(11, 5))

    fig.tight_layout()
    world_for_movie.boundary.plot(ax=ax, linewidth=1)

    legend_kwds={'label': "Number of Movies per Country", 'orientation': "vertical"}

    merged.plot(column='Movie_Count', ax=ax, legend=True, legend_kwds=legend_kwds, cmap='OrRd', edgecolor='black')

    plt.title("Number of Movies per Country")
    plt.show()

def plot_movie_genres_per_decade(related_genres,total_movies_per_decade,preprocessed_movies):
    plt.figure(figsize=(12, 4))
    for genre, related in related_genres.items():
        related_data = filter_genre_country(preprocessed_movies, '|'.join(related))
        related_data_per_decade = group_by_decade(related_data)
        # Align the indices of related_data_per_decade and total_movies_per_decade
        aligned_data = related_data_per_decade.reindex(total_movies_per_decade.index, fill_value=0)
        proportion_per_decade = (aligned_data / total_movies_per_decade) * 100
        plt.plot(aligned_data.index, proportion_per_decade.values, label=genre)

    plt.xlabel('Decade')
    plt.ylabel('Proportion of Movies (%)')
    plt.title('Proportion of Movies by Genre Over Decades')
    plt.legend()
    plt.show()
    
def plot_genre_trends_per_country(country,historical_data,movie_metadata):
    plt.figure(figsize=(14, 8))
    country_data = movie_metadata[(movie_metadata['Countries'] == country)]
    country_genres = country_data.explode('Genres').groupby(['Year', 'Genres']).size().reset_index(name='Count')

    # Filter top 5 genres by total count for this country
    top_genres = country_genres.groupby('Genres')['Count'].sum().nlargest(5).index
    filtered_data = country_genres[country_genres['Genres'].isin(top_genres)]

    genre_handles = []
    for genre in top_genres:
        genre_data = filtered_data[filtered_data['Genres'] == genre]
        line, = plt.plot(genre_data['Year'], genre_data['Count'], label=genre)
        genre_handles.append(line)

    country_events = get_country_events(historical_data, country)
    event_colors = plt.cm.tab20.colors 
    event_handles = []

    for idx, (_, event) in enumerate(country_events.iterrows()):
        color = event_colors[idx % len(event_colors)]
        plt.plot([event['Year'], event['Year']], [0, plt.gca().get_ylim()[1] * 0.75], color=color, linestyle='--', linewidth=1.5, alpha=0.7)
        plt.scatter(event['Year'], plt.gca().get_ylim()[1] * 0.75, color=color, marker='*', s=100, zorder=5)
        event_handles.append(mpatches.Patch(color=color, label=event['Event Name']))
        
    plt.title(f"Top Genre Trends Over Time in {country}", fontsize=16)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Number of Movies", fontsize=14)
    plt.legend(handles=genre_handles + event_handles, title="Legend", fontsize=8, loc='upper right', bbox_to_anchor=(1.2, 1))
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    
def plot_genre_proportion_and_event(df, total_movies, genre_pattern, genre_name, event_name, event_dates, country=None, start=None, is_period=None):
    """
    Plots the proportion of films of a specific genre over time, with the option to highlight a significant event.

    Parameters:
        genre_pattern (str): A regex pattern to match the genre of films.
        genre_name (str): The name of the genre for the plot title.
        event_name (str): The name of the event to highlight on the plot.
        event_dates (tuple): A tuple containing the start and end year of the event (e.g., (start_year, end_year)).
        country (str, optional): Country name to filter the films. If None, includes all countries.
        start (int, optional): The year to start the plot from. If None, starts from the earliest year.
        is_period (bool): If True, highlights the event as a period; if False, highlights it as a single point.
    """
    genre_films = df[df['Genres'].str.contains(genre_pattern, case=False, na=False)]
    
    if country:
        genre_films = genre_films[genre_films['Countries'].str.contains(country, case=False, na=False)]
    
    genre_films_per_year = genre_films.groupby('Year').size()
    genre_films_proportion = (genre_films_per_year / total_movies).fillna(0) * 100

    # Filter the data to start from the specified year
    if start:
        genre_films_proportion = genre_films_proportion[genre_films_proportion.index >= start]

    plt.figure(figsize=(8, 4))
    title = f'Proportion of {genre_name} Films Over Time'
    if country:
        title += f' in {country}'
    plt.bar(genre_films_proportion.index, genre_films_proportion.values, color='royalblue')
    plt.xlabel('Year')
    plt.ylabel(f'Proportion of {genre_name} Movies (%)')
    plt.title(title)

    if is_period:
        plt.axvspan(event_dates[0], event_dates[1], color='lightblue', alpha=0.3, label=event_name)
    else:
        plt.axvline(x=event_dates[0], color='red', linestyle='--', label=event_name)

    plt.legend()
    plt.show()
    

def plot_genre_number_and_event(df, genre_pattern, genre_name, event_name, event_dates, country=None, start=None, is_period=None):
    """
    Plots the number of films of a specific genre over time, with the option to highlight a significant event.

    Parameters:
        genre_pattern (str): A regex pattern to match the genre of films.
        genre_name (str): The name of the genre for the plot title.
        event_name (str): The name of the event to highlight on the plot.
        event_dates (tuple): A tuple containing the start and end year of the event (e.g., (start_year, end_year)).
        country (str, optional): Country name to filter the films. If None, includes all countries.
        is_period (bool): If True, highlights the event as a period; if False, highlights it as a single point.
    """
    genre_films = df[df['Genres'].str.contains(genre_pattern, case=False, na=False)]
    
    if country:
        genre_films = genre_films[genre_films['Countries'].str.contains(country, case=False, na=False)]
    
    genre_films_per_year = genre_films.groupby('Year').size().fillna(0)
    # Filter the data to start from the specified year
    if start:
        genre_films_proportion = genre_films_proportion[genre_films_proportion.index >= start]
        
    plt.figure(figsize=(8, 4))
    title = f'Number of {genre_name} Films Over Time'
    if country:
        title += f' in {country}'
    plt.bar(genre_films_per_year.index, genre_films_per_year.values, color='royalblue')
    plt.xlabel('Year')
    plt.ylabel(f'Number of {genre_name} Movies (%)')
    plt.title(title)

    if is_period:
        plt.axvspan(event_dates[0], event_dates[1], color='lightblue', alpha=0.3, label=event_name)
    else:
        plt.axvline(x=event_dates[0], color='red', linestyle='--', label=event_name)

    plt.legend()
    plt.show()

def plot_global_plot(historical,movies):
    sns.set_palette("pastel")

    combined_data = []
    for _, event in historical.iterrows():
        event_data = process_event(event, movies)
        event_data['Event'] = event['Event Name']
        combined_data.append(event_data)

    # Concaténer toutes les données pour un seul plot
    final_data = pd.concat(combined_data)
    final_data['Separation'] = final_data['Event'] + '_' + final_data['Period']

    # Ajouter des séparations
    event_order = []
    for event in historical['Event Name']:
        event_order.append(f"{event}_Before")
        event_order.append(f"{event}_After")
        event_order.append(" ")

    final_data = final_data.sort_values(by=['Event', 'Period'], key=lambda x: x.map({'Before': 0, 'After': 1}))
    pivot_data = final_data.pivot_table(index=['Separation'], columns='Filtered_Genres', values='Proportion', fill_value=0)

    # Ajouter des lignes vides pour les séparations
    for sep in [i for i in pivot_data.index if "Separation" in i]:
        pivot_data.loc[sep] = 0

    pivot_data = pivot_data.reindex(event_order)

    pivot_data.plot(kind='bar', stacked=True, figsize=(18, 8))
    plt.title("Proportion of Movie Genres Before and After Events")
    plt.xlabel("Events and Periods")
    plt.ylabel("Proportion")
    plt.legend(title="Genres", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def plot_actual_vs_predicted(years, actual, predicted, model, title="Trend of War Movies"):
    """
    Plots the actual vs predicted proportions of war movies over time and prints model coefficients.

    Parameters:
        years (array-like): The years for the x-axis.
        actual (array-like): Actual proportion values.
        predicted (array-like): Predicted proportion values.
        model (fitted model object): A regression model object with intercept_ and coef_ attributes.
        title (str): The title of the plot.
    """
    # Plot actual vs predicted
    plt.figure(figsize=(8, 4))
    plt.plot(years, actual, label='Actual Proportion', color='blue')
    plt.plot(years, predicted, label='Predicted Proportion', color='red', linestyle='--')
    
    # Add labels, title, and legend
    plt.xlabel('Year')
    plt.ylabel('Proportion of War Movies (%)')
    plt.title(title)
    plt.legend()
    plt.show()

def plot_selected_events(historical, movies, selected_events):
    sns.set_palette("pastel")

    combined_data = []
    for _, event in historical.iterrows():
        if event['Event Name'] in selected_events:
            event_data = process_event(event, movies)
            event_data['Event'] = event['Event Name']
            combined_data.append(event_data)

    final_data = pd.concat(combined_data)
    final_data['Separation'] = final_data['Event'] + '_' + final_data['Period']

    final_data = final_data.sort_values(by=['Event', 'Period'], key=lambda x: x.map({'Before': 0, 'After': 1}))
    pivot_data = final_data.pivot_table(index=['Separation'], columns='Filtered_Genres', values='Proportion', fill_value=0)

    event_order = []
    for event in selected_events:
        event_order.append(f"{event}_Before")
        event_order.append(f"{event}_After")
        pivot_data.loc[f"{event}_Separation"] = 0  # Ajout de lignes vides
        event_order.append(f" ")

    pivot_data = pivot_data.reindex(event_order)

    pivot_data.plot(kind='bar', stacked=True, figsize=(15, 8))
    plt.title("Proportion of Movie Genres Before and After Selected Events")
    plt.xlabel("Events and Periods")
    plt.ylabel("Proportion")
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Genres", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
    
    
def plot_first_look_historical(historical_events_df):
    colors_location = ['#FFB5E8', '#85E3FF', '#B9FBC0', '#FFABAB', '#FFC3A0']
    colors_impact = ['#FFB5E8', '#B28DFF', '#FFABAB']

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # By Location
    location_counts = historical_events_df['Location'].value_counts()
    axes[0].bar(location_counts.index, location_counts.values, color=colors_location[:len(location_counts)])
    axes[0].set_title("Distribution of events by Location")
    axes[0].tick_params(axis='x', rotation=45)

    # By Impact Type
    impact_counts = historical_events_df['Impact Type'].value_counts()
    axes[1].bar(impact_counts.index, impact_counts.values, color=colors_impact[:len(impact_counts)])
    axes[1].set_title("Events by Impact Type")

    # By Year
    sns.histplot(data=historical_events_df, x='Year', bins=20, kde=True, color="lightblue", ax=axes[2])
    axes[2].set_title("Distribution of historical events by Year")
    axes[2].set_xlabel("Year")
    axes[2].set_ylabel("Number of events")

    plt.tight_layout()
    plt.show()
    
    
def plot_type_event(df, event_type, outcome, country):
    events = df[df['Type of Event'].str.contains(event_type, case=False, na=False)]
    
    if country:
        events = events[events['Country'].str.contains(country, case=False, na=False)]
    
    if outcome:
        events = events[events['Outcome'].str.contains(outcome, case=False, na=False)] 
    
    events_counts=events.groupby('Year').size()
    
    title_evt=event_type
    if outcome: title_evt=f'{outcome} {event_type}'
    title = f'Number of {title_evt} Events Over Time'
    if country:
        title += f' in {country}'
    # Plot the number of events over time
    plt.figure(figsize=(12, 6))
    plt.plot(events_counts.index, events_counts.values, marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Number of Events')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()


def ztest(df,year, genre):
    pre_event=df[df['Year']<year]
    post_event=df[df['Year']>year]
    
    pre_total = pre_event.shape[0]
    pre_movies = pre_event[pre_event['Genres'].str.contains(genre, case=False, na=False)].shape[0]

    post_total = post_event.shape[0]
    post_movies = post_event[post_event['Genres'].str.contains(genre, case=False, na=False)].shape[0]

    # Proportions
    p1 = pre_movies / pre_total
    p2 = post_movies / post_total
    
    # Pooled proportion
    p = (pre_movies + post_movies) / (pre_total + post_total)
    
    # Standard error
    se = np.sqrt(p * (1 - p) * (1 / pre_total + 1 / post_total))

    # Z-statistic
    z = (p2 - p1) / se

    # P-value
    p_value = 1 - norm.cdf(z)
    
    # Output results
    print(f"Proportion of {genre} Movies before {year}:", p1)
    print(f"Proportion of {genre} Movies after {year}:", p2)
    print("Z-statistic:", z)
    print("P-value:", p_value)

    # Interpretation
    alpha = 0.05
    if p_value < alpha:
        print(f"Reject the null hypothesis: There is a significant increase in the proportion of {genre} movies.")
    else:
        print(f"Fail to reject the null hypothesis: No significant increase in the proportion of {genre} movies.")


def reg_model(df,year, genre, event_name, model):
    genre_movies = df[df['Genres'].str.contains(genre, case=False, na=False)]
    total_movies_per_year = df.groupby('Year').size()
    genre_movies_per_year = genre_movies.groupby('Year').size()
    
    # Calculate proportion of political movies per year
    proportion_genre = (genre_movies_per_year / total_movies_per_year).fillna(0)
    
    # Create a DataFrame for regression
    data = pd.DataFrame({
        'Year': proportion_genre.index,
        'Proportion': proportion_genre.values })
    
    data['Time'] = data['Year'] - data['Year'].min()  # Time variable for trend
    data['Post_Event'] = (data['Year'] >= year).astype(int)  # Indicator for post-event
    data['Time_After'] = data['Time'] * data['Post_Event']  # Interaction term
    
    if model=='linear_reg':
        # Fit the regression model
        X = sm.add_constant(data[['Time', 'Post_Event', 'Time_After']])
        model = sm.OLS(data['Proportion'], X).fit()
        
    elif model=='poly_reg':
        # Add polynomial terms (e.g., quadratic, cubic)
        data['Time_Squared'] = data['Time'] ** 2
        data['Time_Cubed'] = data['Time'] ** 3

        # Fit the regression model with polynomial terms
        X = sm.add_constant(data[['Time', 'Time_Squared', 'Time_Cubed', 'Post_Event', 'Time_After']])
        model = sm.OLS(data['Proportion'], X).fit()
    
    # Output regression results
    print(model.summary())

    # Plot the results
    plt.figure()
    plt.scatter(data['Year'], data['Proportion'], label='Observed Proportion', color='royalblue')
    plt.plot(data['Year'], model.predict(X), label='Fitted Trend', color='darkviolet')
    plt.axvline(1972, color='red', linestyle='--', label=f'{event_name} ({year})')
    plt.title(f'Interrupted Time Series: Impact of {event_name} on {genre} Movies')
    plt.xlabel('Year')
    plt.ylabel(f'Proportion of {genre} Movies')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
    
    

def kde_model(df, start_year, end_year, genre, event_year, event_name):
    """
    Fit a Kernel Density Estimation (KDE) model to analyze the impact of an event on a movie genre.

    Parameters:
        df (DataFrame): The dataset containing movie information.
        start_year (int): The starting year for the analysis.
        end_year (int): The ending year for the analysis.
        genre (str): The movie genre to analyze (e.g., 'spy').
        event_year (int): The year of the event being analyzed.
        event_name (str): A descriptive name of the event.

    Returns:
        None: Displays the Chi-Square test results and a plot of the observed and fitted KDE curve.
    """
    # Step 1: Filter data for the selected genre and years
    genre_movies = df[df['Genres'].str.contains(genre, case=False, na=False)]
    genre_movies_counts = genre_movies.groupby('Year').size()
    relevant_years = genre_movies_counts[(genre_movies_counts.index >= start_year) & 
                                         (genre_movies_counts.index <= end_year)]

    # Step 2: Prepare KDE for fitting the observed counts
    years = relevant_years.index.values.reshape(-1, 1)  # Reshape for KDE
    counts = relevant_years.values

    # Fit KDE model
    kde = KernelDensity(kernel='gaussian', bandwidth=0.6).fit(years, sample_weight=counts)
    x = np.linspace(start_year, end_year, 500).reshape(-1, 1)  # Smooth range of years
    fitted_values = np.exp(kde.score_samples(x))  # Get KDE values

    # Scale KDE to match observed peak
    fitted_values = fitted_values * (counts.max() / fitted_values.max())

    # Step 3: Perform Chi-Square Goodness-of-Fit Test
    observed_counts = counts  # Observed counts
    fitted_counts = np.interp(years.flatten(), x.flatten(), fitted_values)  # Interpolate KDE values
    fitted_counts = fitted_counts / fitted_counts.sum() * observed_counts.sum()  # Normalize

    chi2_stat, p_value = chisquare(f_obs=observed_counts, f_exp=fitted_counts)

    # Step 4: Print results
    print(f"Chi-Square Statistic: {chi2_stat:.2f}")
    print(f"P-Value: {p_value:.2e}")

    # Step 5: Plot observed counts and fitted KDE curve
    plt.figure()
    plt.bar(relevant_years.index, observed_counts, label='Observed Counts', color='royalblue', alpha=0.6)
    plt.plot(x, fitted_values, label='Fitted KDE Curve', color='darkviolet', linewidth=2)
    plt.axvline(event_year, color='red', linestyle='--', label=f'{event_name} ({event_year})')
    plt.title(f'Impact of {event_name} on {genre.capitalize()} Movies')
    plt.xlabel('Year')
    plt.ylabel(f'Number of {genre.capitalize()} Movies')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

