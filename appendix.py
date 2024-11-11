import pandas as pd
import ast

def extract_names(cell):
    #Transform the string of dictionaries into a list of real dictionaries with the id referring to the key and the name referring to the value
    #Then only extract the names from the dictionaries
    try:
        data_dict = ast.literal_eval(cell)
        return ", ".join(data_dict.values())
    except (ValueError, SyntaxError):
        return cell
    
    
def extract_year(date_str):
    if len(date_str) == 4 and date_str.isdigit():
        return date_str
    else:
        # Use pd.to_datetime for other formats and extract year
        return pd.to_datetime(date_str, errors='coerce').year
    
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