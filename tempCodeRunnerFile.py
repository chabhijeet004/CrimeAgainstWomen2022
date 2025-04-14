
# # Get all crime columns (assuming they start from the 4th column)
# crime_columns = data.columns[3:]

# # Filter only numeric crime data
# crime_data = data[crime_columns].select_dtypes(include='number')

# # Sum total crimes per district
# data["Total_Crimes"] = crime_data.sum(axis=1)

# # Sort districts by lowest total crimes
# safest_districts = data.sort_values(by="Total_Crimes").reset_index(drop=True)

# # Show top 10 safest districts
# top_10_safest = safest_districts[["State", "District", "Total_Crimes"]].head(5)
# print("🛡️ Top 10 Safest Districts (Least Crimes Reported Against Women):\n")
# print(top_10_safest)

# plt.figure(figsize=(10, 6))
# plt.bar(top_10_safest["District"], top_10_safest["Total_Crimes"], color='green')
# plt.xlabel("Total Crimes")
# plt.title("Top 10 Safest Districts for Women (Least Crimes)")
# plt.gca().invert_yaxis()  # Highest at the top
# plt.tight_layout()
# plt.show()