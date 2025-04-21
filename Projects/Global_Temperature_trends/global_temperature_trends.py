from io import StringIO
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

url = "https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Land_and_Ocean_complete.txt"
response = requests.get(url)
text = response.text

#split into lines
lines = text.splitlines()

#skip metadata
data_lines = [line for line in lines if not line.startswith('%') and line.strip()]

#identify where actual data starts
data_start_index = None
for idx, line in enumerate(data_lines):
    if line.strip().startswith("1850"):  # The year value indicates the start of data rows
        data_start_index = idx
        break

#slice and clean the data
data_lines = data_lines[data_start_index:]

#rebuild the cleaned data into a string format for pandas to read
clean_data_str = "\n".join(data_lines)
data_io = StringIO(clean_data_str)

columns = [
    "Year", "Month", "Monthly Anomaly", "Monthly Unc.",
    "Annual Anomaly", "Annual Unc.", "Five-year Anomaly",
    "Five-year Unc.", "Ten-year Anomaly", "Ten-year Unc.",
    "Twenty-year Anomaly", "Twenty-year Unc."
]

df = pd.read_csv(data_io, delim_whitespace=True, names=columns, header=None)

df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['Month'] = pd.to_numeric(df['Month'], errors='coerce')

print(df.head())

#data cleaning
df['Annual Anomaly'].fillna(df['Annual Anomaly'].mean(),inplace=True)
df['Annual Unc.'].fillna(df['Annual Unc.'].mean(),inplace=True)
df['Five-year Anomaly'].fillna(df['Five-year Anomaly'].mean(),inplace=True)
df['Five-year Unc.'].fillna(df['Five-year Unc.'].mean(),inplace=True)
df['Ten-year Anomaly'].fillna(df['Ten-year Anomaly'].mean(),inplace=True)
df['Ten-year Unc.'].fillna(df['Ten-year Unc.'].mean(),inplace=True)
df['Twenty-year Anomaly'].fillna(df['Twenty-year Anomaly'].mean(),inplace=True)
df['Twenty-year Unc.'].fillna(df['Twenty-year Unc.'].mean(),inplace=True)

#print(df.isnull().sum())
#print(df.duplicated().sum())
#print(df['Year'].unique())
#print(df['Month'].unique())

df = df.rename(columns={'Annual Unc.': 'Annual Uncleaned', 'Five-year Unc.': 'Five-year Uncleaned','Ten-year Unc.':'Ten-year Uncleaned','Twenty-year Unc.':'Twenty-year Uncleaned'})

'''
plt.boxplot(df["Annual Anomaly"])
plt.show()
'''
df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)

plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Monthly Anomaly"], label="Monthly Anomaly", alpha=0.6)
plt.plot(df.index, df["Five-year Anomaly"], label="5-Year Avg", linewidth=2)
plt.title("Global Temperature Anomalies Over Time")
plt.ylabel("Temperature Anomaly (°C)")
plt.legend()
plt.grid(True)
plt.show()

df_annual = df[df['Month'] == 1]

X = df_annual['Year'].values
Y = df_annual['Annual Anomaly'].values

# Mean values
x_mean = np.mean(X)
y_mean = np.mean(Y)

# Calculate slope (a)
numerator = np.sum((X - x_mean) * (Y - y_mean))
denominator = np.sum((X - x_mean)**2)
a = numerator / denominator

# Intercept (b)
b = y_mean - a * x_mean

# Predict future years
future_years = np.arange(2025, 2051)
future_anomalies = a * future_years + b

plt.figure(figsize=(12, 6))
plt.scatter(X, Y, label='Historical Data', alpha=0.5)
plt.plot(X, a*X + b, color='blue', label='Regression Line')
plt.plot(future_years, future_anomalies, color='red', linestyle='--', label='Forecast (2025–2050)')
plt.title("Forecasting Global Temperature Anomalies")
plt.xlabel("Year")
plt.ylabel("Annual Temperature Anomaly (°C)")
plt.legend()
plt.grid(True)
plt.show()

# Define future range
future_years = np.arange(2025, 2051)

# Simulate each scenario
scenarios = {
    "Business as Usual": 1.2,
    "Moderate Action": 1.1,
    "Aggressive Action": 0.4
}

# Store results for plotting
scenario_predictions = {}

for name, factor in scenarios.items():
    modified_slope = a * factor
    future_temp = modified_slope * future_years + b
    scenario_predictions[name] = future_temp

# Plot all scenarios
plt.figure(figsize=(12, 6))
plt.plot(future_years, a * future_years + b, '--', label="Original Forecast", color='gray')

colors = ['red', 'orange', 'green']
for (name, temps), color in zip(scenario_predictions.items(), colors):
    plt.plot(future_years, temps, label=name, color=color)

plt.axhline(1.5, color='purple', linestyle=':', label="1.5°C Danger Threshold")
plt.title("Policy Scenario Simulations: Global Temperature Anomalies")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.legend()
plt.grid(True)
plt.show()

thresholds = [1.5, 2.0]

for scenario, temps in scenario_predictions.items():
    print(f"\nScenario: {scenario}")
    for threshold in thresholds:
        years_above = future_years[temps >= threshold]
        if len(years_above) > 0:
            print(f"Reaches {threshold}°C in year {years_above[0]}")
        else:
            print(f"Does not reach {threshold}°C by 2050")

def recommend_actions(year_crossed):
    if year_crossed <= 2030:
        return "⚠️ Immediate global carbon tax, accelerate renewables, deforestation ban"
    elif year_crossed <= 2040:
        return "⚠️ Moderate interventions needed: scale green infrastructure, reduce fossil subsidies"
    else:
        return "🟢 Continue current path, monitor closely"

# Apply recommendations
for scenario, temps in scenario_predictions.items():
    print(f"\n📘 Policy Guidance for: {scenario}")
    for threshold in thresholds:
        years_above = future_years[temps >= threshold]
        if len(years_above) > 0:
            year_crossed = years_above[0]
            print(f"  Threshold {threshold}°C breached in {year_crossed}:")
            print("   " + recommend_actions(year_crossed))
        else:
            print(f"  Threshold {threshold}°C not breached: No urgent action needed.")

