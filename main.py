# ======================================================
# DATA VISUALIZATION - NETFLIX DATASET PROJECT
# ======================================================

#  Importing Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

#  Set Seaborn Theme for Better Aesthetics
sns.set(style="whitegrid", palette="Set2")

#  Load Dataset
df = pd.read_csv("netflix_titles.csv")

#  Quick Glance at Data
print("Dataset Shape:", df.shape)
print("Columns:", df.columns)
print("\nMissing Values:\n", df.isnull().sum())

#  Basic Data Cleaning
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce', format='mixed')
df['year_added'] = df['date_added'].dt.year
df['release_year'] = df['release_year'].astype('Int64')

# ======================================================
# 1. Content Growth Over Time
# ======================================================
plt.figure(figsize=(10,5))
df['year_added'].value_counts().sort_index().plot(kind='bar', color='salmon')
plt.title("Number of Netflix Titles Added Each Year", fontsize=14)
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# ======================================================
# 2. Type Distribution (Movies vs TV Shows)
# ======================================================
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type', palette='viridis')
plt.title("Distribution of Movies and TV Shows", fontsize=14)
plt.xlabel("Type of Content")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ======================================================
# 3. Top 10 Countries Producing Netflix Content
# ======================================================
top_countries = df['country'].dropna().str.split(',').explode().str.strip().value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='mako')
plt.title("Top 10 Countries Producing Netflix Content", fontsize=14)
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# ======================================================
# 4. Most Common Genres
# ======================================================
genres = df['listed_in'].dropna().str.split(',').explode().str.strip().value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=genres.values, y=genres.index, palette='coolwarm')
plt.title("Top 10 Most Common Genres on Netflix", fontsize=14)
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()

# ======================================================
# 5. Ratings Distribution
# ======================================================
plt.figure(figsize=(10,5))
sns.countplot(data=df, y='rating', order=df['rating'].value_counts().index, palette='pastel')
plt.title("Distribution of Content Ratings on Netflix", fontsize=14)
plt.xlabel("Count")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()


# ======================================================
# Insights Summary
# ======================================================
print("Key Insights:")
print("- Netflix added most of its titles after 2015, showing rapid content growth.")
print("- Movies dominate the platform compared to TV Shows.")
print("- The US and India are the top content producers on Netflix.")
print("- Popular genres include Dramas, Comedies, and International Movies.")
print("- TV-MA and TV-14 are the most common content ratings, showing focus on mature audiences.")
