import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Movie': ['Ghilli', 'Thuppakki', 'Mersal', 'Master',
              'Leo', 'Bigil', 'Kaththi', 'Beast'],
    
    'Year': [2004, 2012, 2017, 2021, 2023, 2019, 2014, 2022],
    
    'Rating': [8.1, 8.0, 7.8, 7.4, 7.5, 6.8, 8.0, 5.2],
    
    'BoxOffice_Crore': [50, 100, 250, 300, 600, 285, 130, 240],
    
    'Genre': ['Action', 'Action', 'Action',
              'Action', 'Action', 'Sports',
              'Action', 'Action']
}
df = pd.DataFrame(data)
print("Dataset:")
print(df)
print("\nDataset Info:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())
df.plot(
    x='Movie',
    y='Rating',
    kind='bar',
    figsize=(8,5),
    legend=False
)
plt.title('Vijay Movies Ratings')
plt.xlabel('Movie')
plt.ylabel('IMDb Rating')
plt.xticks(rotation=45)
plt.show()
df.plot(
    x='Movie',
    y='BoxOffice_Crore',
    kind='bar',
    figsize=(8,5),
    legend=False
)
plt.title('Box Office Collection of Vijay Movies')
plt.xlabel('Movie')
plt.ylabel('Collection (Crores)')
plt.xticks(rotation=45)
plt.show()
df['Rating'].plot(
    kind='hist',
    bins=5,
    figsize=(6,4)
)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()
df.plot(
    kind='scatter',
    x='Year',
    y='BoxOffice_Crore',
    figsize=(6,4)
)
plt.title('Year vs Box Office Collection')
plt.show()
correlation = df[['Year', 'Rating', 'BoxOffice_Crore']].corr()
print("\nCorrelation Matrix:")
print(correlation)
print("\nEDA Observations:")
print("1. Leo has the highest box office collection.")
print("2. Most Vijay movies in this dataset belong to the Action genre.")
print("3. Ghilli and Thuppakki have high ratings.")
print("4. Box office collections increased over the years.")
input("Press Enter to exit...")