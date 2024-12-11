import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv('data.csv')

df.plot(x='Name', y='Minutes Per Year', kind='bar')

plt.title('Spotify Wrapped: Minutes Per Year by User', fontsize=16)
plt.xlabel('User Name', fontsize=14)
plt.ylabel('Minutes Per Year', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
 
 
plt.tight_layout()