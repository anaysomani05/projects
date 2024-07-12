import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/dataset_part_2.csv')

# Display the first 5 rows
print(df.head(5))

# Convert relevant columns to numeric, replacing non-numeric values with NaN
numeric_columns = ['Class', 'PayloadMass', 'FlightNumber']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Exploratory data analysis
plt.figure(figsize=(20, 6))
sns.scatterplot(x="FlightNumber", y="PayloadMass", hue="Class", data=df)
plt.xlabel("Flight Number", fontsize=20)
plt.ylabel("Pay load Mass (kg)", fontsize=20)
plt.show()

plt.figure(figsize=(20, 6))
sns.scatterplot(x="FlightNumber", y="LaunchSite", hue="Class", data=df)
plt.xlabel("Flight Number", fontsize=20)
plt.ylabel("Launch Site", fontsize=20)
plt.show()

plt.figure(figsize=(20, 6))
sns.scatterplot(x="LaunchSite", y="PayloadMass", hue="Class", data=df)
plt.xlabel("Launch Site", fontsize=20)
plt.ylabel("Pay load Mass (kg)", fontsize=20)
plt.show()

# Calculate mean Class by Orbit
temp = df.groupby("Orbit")["Class"].mean().reset_index()
temp["Class"] = temp["Class"] * 100
plt.figure(figsize=(10, 6))
sns.barplot(x="Orbit", y="Class", data=temp)
plt.show()

plt.figure(figsize=(20, 6))
sns.scatterplot(x="FlightNumber", y="Orbit", hue="Class", data=df)
plt.xlabel("FlightNumber", fontsize=20)
plt.ylabel("Orbit", fontsize=20)
plt.show()

plt.figure(figsize=(20, 6))
sns.scatterplot(x="PayloadMass", y="Orbit", hue="Class", data=df)
plt.xlabel("PayloadMass", fontsize=20)
plt.ylabel("Orbit", fontsize=20)
plt.show()

# Function to extract years from the date
def Extract_year(date):
    return date.split("-")[0] if isinstance(date, str) else np.nan

# Extract year and calculate success rate
df["year"] = df["Date"].apply(Extract_year)
df["Success Rate"] = df["Class"] * 100
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="year", y="Success Rate")
plt.show()

# Features engineering
features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
print(features.head())

# One-hot encoding
categorical_columns = ['Orbit', 'LaunchSite', 'LandingPad', 'Serial']
features_encoded = pd.get_dummies(features, columns=categorical_columns)

# Ensure all columns are numeric
for col in features_encoded.columns:
    features_encoded[col] = pd.to_numeric(features_encoded[col], errors='coerce')

# Convert to float64
features_encoded = features_encoded.astype('float64')

print(features_encoded.head())
print(features_encoded.dtypes)