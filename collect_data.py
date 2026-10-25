import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()

API_KEY = os.getenv("RAWG_API_KEY")

# RAWG games API endpoint
url = "https://api.rawg.io/api/games"

# Store all collected games here
all_games = []

# Collect 3 pages of results
for page in range(1, 4):

    params = {
        "key": API_KEY,
        "page_size": 40,
        "page": page
    }

    print(f"Collecting page {page}...")

    response = requests.get(url, params=params)

    if response.status_code == 200:

        data = response.json()

        # Add this page's games to our list
        all_games.extend(data["results"])

        print(f"Page {page}: {len(data['results'])} games collected")

    else:
        print("API request failed.")
        print("Status code:", response.status_code)


# Create a list for our cleaned data
game_data = []

# Extract the fields we need
for game in all_games:

    # Get genre names
    genres = [genre["name"] for genre in game.get("genres", [])]

    game_data.append({
        "name": game.get("name"),
        "released": game.get("released"),
        "rating": game.get("rating"),
        "ratings_count": game.get("ratings_count"),
        "genres": ", ".join(genres)
    })


# Convert the data into a Pandas DataFrame
df = pd.DataFrame(game_data)

# Remove duplicate games using the game name
df = df.drop_duplicates(subset=["name"])

# Display the number of games collected
print(f"\nTotal unique games collected: {len(df)}")

# Display the first 10 games
print("\nFirst 10 games:")
print(df.head(10))

# Save the data to a CSV file
df.to_csv("video_game_data.csv", index=False)

print("\nData saved to video_game_data.csv")