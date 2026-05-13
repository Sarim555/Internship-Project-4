import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Dataset for Data Analytics - Sheet1.csv")

# Display data
print(df.head())

# Bar Chart
plt.figure(figsize=(8,5))
df['Category'].value_counts().plot(kind='bar')
plt.title('Category Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.savefig('bar_chart.png')
plt.show()

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df['Sales'], bins=10)
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.savefig('histogram.png')
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df['Sales'], df['Profit'])
plt.title('Sales vs Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.savefig('scatter_plot.png')
plt.show()

# Heatmap
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('heatmap.png')
plt.show()