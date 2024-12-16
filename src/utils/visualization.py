import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

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

def plot_bar(x,y, xlabel, ylabel, title, color='red'):
    plt.figure(figsize=(8, 4))
    plt.bar(x, y, color=color, alpha=0.6)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(loc='upper right')
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
    plt.bar(comedy_proportion.index, comedy_proportion.values, label=f'{region_name} War Comedy Movies Proportion', color='red', alpha=0.6)
    plt.bar(drama_proportion.index, drama_proportion.values, label=f'{region_name} War Drama Movies Proportion', color='limegreen', alpha=0.6)
    plt.xlabel('Year')
    plt.ylabel('Proportion of Movies')
    plt.title(f'War Comedy Movies and War Drama Movies in {region_name} Over Time')
    plt.legend(loc='upper right')
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