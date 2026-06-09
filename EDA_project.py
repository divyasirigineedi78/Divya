import pandas as pd
import matplotlib.pyplot as plt

# Sample Dataset
data = {
    "Age": [20, 22, 21, 23, 24, 25, 26, 27],
    "Marks": [85, 90, 78, 88, 95, 92, 87, 89]
}

df = pd.DataFrame(data)

# First 5 Rows
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Correlation Matrix
print("\nCorrelation Matrix:")
print(df.corr())

# Histogram
df.hist(figsize=(8, 4))
plt.show()

# Box Plot
df.plot(kind='box', figsize=(6, 4))
plt.show()
