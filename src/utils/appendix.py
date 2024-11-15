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
        # Use pd.to_datetime for other formats and extract the year
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