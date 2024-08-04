import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
dataset_path = '/kaggle/input/nba-stats-dataset-for-last-10-years/nba.csv'
df = pd.read_csv(dataset_path)

# Display the first few rows
print(df.head())

# Calculate average points per game by player
df['PTS_per_game'] = df['PTS'] / df['GP']
df[['PLAYER', 'PTS_per_game']].head()

# Calculate average assists per game by player
df['AST_per_game'] = df['AST'] / df['GP']
df[['PLAYER', 'AST_per_game']].head()

# Calculate average rebounds per game by player
df['REB_per_game'] = df['REB'] / df['GP']
df[['PLAYER', 'REB_per_game']].head()

# Plot average points per game for top 5 players
top_5_players = df.nlargest(5, 'PTS_per_game')
plt.figure(figsize=(10, 6))
sns.barplot(x='PLAYER', y='PTS_per_game', data=top_5_players)
plt.title('Top 5 Players by Average Points per Game')
plt.xlabel('Player')
plt.ylabel('Points per Game')
plt.show()

# Plot efficiency for top 5 players
top_5_efficiency = df.nlargest(5, 'EFF')
plt.figure(figsize=(10, 6))
sns.barplot(x='PLAYER', y='EFF', data=top_5_efficiency)
plt.title('Top 5 Players by Efficiency')
plt.xlabel('Player')
plt.ylabel('Efficiency')
plt.show()

# Summary statistics for the dataset
print(df.describe())
