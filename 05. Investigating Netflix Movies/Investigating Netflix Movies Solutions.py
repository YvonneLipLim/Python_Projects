# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Q1. What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration (use 1990 as the decade's start year).
movies_1990 = netflix_df[(netflix_df["release_year"] >= 1990) & (netflix_df["release_year"] <= 1999) & (netflix_df["type"] == "Movie")] # Get data for movies from 1990 and 1999
count_duration = movies_1990["duration"].value_counts() # Count frequency of the movie duration
most_freq_duration = count_duration.idxmax() # Find duration with highest frequency
duration = int(most_freq_duration) # Save most_freq_duration as integer
print(duration)

# Q2. A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as short_movie_count.
netflix_df["duration"] = netflix_df["duration"].astype(str) # Ensure 'duration' column is of string type before using .str accessor
movies_action_1990 = netflix_df[(netflix_df["release_year"] >= 1990) & (netflix_df["release_year"] <= 1999) & (netflix_df["type"] == "Movie") & (netflix_df["genre"].str.contains("Action"))] # Filter movies from 1990 and 1999, with genre as 'Action'
short_movie_count = movies_action_1990[movies_action_1990["duration"].str.replace("min", "").astype(int) < 90].shape[0] # Count short action movies
print(short_movie_count)
