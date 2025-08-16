import pandas as pd
import os 
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

DATA_PATH = r"C:\Users\athul\Desktop\Learn\Project\Movie Project\Data\Cleaned"
Merged_file = os.path.join(DATA_PATH, "merged_movies.xlsx")

df = pd.read_excel(Merged_file, sheet_name="Merged_movies_cleaned")

correlation = df[['averageRating', 'revenue']].corr(method='pearson')
print("Correlation between rating and revenue:\n", correlation)

#plt.figure(figsize=(10,6))
#sns.scatterplot(data=df, x='averageRating', y='revenue', alpha=0.5)
#plt.title("IMDb Rating vs Box Office Revenue")
##plt.xlabel("Average IMDb Rating")
#plt.ylabel("Box Office Revenue")
#plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x/1e6:.0f}M'))
#plt.grid(True)
#plt.show()
 
#plt.figure(figsize=(8,5))
#sns.histplot(df['averageRating'], bins=20, kde=True)
#plt.title("Distribution of IMDb Ratings")
#plt.xlabel("Rating")
#plt.ylabel("Count")
#plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
#plt.show()#

correlation = df[['averageRating', 'revenue']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap: Rating vs Revenue")
plt.show()
