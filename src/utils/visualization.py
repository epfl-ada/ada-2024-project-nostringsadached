import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from src.utils.appendix import *
import matplotlib.patches as mpatches

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