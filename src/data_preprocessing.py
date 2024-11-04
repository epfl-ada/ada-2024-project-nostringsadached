#Pour le nettoyage des données.

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

def clean_historical_data(data):
    # Traiter les valeurs manquantes
    # Supprimer les données avant l'année du premier film de cleaned_movie_data
    # Drop les colonnes qui ne nous intéressent pas 
    # Transformer les formats de dates pour l’analyse temporelle.
    return data.dropna()

def vectorize_historical_data(data):
    # tokenizer les evenements qui nous interesse pour pouvoir les faire correspondre avec ceux de movie_data
    return data.dropna()