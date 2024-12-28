import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
movies = pd.DataFrame({
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['The Matrix', 'John Wick', 'Inception', 'The Dark Knight', 'Interstellar'],
    'genre': ['Action, Sci-Fi', 'Action, Thriller', 'Action, Sci-Fi', 'Action, Crime', 'Sci-Fi, Drama'],
    'description': [
        'A computer hacker learns from mysterious rebels about the true nature of his reality.',
        'A retired hitman seeks vengeance against those who wronged him.',
        'A thief who enters the dreams of others to steal secrets from their subconscious.',
        'A vigilante Batman faces a criminal mastermind known as the Joker.',
        'A team of explorers travels through a wormhole in space in search of a new home for humanity.'
    ]
})

# Step 1: Create a TF-IDF matrix based on movie descriptions
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies['description'])

# Step 2: Compute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Step 3: Build a function to recommend movies based on similarity
def recommend_movie(title, movies, cosine_sim):
    # Step 3.1: Find the index of the movie that matches the title
    idx = movies.index[movies['title'] == title].tolist()[0]

    # Step 3.2: Get the pairwise similarity scores for the movie with all other movies
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Step 3.3: Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Step 3.4: Get the top 3 most similar movies
    sim_scores = sim_scores[1:4]

    # Step 3.5: Get the movie indices and titles
    movie_indices = [i[0] for i in sim_scores]
    recommended_movies = movies['title'].iloc[movie_indices]
    
    return recommended_movies

# Step 4: Test the recommendation system
movie_to_recommend = 'The Matrix'
recommended_movies = recommend_movie(movie_to_recommend, movies, cosine_sim)

print(f"Movies recommended based on '{movie_to_recommend}':")
print(recommended_movies)
