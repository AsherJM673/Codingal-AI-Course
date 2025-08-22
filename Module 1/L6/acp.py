import pandas as pd
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# Sample movie data
movies = [
    {'title': 'Inception', 'genre': 'Sci-Fi', 'imdb': 8.8, 'overview': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task.'},
    {'title': 'La La Land', 'genre': 'Romance', 'imdb': 8.0, 'overview': 'A jazz pianist falls for an aspiring actress in Los Angeles.'},
    {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'imdb': 9.3, 'overview': 'Two imprisoned men bond over a number of years.'},
    {'title': 'Inside Out', 'genre': 'Animation', 'imdb': 8.2, 'overview': 'After young Riley is uprooted from her Midwest life, her emotions conflict on how best to navigate a new city.'},
    {'title': 'Joker', 'genre': 'Crime', 'imdb': 8.5, 'overview': 'In Gotham City, mentally troubled comedian Arthur Fleck is disregarded by society.'}
]

df = pd.DataFrame(movies)

# Sentiment Analysis
sia = SentimentIntensityAnalyzer()
df['sentiment'] = df['overview'].apply(lambda x: sia.polarity_scores(x)['compound'])

def recommend_movies(genres=None, mood=None, min_rating=0, ai_based=True, num_recommendations=3):
    filtered = df.copy()
    if genres:
        filtered = filtered[filtered['genre'].isin(genres)]
    if min_rating:
        filtered = filtered[filtered['imdb'] >= min_rating]
    if mood:
        if mood.lower() == "positive":
            filtered = filtered[filtered['sentiment'] > 0.2]
        elif mood.lower() == "negative":
            filtered = filtered[filtered['sentiment'] < -0.2]
        elif mood.lower() == "neutral":
            filtered = filtered[(filtered['sentiment'] >= -0.2) & (filtered['sentiment'] <= 0.2)]
    if filtered.empty:
        print("No movies match your criteria.")
        return
    if ai_based:
        # Sort by IMDb rating and sentiment
        filtered = filtered.sort_values(['imdb', 'sentiment'], ascending=[False, False])
        recommendations = filtered.head(num_recommendations)
    else:
        recommendations = filtered.sample(n=min(num_recommendations, len(filtered)))
    for _, row in recommendations.iterrows():
        print(f"\nTitle: {row['title']}\nGenre: {row['genre']}\nIMDb Rating: {row['imdb']}\nOverview Sentiment: {row['sentiment']:.2f}")

# --- Example Interactions ---
# User input simulation:
user_genres = ['Drama', 'Sci-Fi']     # e.g. input("Enter preferred genres (comma separated): ").split(',')
user_mood = "positive"                # e.g. input("Mood (positive, negative, neutral or leave blank): ")
user_min_rating = 8.0                 # e.g. float(input("Minimum IMDb rating: "))
ai_choice = True                      # e.g. input("AI-based recommendations? (yes/no): ").lower() == 'yes'

recommend_movies(user_genres, user_mood, user_min_rating, ai_choice)
