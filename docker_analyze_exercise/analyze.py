import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('IMBD.csv')

df['rating'] = df['rating'].replace({'NAN': 0})
df['rating'] = df['rating'].astype(float)

highest_rating = df.sort_values(by='rating' , ascending=False)[['title' , 
                                                                'rating']].head(10)
plt.figure(figsize=(12, 4.5))
plt.style.use('seaborn-v0_8-white')
colors = plt.cm.viridis(np.linspace(0, 1, len(highest_rating)))
bars = plt.barh(highest_rating['title'], highest_rating['rating'], color=colors)

plt.title('TV shows with highest rating', size = 16)
plt.xlabel('Movie')
plt.ylabel('Score')
plt.gca().invert_yaxis()
plt.xlim(5, 10)
plt.savefig('plot.png')