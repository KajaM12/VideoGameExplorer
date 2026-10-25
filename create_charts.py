import pandas as pd
import matplotlib.pyplot as plt

# Load the collected data
df = pd.read_csv("video_game_data.csv")

# Remove missing genre values
genre_data = df.dropna(subset=["genres"]).copy()

# Split games with multiple genres
genre_data["genres"] = genre_data["genres"].str.split(", ")

# Put each genre on its own row
individual_genres = genre_data.explode("genres")

# Calculate average rating for each genre
genre_ratings = (
    individual_genres
    .groupby("genres")["rating"]
    .mean()
    .sort_values(ascending=False)
)

# Create the chart
plt.figure(figsize=(10, 6))

genre_ratings.plot(kind="bar")

plt.title("Average Video Game Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

# Save the chart
plt.savefig("average_rating_by_genre.png", dpi=300)

# Display the chart
plt.show()


# Calculate total ratings associated with each genre
genre_popularity = (
    individual_genres
    .groupby("genres")["ratings_count"]
    .sum()
    .sort_values(ascending=False)
)

# Create the popularity chart
plt.figure(figsize=(10, 6))

genre_popularity.plot(kind="bar")

plt.title("Total Ratings Associated with Each Genre")
plt.xlabel("Genre")
plt.ylabel("Total Ratings")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save and display the chart
plt.savefig("genre_popularity.png", dpi=300)
plt.show()
