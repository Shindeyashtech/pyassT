import pandas as pd

# Load the Excel file
file_path = "large_data.xlsx"  # Update with your file path if needed
excel_file = pd.ExcelFile(file_path)

# Load data from the first sheet
df = excel_file.parse('Sheet1')

# 1. Filter: Select rows where Salary > 60000
filtered_df = df[df["Salary"] > 60000]

# 2. Sort: Sort by Age in descending order
sorted_df = filtered_df.sort_values(by="Age", ascending=False)

# 3. Group: Group by Age and calculate average salary
grouped_df = sorted_df.groupby("Age")["Salary"].mean().reset_index()
grouped_df = grouped_df.rename(columns={"Salary": "Average_Salary"})

# Save the modified dataset to a new Excel file
output_path = "modified_data.xlsx"
grouped_df.to_excel(output_path, index=False)

print("Modified dataset saved to", output_path)
