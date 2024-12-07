import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.preprocessing import StandardScaler

# Sample Movie Dataset
data = {
    'User': ['Tayo', 'Tayo', 'Tayo', 'Ope', 'Ope', 'Ope', 'Olamide', 'Olamide'],
    'Movie': ['Inception', 'Titanic', 'Avatar', 'Inception', 'Avatar', 'Avengers', 'Titanic', 'Avengers'],
    'Rating': [5, 4, 5, 5, 4, 5, 4, 5]
}


df = pd.DataFrame(data)

# User-Item Matrix
user_movie_matrix = df.pivot_table(index='User', columns='Movie', values='Rating').fillna(0)

# Cosine Similarity Between Movies
movie_matrix = user_movie_matrix.T
similarity_matrix = cosine_similarity(movie_matrix)

movie_similarity_df = pd.DataFrame(similarity_matrix, index=movie_matrix.index, columns=movie_matrix.index)

print("Movie Similarity Matrix:")
print(movie_similarity_df)

# Function to Recommend Movies
def recommend_movies(movie, similarity_matrix, top_n=3):
    if movie not in similarity_matrix.columns:
        return f"Movie '{movie}' not found in the dataset."
    
    # Similarity scores for the input movie
    similar_movies = similarity_matrix[movie].sort_values(ascending=False)[1:top_n+1]
    return similar_movies

recommendations = recommend_movies('Inception', movie_similarity_df, top_n=3)

print("\nMovies Recommended Based on 'Inception':")
print(recommendations)
