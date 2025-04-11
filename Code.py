import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel("c:/Users/HP/Desktop/PROJECT/CrimeAgainstWomen2022/Project_Dataset.xlsx")
print("file readed successfully")

print(df.head())
print(df.tail())

print(df.info())
df.columns = df.columns.str.strip()

#objective 1: identifying high risk states for women
cols = df.columns[[3,4,5,6,7,8,9,16,19,22,28,29,30,31,32,33,34,35,36,37,38,39,41,44,45]]

statewise_crime = df.groupby("State")[cols].sum()

statewise_crime["Total_Crimes"] = statewise_crime.sum(axis=1)

top_risk_states = statewise_crime.sort_values("Total_Crimes", ascending=False)

# Plot
top_risk_states["Total_Crimes"].head(10).plot(kind='bar', color='crimson')
plt.title("Top 10 High-Risk States for Women")
plt.ylabel("Total Crime Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


