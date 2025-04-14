#Libraries used
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Reading DataSet
data=pd.read_excel("C:/Users/HP/Desktop/PROJECT/CrimeAgainstWomen2022/Project_Dataset.xlsx")
print("Data imported succesfully")

print(data.head())


data.info()


print(data.describe())

print("\nMissing Values:\n", data.isnull().sum())


print("\nDuplicate Rows:", data.duplicated().sum())

#objective 1: identifying high risk states for women
cols = data.columns[[3,4,5,6,7,8,9,16,19,22,28,29,30,31,32,33,34,35,36,37,38,39,41,44,45]]

statewise_crime = data.groupby("State")[cols].sum()

statewise_crime["Total_Crimes"] = statewise_crime.sum(axis=1)

top_risk_states = statewise_crime.sort_values("Total_Crimes", ascending=False)
top_risk_states["Total_Crimes"].head(10).plot(kind='bar', color='crimson')
plt.title("Top 10 High-Risk States for Women")
plt.ylabel("Total Crime Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#objective 2: Correlation Between Female Suicides and Cruelty by In-laws
df_relevant = data[['Suicide of Women', 'Cruelty by Inlaws']]


correlation = df_relevant.corr()
plt.figure(figsize=(6, 4))
sns.set(style='whitegrid')
heatmap = sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap: Female Suicides vs Cruelty by In-laws")
plt.tight_layout()
plt.show()
# Objective 3: Correlation Between Female Suicides and Cruelty by In-laws
suicide_col = "Suicide of Women"
cruelty_col = "Cruelty by Inlaws"

# Compute correlation
correlation_value = data[[suicide_col, cruelty_col]].corr().iloc[0, 1]

# Scatter plot to visualize the relationship
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x=cruelty_col, y=suicide_col, alpha=0.6)
sns.regplot(data=data, x=cruelty_col, y=suicide_col, scatter=False, color="red", label=f"Corr: {correlation_value:.2f}")
plt.title("Correlation Between Female Suicides and Cruelty by In-laws")
plt.xlabel("Cruelty by In-laws")
plt.ylabel("Suicide of Women")
plt.legend()
plt.show()

correlation_value






#objective N
crime_data = data.iloc[:, 3:]

crime_totals = crime_data.sum().sort_values(ascending=False)
top_10_crimes = crime_totals.head(10)
print("Top 10 Most Prevalent Crimes Against Women:\n")
print(top_10_crimes)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_crimes.values, y=top_10_crimes.index, palette='magma')
plt.title('Top 10 Most Prevalent Crimes Against Women')
plt.xlabel('Total Cases')
plt.ylabel('Crime Category')
plt.show()




#objective 3: 1.To compare the frequency of crimes committed against women above 18 and girls below 18 using age-segmented data columns such as rape, attempt to rape, and assault
adult_crimes = ['Rape ', 'Rape of Women (above 18)', 'Sexual Harassment']
minor_crimes = ['Child Rape', 'Sexual Assault of Children', 'Use of Child for Pornography']

adult_total = data[adult_crimes].sum().sum()
minor_total = data[minor_crimes].sum().sum()

crime_comparison = pd.Series({'Women (18+)': adult_total, 'Girls (<18)': minor_total})

# Plotting
plt.figure(figsize=(6, 5))
sns.barplot(x=crime_comparison.index, y=crime_comparison.values)
plt.title('Comparison of Crimes Against Women vs Girls')
plt.ylabel('Total Cases')
plt.xlabel('Age Group')

plt.show()



crime_data = data.iloc[:, 3:]

# Get top 15 crimes based on total counts
top_15_crimes = crime_data.sum().sort_values(ascending=False).head(10).index.tolist()

# Create correlation matrix for these top 15
filtered_corr = crime_data[top_15_crimes].corr()

# Get top correlated crime pairs (excluding self-correlation)
corr_unstacked = filtered_corr.unstack()
corr_unstacked = corr_unstacked[corr_unstacked.index.get_level_values(0) != corr_unstacked.index.get_level_values(1)]
corr_sorted = corr_unstacked.sort_values(ascending=False).drop_duplicates()

# Show top 10 correlated pairs
top_10_pairs = corr_sorted.head(10)
print("🔗 Top 10 Most Correlated Crime Pairs Among Top 15 Categories:\n")
print(top_10_pairs)

# Optional: Small heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(filtered_corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Among Top 15 Crimes Against Women")
plt.tight_layout()
plt.show()
# Reading DataSet
data=pd.read_excel("C:/Users/HP/Desktop/PROJECT/CrimeAgainstWomen2022/Project_Dataset.xlsx")
print("Data imported succesfully")
exclude_cols = ['SNo', 'Year', 'State/UT', 'District']
crime_cols = [col for col in data.columns if col not in exclude_cols and data[col].dtype in ['int64', 'float64']]

# Group by State/UT and calculate total crimes
state_crimes = data.groupby('State')[crime_cols].sum()
state_crimes['Total Crimes'] = state_crimes.sum(axis=1)

# Sort and get top 10 states
top10_states = state_crimes['Total Crimes'].sort_values(ascending=False).head(10)

# Plot pie chart
plt.figure(figsize=(10, 8))
plt.pie(top10_states, labels=top10_states.index, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 9})
plt.title('Top 10 States Contributing to National Crimes Against Women', fontsize=14)
plt.tight_layout()
plt.show()






