import os
import pandas as pd

DATA_PATH = os.path.join(os.getcwd(), "Data")

imdb_paths = {
    "basics": os.path.join(DATA_PATH, "IMDB", "title.basics.tsv"),
    "ratings": os.path.join(DATA_PATH, "IMDB", "title.ratings.tsv")
}

box_office_path = os.path.join(DATA_PATH, "TMDB", "Budget and Revenue.xlsx")

print("Loading IMDb basics")
imdb_basics = pd.read_csv(
    imdb_paths["basics"],
    sep="\t",
    low_memory=False,
    dtype=str
)

print("Loading IMDb ratings")
imdb_ratings = pd.read_csv(
    imdb_paths["ratings"],
    sep="\t",
    low_memory=False,
    dtype=str
)

print("Loading Box Office dataset")
box_office = pd.read_excel(box_office_path)

print("IMDb Basics shape:", imdb_basics.shape)
print("IMDb Ratings shape:", imdb_ratings.shape)
print("Box Office shape:", box_office.shape)

cleaned_path = os.path.join(DATA_PATH, "Cleaned")
os.makedirs(cleaned_path, exist_ok=True)

imdb_basics.to_csv(os.path.join(cleaned_path, "imdb_basics_cleaned.csv"), index=False)
imdb_ratings.to_csv(os.path.join(cleaned_path, "imdb_ratings_cleaned.csv"), index=False)
box_office.to_excel(os.path.join(cleaned_path, "box_office_cleaned.xlsx"), index=False)

print("Cleaned datasets saved to:", cleaned_path)
