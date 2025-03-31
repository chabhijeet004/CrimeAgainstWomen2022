import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel("c:/Users/HP/Desktop/PROJECT/CrimeAgainstWomen2022/Project_Dataset.xlsx")
print("file readed successfully")

print(data.info())
data.columns = data.columns.str.strip()



df = data.dropna()
df = data[["State", "Rape"]]

statewise_rape_cases = df.groupby("State")["Rape"].sum().sort_values(ascending=True)

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