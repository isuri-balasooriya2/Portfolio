import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("nyt_books_data_2019_onwards.csv")
#print(df.isnull().sum())
#print(df.duplicated().sum())

df = df.sort_values(['title', 'date'])
df['rank_last_week'] = df.groupby('title')['rank'].shift(1)
df['on_list_next_week'] = df.groupby('title')['date'].shift(-1).notnull().astype(int)

def rule_based_predict(row):
    if row['weeks_on_list'] >= 5:
        return 1
    elif row['rank'] <= 5:
        return 1
    elif pd.notnull(row['rank_last_week']) and (row['rank_last_week'] < row['rank']):
        return 0
    else:
        return 0

df['predicted_stay'] = df.apply(rule_based_predict, axis=1)
correct = (df['predicted_stay'] == df['on_list_next_week']).sum()
total = df['on_list_next_week'].notnull().sum()

accuracy = correct / total
print(f"Rule-based accuracy: {accuracy:.2%}")

# Author consistency
author_retention = df.groupby('author')['on_list_next_week'].mean().sort_values(ascending=False)
print(author_retention.head())

top_authors = author_retention.head(10)

plt.figure(figsize=(10, 6))
top_authors.plot(kind='barh', color='skyblue')
plt.xlabel('Retention Rate')
plt.title('Top 10 Authors by Retention Rate')
plt.gca().invert_yaxis()  # Highest at top
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
