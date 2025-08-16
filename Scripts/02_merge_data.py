import pandas as pd
import os


DATA_PATH = r"C:\Users\athul\Desktop\Learn\Project\Movie Project\Data\Cleaned"

imdb_basics = pd.read_csv(os.path.join(DATA_PATH, "imdb_basics_cleaned.csv"),
    low_memory=False)
imdb_ratings = pd.read_csv(os.path.join(DATA_PATH, "imdb_ratings_cleaned.csv"))
box_office = pd.read_excel(os.path.join(DATA_PATH, "box_office_cleaned.xlsx"))


merged_data = pd.merge(imdb_basics, imdb_ratings, on="tconst", how="inner")

final_data = pd.merge(
    merged_data,
    box_office,
    left_on=["primaryTitle", "startYear"],
    right_on=["title", "Release year"],
    how="inner"
)


output_path = os.path.join(DATA_PATH, "merged_movies.csv")
final_data.to_csv(output_path, index=False)

print("Merged dataset saved at:", output_path)
print("Final shape:", final_data.shape)
