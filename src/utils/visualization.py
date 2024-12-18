import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from src.utils.appendix import *
import matplotlib.patches as mpatches
import pandas as pd

def plot_boxplot(data, title, xlabel, figsize=(8, 1), color='lightblue', orient='h'):
    """
    Plots a boxplot for the given data.

    Parameters:
        data (array-like): The data to plot.
        title (str): The title of the plot.
        xlabel (str): The label for the x-axis.
        figsize (tuple): Figure size (default: (8, 1)).
        color (str): Color of the boxplot (default: 'lightblue').
        orient (str): Orientation of the boxplot (default: 'h' for horizontal).
    """
    plt.figure(figsize=figsize)
    sns.boxplot(data, color=color, orient=orient)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

def plot_bar(x, y, xlabel, ylabel, title, color='red'):
    plt.figure(figsize=(8, 4))
    plt.bar(x, y, color=color, alpha=0.6)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
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
    plt.plot(genre_films_proportion.index, genre_films_proportion.values, color='navy')
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
    plt.plot(genre_films_per_year.index, genre_films_per_year.values, color='navy')
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