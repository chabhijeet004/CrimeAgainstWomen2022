import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your cleaned dataset
df = pd.read_excel("C:/Users/HP/Desktop/PROJECT/CrimeAgainstWomen2022/Project_Dataset.xlsx")  # Replace with actual filename

# Optional: Drop non-crime columns (like State, District)
df_numeric = df.select_dtypes(include='number')  # Only numerical columns

# Calculate correlation matrix
correlation_matrix = df_numeric.corr()

# Display heatmap
plt.figure(figsize=(16, 12))
sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Between Different Crime Categories", fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()