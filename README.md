# Real-World Retail Sales Data Analysis Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Retail Dataset Creation
np.random.seed(42)

data = {
    'Order_ID': range(1, 101),
    'Product_Category': np.random.choice(['Electronics', 'Clothing', 'Groceries'], 100),
    'Sales_Amount': np.random.randint(100, 5000, 100),
    'Quantity': np.random.randint(1, 10, 100),
    'Customer_Age': np.random.randint(18, 60, 100)
}

df = pd.DataFrame(data)

# Display first 5 rows
print("Dataset Preview:")
print(df.head())

# Basic Information
print("\nDataset Information:")
print(df.info())

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Total Sales
total_sales = df['Sales_Amount'].sum()
print("\nTotal Sales:", total_sales)

# Sales by Category
category_sales = df.groupby('Product_Category')['Sales_Amount'].sum()
print("\nSales by Category:")
print(category_sales)

# Visualization 1: Sales by Category
plt.figure(figsize=(6,4))
category_sales.plot(kind='bar')
plt.title('Total Sales by Product Category')
plt.xlabel('Category')
plt.ylabel('Sales Amount')
plt.tight_layout()
plt.show()

# Visualization 2: Sales Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Sales_Amount'], bins=15)
plt.title('Sales Amount Distribution')
plt.xlabel('Sales Amount')
plt.show()

# Visualization 3: Quantity vs Sales
plt.figure(figsize=(6,4))
sns.scatterplot(x='Quantity', y='Sales_Amount', data=df)
plt.title('Quantity vs Sales Amount')
plt.show()

# Findings
print("\nProject Findings:")
print("1. Total sales generated:", total_sales)
print("2. Best performing category:", category_sales.idxmax())
print("3. Sales distribution analyzed.")
print("4. Relationship between quantity sold and sales amount visualized.")
