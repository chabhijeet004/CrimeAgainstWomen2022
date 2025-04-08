import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel("c:/Users/HP/Desktop/PROJECT/CrimeAgainstWomen2022/Project_Dataset.xlsx")
print("file readed successfully")

print(data.info())
# data.columns = data.columns.str.strip()

correlation = data[['Cruelty by Inlaws', 'Suicide of Women']].corr().iloc[0, 1]
# data_subset = data.iloc[:,[3,12]]

# # Compute correlation
# corr = data_subset.corr()

# # Plot heatmap
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.heatmap(correlation, annot=True, cmap='coolwarm')
# plt.title("Correlation between Dowry Deaths and Cruelty by Inlaws")
# plt.show()

age_segmented = data[[
 'Rape of Women (above 18)',
 'Rape of Women (Below 18)',
 'Attempt to rape Women (above 18)',
 'Attempt to rape Girls (Below 18)',
 'Assault on Women (18 Yrs. And above)',
 'Assualt on Girls (Below 18 yrs)'  # Note: "Assualt" is misspelled in the dataset
]].sum()

# Plotting
age_segmented.plot(kind='bar', color=['salmon', 'tomato', 'skyblue', 'royalblue', 'lightgreen', 'green'])
plt.title('Crimes Against Girls Under 18 vs Women Over 18')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_rape = data.groupby('District')[['Rape of Women (above 18)', 'Rape of Women (Below 18)']].sum()
top_rape['Total Rape Cases'] = top_rape.sum(axis=1)
top_10_rape = top_rape.sort_values('Total Rape Cases', ascending=False).head(10)
print(top_10_rape)

top_10_rape[['Rape of Women (above 18)', 'Rape of Women (Below 18)']].plot(kind='bar', stacked=True)
plt.title('Top 10 Districts by Rape Cases (Segmented by Age)')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



cruelty_suicide = data.groupby('State')[['Cruelty by Inlaws', 'Suicide of Women']].sum()
cruelty_suicide['Suicide-Cruelty Ratio'] = cruelty_suicide['Suicide of Women'] / (cruelty_suicide['Cruelty by Inlaws'] + 1)
top_cruel_states = cruelty_suicide.sort_values('Cruelty by Inlaws', ascending=False).head(10)
print(top_cruel_states)

top_cruel_states[['Cruelty by Inlaws', 'Suicide of Women']].plot(kind='bar')
plt.title('Top States by Cruelty and Suicides of Women')
plt.ylabel('Case Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


df = data.dropna()
df = data[["State", "Cruelty by Inlaws"]]

statewise_rape_cases = df.groupby("State")["Cruelty by Inlaws"].sum().sort_values(ascending=True)

# Set figure size 
plt.figure(figsize=(12, 6))

# Create bar plot
sns.barplot(x=statewise_rape_cases.index, y=statewise_rape_cases.values)

# Format the plot
plt.xticks(rotation=90)
plt.xlabel("State")
plt.ylabel("Total Rape Cases")
plt.title("Total Rape Cases per State")
# plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show plot
plt.show()