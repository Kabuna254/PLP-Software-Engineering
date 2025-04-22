import pandas as pd

# Create a DataFrame (table-like structure)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'Score': [85, 90, 95]
}

df = pd.DataFrame(data)

print(df)

# Access column
print("Names:", df['Name'])

# Filter rows
print("Scores above 90:")
print(df[df['Score'] > 90])