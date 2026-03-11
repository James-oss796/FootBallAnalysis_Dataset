import pandas as pd

# load dataset
df = pd.read_csv("../data/results.csv")

# convert date column
df["date"] = pd.to_datetime(df["date"])

# create total goals column
df["total_goals"] = df["home_score"] + df["away_score"]

# 1. number of matches
num_matches = len(df)
print("Number of matches:", num_matches)

# 2. earliest and latest year
earliest_year = df["date"].dt.year.min()
latest_year = df["date"].dt.year.max()
print("Earliest year:", earliest_year)
print("Latest year:", latest_year)

# 3. number of unique countries
unique_countries = df["country"].nunique()
print("Unique countries:", unique_countries)

# 4. most frequent home team
most_home_team = df["home_team"].value_counts().idxmax()
print("Most frequent home team:", most_home_team)

# 5. average goals per match
avg_goals = df["total_goals"].mean()
print("Average goals per match:", avg_goals)

# 6. highest scoring match
highest_goals = df["total_goals"].max()
highest_match = df.loc[df["total_goals"].idxmax()]
print("Highest goals in a match:", highest_goals)
print(highest_match)

# 7. home vs away goals
home_goals = df["home_score"].sum()
away_goals = df["away_score"].sum()
print("Total home goals:", home_goals)
print("Total away goals:", away_goals)

# 8. most common total goals value
common_goals = df["total_goals"].mode()[0]
print("Most common total goals:", common_goals)