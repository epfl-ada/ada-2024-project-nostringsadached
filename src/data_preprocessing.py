#Pour le nettoyage des données.
import pandas as pd

movies_data = pd.read_csv("data/MovieSummaries/movie.metadata.tsv", delimiter='\t') # Columns are separated by tabs rather than commas
history_data = pd.read_csv("data/HistoricalDataset/historical.dataset.csv")



def clean_movie_data(data):
    # Exemple de nettoyage : supprimer les valeurs manquantes
    # Transformer les formats de dates pour l’analyse temporelle
    return data.dropna()

def clean_plot_data(data):
    # Supprimer valeurs manquantes
    return data.dropna()

def vectorize_plot_data(data):
    # Convertir les descriptions en une forme vectorielle, qui convient aux tâches d'analyse de texte.
    return data.dropna()

def clean_historical_data(data_movie, data_history):
    # Traiter les valeurs manquantes
    # Drop les colonnes qui ne nous intéressent pas 
    
    # the historical dataset starts from very ancient times, we want to only keep events happening after the first movie was released
    # for this purpose, we need to make the date values more convenient to work with
    cleaned_data_history = remove_BC(data_history)
    cleaned_data_history['Year'] = cleaned_data_history['Year'].astype(int) # converts the column ['Year'] from str to int
    
    # get the year of the first released movie
    movies_dt = pd.to_datetime(data_movie.iloc[:, 3], errors='coerce') # converts the 'Release date' column to datetime
    first_movie_year = movies_dt.dt.year.min()
    print('\n In our dataset, the first movie that was released was in', int(first_movie_year))
    
    # remove historical events that happened before the first movie was released
    cleaned_data_history = cleaned_data_history[cleaned_data_history['Year'] >= first_movie_year]
    
    # drop columns that we don't need
    cleaned_data_history.drop(columns=["Place Name","Date", "Month"], inplace=True)
    
    return cleaned_data_history.dropna()


def vectorize_historical_data(data):
    # tokenizer les evenements qui nous interesse pour pouvoir les faire correspondre avec ceux de movie_data
    return data.dropna()

def remove_BC(data):
    # we can safely remove all columns with BC dates, knowing that movies didn't exist at that time
    clean_data = data[~data['Year'].str.contains('BC')]
    return clean_data


