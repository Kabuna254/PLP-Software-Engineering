# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Load the dataset
try:
    iris_raw = load_iris(as_frame=True)
    iris_df = iris_raw.frame
    print("Dataset loaded successfully.\n")
except FileNotFoundError:
    print("Dataset file not found. Please ensure the path is correct.")
    exit()

# Display the first few rows
print("First 5 rows of the dataset:\n", iris_df.head())

# Check data types and missing values
print("\nData types:\n", iris_df.dtypes)
print("\nMissing values:\n", iris_df.isnull().sum())

# Clean the dataset
iris_df.dropna(inplace=True)  # No missing values, but this is safe

# Task 2: Basic Data Analysis
print("\nStatistical Summary:\n", iris_df.describe())

# Grouping by species and computing mean of numerical columns
group_means = iris_df.groupby("target")[
    ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]
].mean()
print("\nMean values grouped by species target:\n", group_means)

# Map numeric target to species names
iris_df['species'] = iris_df['target'].map(dict(enumerate(iris_raw.target_names)))

# Task 3: Visualizations

# 1. Line chart: Cumulative average petal length by index (simulating time series)
iris_df["cumulative_avg_petal_len"] = iris_df["petal length (cm)"].expanding().mean()
plt.plot(iris_df.index, iris_df["cumulative_avg_petal_len"])
plt.title("Cumulative Average Petal Length Over Records")
plt.xlabel("Index")
plt.ylabel("Cumulative Avg Petal Length (cm)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar chart: Average petal length per species
sns.barplot(x="species", y="petal length (cm)", data=iris_df, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of sepal width
sns.histplot(iris_df["sepal width (cm)"], kde=True, bins=15)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Scatter plot: Sepal length vs. Petal length
sns.scatterplot(data=iris_df, x="sepal length (cm)", y="petal length (cm)", hue="species")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.show()

# Findings
print("\nObservations:")
print("- Setosa species have smaller petal length and width.")
print("- Versicolor and Virginica are closer in sepal sizes but differ in petal dimensions.")
print("- Petal length and sepal length show a positive correlation.")
print("- Data appears clean and well-structured with no missing values.")
