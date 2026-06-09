import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data.csv")

# First 5 rows
print("First 5 Rows:")
print(data.head())

# Dataset information
print("\nDataset Info:")
print(data.info())

# Statistical Summary
print("\nStatistical Summary:")
print(data.describe())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Correlation Matrix
print("\nCorrelation:")
print(data.corr(numeric_only=True))

# Histogram
data.hist(figsize=(8,6))
plt.show()

# Box Plot
data.plot(kind='box', figsize=(8,6))
plt.show()
