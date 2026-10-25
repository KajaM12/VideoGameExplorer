import pandas as pd

# Load our collected video game data
df = pd.read_csv("video_game_data.csv")

print("Total games:", len(df))

# Remove missing genre values
genre_data = df.dropna(subset=["genres"]).copy()

# Split games with multiple genres
genre_data["genres"] = genre_data["genres"].str.split(", ")

# Put each genre on its own row
individual_genres = genre_data.explode("genres")

# Count individual genres
genre_counts = individual_genres["genres"].value_counts()

print("\nMost common individual genres:")
print(genre_counts)

# Calculate average rating for each genre
genre_ratings = (
    individual_genres
    .groupby("genres")["rating"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage rating by genre:")
print(genre_ratings.round(2))

# Calculate total ratings for each genre
genre_popularity = (
    individual_genres
    .groupby("genres")["ratings_count"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTotal ratings by genre:")
print(genre_popularity)