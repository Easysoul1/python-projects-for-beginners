#Pratice exercises
# Question 1 Week 11
# Performing Data Analysis on iris dataset

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
data = pd.read_csv('./asset/iris.csv')
print("First 5 rows of the dataset:")
print(data.head())

# Perform exploratory data analysis
print("\nSummary statistics:")
print(data.describe())

print("\nInformation about the dataset:")
print(data.info())

print("\nChecking for missing values:")
print(data.isnull().sum())

# Visualize the data using various plots
# Pairplot
sns.pairplot(data, hue='species')
plt.title('Pairplot of Iris Dataset')
plt.show()

# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='species', y='sepal_length', data=data)
plt.title('Boxplot of Sepal Length by Species')
plt.show()

# Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='species', y='petal_length', data=data)
plt.title('Violin Plot of Petal Length by Species')
plt.show()

# Heatmap of correlation matrix
plt.figure(figsize=(10, 6))
numeric_data = data.select_dtypes(include=[float, int])  # Select only numeric columns
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

# Calculate summary statistics
summary_stats = data.describe()
print("\nSummary statistics:")
print(summary_stats)
