import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

df = pd.read_csv("owid-covid-data.csv")
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")
df["month"] = df["date"].dt.to_period("M")

df['total_cases'].fillna(0,inplace=True)
df['new_cases'].fillna(0,inplace=True)
df['total_deaths'].fillna(0,inplace=True)
df['new_deaths'].fillna(0,inplace=True)

df['stringency_index'].fillna(0,inplace=True)
df['population_density'].fillna(0,inplace=True)
df['median_age'].fillna(0,inplace=True)
df['aged_65_older'].fillna(0,inplace=True)
df['aged_70_older'].fillna(0,inplace=True)
df['gdp_per_capita'].fillna(0,inplace=True)
df['extreme_poverty'].fillna(0,inplace=True)
df['cardiovasc_death_rate'].fillna(0,inplace=True)
df['diabetes_prevalence'].fillna(0,inplace=True)
df['female_smokers'].fillna(0,inplace=True)
df['male_smokers'].fillna(0,inplace=True)
df['life_expectancy'].fillna(0,inplace=True)
df['human_development_index'].fillna(0,inplace=True)

#print(df.isnull().sum())

df['iso_code'].replace({'OWID_ENG':'ENG'},inplace=True)

# Sort values for correct rolling application
df = df.sort_values(["iso_code", "date"])

monthly_cases = df.groupby(["iso_code","month"])["new_cases"].sum().reset_index()
monthly_cases["month"] = monthly_cases["month"].dt.to_timestamp()

plt.figure(figsize=(14,6))
sns.lineplot(data=monthly_cases, x="month", y="new_cases", hue="iso_code",marker='o')
plt.title("Monthly New COVID-19 Cases")
plt.xlabel("Month")
plt.ylabel("Total Cases")
plt.legend(title="Country")
plt.tight_layout()
plt.show()

#Question 1
df["new_cases"] = pd.to_numeric(df["new_cases"], errors="coerce")
df["population"] = pd.to_numeric(df["population"], errors="coerce")
df["cases_per_100k"] = (df["new_cases"] / df["population"]) * 100000

df_monthly = (
    df.groupby(["iso_code", pd.Grouper(key="date", freq="M")])
    .agg({"cases_per_100k": "sum"})  # You could use sum too
    .reset_index()
)

plt.figure(figsize=(14,6))
sns.lineplot(data=df_monthly, x="date", y="cases_per_100k", hue="iso_code")
plt.title("Monthly COVID-19 Cases per 100,000 People")
plt.xlabel("Date")
plt.ylabel("Cases per 100k")
plt.xticks(rotation=45)
plt.legend(title="Country")
plt.tight_layout()
plt.show()

#Question 2
iso_code = 'ITA'
country_df = df[df['iso_code'] == iso_code]

testing = country_df.groupby(pd.Grouper(key="date", freq="M")
).agg({
    "new_cases": "sum",
    "new_tests": "sum",
    "positive_rate": "sum"
}).reset_index()

plt.figure(figsize=(14,6))

sns.lineplot(data=testing, x="date", y="new_cases", label="New Cases")
sns.lineplot(data=testing, x="date", y="new_tests", label="New Tests")
sns.lineplot(data=testing, x="date", y="positive_rate", label="Positive Rate")

plt.title(f"Monthly Trends for {iso_code}")
plt.xlabel("Month")
plt.ylabel("Counts / Rate")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

#Question 3
iso_code = 'ITA'
country_df = df[df['iso_code'] == iso_code]

country_df["vaccination_rate"] = (country_df["people_fully_vaccinated"] / country_df["population"]) * 100
monthly_df = country_df.groupby(pd.Grouper(key="date", freq="M")).agg({
    "new_cases": "sum",
    "vaccination_rate": "max"
}).reset_index()

fig, ax1 = plt.subplots(figsize=(14, 6))

ax1.set_title(f"{iso_code} - Vaccination Rate vs Monthly New Cases")
ax1.set_xlabel("Date")
ax1.set_ylabel("New Cases", color="tab:blue")
ax1.plot(monthly_df["date"], monthly_df["new_cases"], color="tab:blue", label="New Cases")
ax1.tick_params(axis='y', labelcolor="tab:blue")
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)

ax2 = ax1.twinx()
ax2.set_ylabel("Vaccination Rate (%)", color="tab:green")
ax2.plot(monthly_df["date"], monthly_df["vaccination_rate"], color="tab:green", linestyle="--", label="Vaccination Rate")
ax2.tick_params(axis='y', labelcolor="tab:green")

fig.tight_layout()
plt.show()

#Question 4
country_df["stringency_index"] = pd.to_numeric(country_df["stringency_index"], errors="coerce")
monthly_stringency = country_df.groupby(pd.Grouper(key="date", freq="M")).agg({
    "new_cases": "sum",
    "stringency_index": "mean"
}).reset_index()

fig, ax1 = plt.subplots(figsize=(12,6))

ax1.plot(monthly_stringency["date"], monthly_stringency["new_cases"], color="red", label="New Cases")
ax1.set_xlabel("Date")
ax1.set_ylabel("New Cases", color="red")
ax1.tick_params(axis="y", labelcolor="red")

ax2 = ax1.twinx()
ax2.plot(monthly_stringency["date"], monthly_stringency["stringency_index"], color="blue", label="Stringency Index")
ax2.set_ylabel("Stringency Index", color="blue")
ax2.tick_params(axis="y", labelcolor="blue")

plt.title("Monthly New COVID-19 Cases vs. Government Stringency Index")
fig.tight_layout()
plt.show()

#Question 5
cols = [
    "new_cases", "new_tests", "positive_rate",
    "people_fully_vaccinated", "stringency_index",
    "hospital_patients", "icu_patients"
]
subset = df[cols].dropna()

correlation = subset.corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

#Question 6
monthly_trends = df.groupby(["iso_code", pd.Grouper(key="date", freq="M")]).agg({
    "new_cases": "sum",
    "new_deaths": "sum",
    "stringency_index": "mean",
    "positive_rate": "mean"
}).reset_index()

plt.figure(figsize=(14, 6))
sns.lineplot(data=monthly_trends, x="date", y="stringency_index", hue="iso_code")
plt.title("Government Response Stringency Over Time")
plt.xlabel("Date")
plt.ylabel("Stringency Index")
plt.show()

df.to_csv("covid-data-cleaned.csv",index=False)