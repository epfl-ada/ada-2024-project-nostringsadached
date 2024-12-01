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
