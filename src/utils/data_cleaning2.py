from src.utils.appendix import *

def preprocessed_movies(raw_movies_data):
    raw_movies_data.columns = ["Wikipedia movie ID", "Freebase movie ID", "Movie name", "Movie release date", "Movie box office revenue",
    "Movie runtime", "Movie languages (Freebase ID:name tuples)", "Movie countries (Freebase ID:name tuples)", "Movie genres (Freebase ID:name tuples)"]
    
    #Remove the ID, keep only the name
    raw_movies_data["Languages"] = raw_movies_data["Movie languages (Freebase ID:name tuples)"].apply(extract_names)
    raw_movies_data["Countries"] = raw_movies_data["Movie countries (Freebase ID:name tuples)"].apply(extract_names)
    raw_movies_data["Genres"] = raw_movies_data["Movie genres (Freebase ID:name tuples)"].apply(extract_names)
    raw_movies_data.drop(columns=["Movie languages (Freebase ID:name tuples)", "Movie countries (Freebase ID:name tuples)", "Movie genres (Freebase ID:name tuples)", "Freebase movie ID","Wikipedia movie ID"], inplace=True)
    
    #Remove the word \"Language\" from the Languages column.
    raw_movies_data["Languages"] = raw_movies_data["Languages"].str.replace('Language', '', regex=True)
    raw_movies_data['Year'] = raw_movies_data['Movie release date'].apply(extract_year)
    raw_movies_data.drop(columns=["Movie release date"], inplace=True)
    #Replace " " by NaN
    raw_movies_data.replace(r'^\s*$', np.nan, regex=True, inplace=True)

    # The lines with nan values in genre and countries are removed
    raw_movies_data = raw_movies_data.dropna(subset=["Genres", "Countries", "Year"])
    
    #keep only until 2013
    raw_movies_data = raw_movies_data[raw_movies_data['Year'] <= 2013]

    raw_movies_data = raw_movies_data.dropna(subset=["Year"])
    raw_movies_data['Year'] = raw_movies_data['Year'].astype(int)

    return raw_movies_data


def preprocess_events(raw_events_data, first_movie_year, last_movie_year):
    raw_events_data.drop(columns=["Place Name","Date", "Month","Sl. No"], inplace = True)
    raw_events_data = raw_events_data[~raw_events_data['Year'].str.contains('BC')]
    
    #make the date values more convenient to work with, by converting the column ['Year'] from str to int
    raw_events_data.loc[:, 'Year'] = raw_events_data.loc[:, 'Year'].astype(int)
    
    #remove historical events that happened before the first movie was released
    raw_events_data = raw_events_data[raw_events_data['Year'] >= first_movie_year]
    raw_events_data = raw_events_data[raw_events_data['Year'] <= last_movie_year]
    
    #Replace USSR and Soviet Union by Russia as we are interested in the geographical location of the events
    raw_events_data = replace_in_columns(raw_events_data, 'Country', 'USSR', 'Russia')
    raw_events_data = replace_in_columns(raw_events_data, 'Country', 'Soviet Union', 'Russia')

    #Replace name of countries to the appropriate format
    raw_events_data = replace_in_columns(raw_events_data, 'Country', 'USA', 'United States of America')
    raw_events_data = replace_in_columns(raw_events_data, 'Country', 'UK', 'United Kingdom')
    raw_events_data = replace_in_columns(raw_events_data, 'Country', 'Zhanaozen', 'Kazakhstan')

    #Actually ! 'Tehran' is the capital of Iran
    raw_events_data = replace_in_columns(raw_events_data, 'Country', 'Tehran', 'Iran')

    return raw_events_data