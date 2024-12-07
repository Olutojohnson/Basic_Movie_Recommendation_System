# Basic Movie Recommendation System

This is a simple Python-based movie recommendation system that uses user ratings to recommend similar movies. The system calculates movie similarity using cosine similarity and suggests movies based on their ratings.

## Features

- Creates a user-item matrix from a dataset of user ratings.
- Calculates movie-to-movie similarity using cosine similarity.
- Recommends movies similar to a given movie.

## Dataset

The system uses a small dataset of users, movies, and ratings:

|    User   |    Movie    |  Rating  |
|-----------|-------------|----------|
|    Tayo   |  Inception  |    5     |
|    Tayo   |   Titanic   |    4     |
|    Tayo   |    Avatar   |    5     |
|    Ope    |  Inception  |    5     |
|    Ope    |    Avatar   |    4     |
|    Ope    |   Avengers  |    5     |
|  Olamide  |   Titanic   |    4     |
|  Olamide  |   Avengers  |    5     |

This dataset can be replaced with a larger or more complex dataset for broader functionality.

## Prerequisites

Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

## Usage

2. Running the Script
Run the script using the following command:

```bash
python script.py
```
