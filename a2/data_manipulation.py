import pandas as pd

# Use the correct full path to your file
file_path = r"C:\Users\yashk\Desktop\pyassT\a2\large_data.xlsx"
excel_file = pd.ExcelFile(file_path)

# Load data from the first sheet
df = excel_file.parse('Sheet1')

# Filter: Salary > 60000
filtered_df = df[df["Salary"] > 60000]

# Sort by Age descending
sorted_df = filtered_df.sort_values(by="Age", ascending=False)

# Group by Age and calculate average salary
grouped_df = sorted_df.groupby("Age")["Salary"].mean().reset_index()
grouped_df = grouped_df.rename(columns={"Salary": "Average_Salary"})

# Save to a new Excel file
output_path = r"C:\Users\yashk\Desktop\pyassT\a2\modified_data.xlsx"
grouped_df.to_excel(output_path, index=False)

print("Modified dataset saved to", output_path)
