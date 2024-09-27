import pandas as pd

# Import dataset (e.g., a CSV file)
# Replace 'your_dataset.csv' with the path to your dataset file
df = pd.read_csv('management.csv')

# Show dataset details
print("Number of Rows: ", df.shape[0])
print("Number of Columns: ", df.shape[1])
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Size (Total elements):", df.size)

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Statistical summary for numerical columns
print("\nSum of Numerical Columns:")
print(df.sum(numeric_only=True))

print("\nAverage of Numerical Columns:")
print(df.mean(numeric_only=True))

print("\nMin values of Numerical Columns:")
print(df.min(numeric_only=True))

print("\nMax values of Numerical Columns:")
print(df.max(numeric_only=True))

# Exporting the data after processing (for example, removing missing values)
# Replace 'exported_dataset.csv' with the path where you'd like to export the file
df_cleaned = df.dropna()  # Dropping rows with missing values as an example
df_cleaned.to_csv('exported_dataset.csv', index=False)
print("\nCleaned dataset exported successfully.")
