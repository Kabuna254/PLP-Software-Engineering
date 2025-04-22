import pandas as pd

data = {
    'Name': ['Fabian', 'James', 'Barak'],
    'Age': [25, 26, 24],
    'Grade': [40, 60, 50]   
}

df = pd.DataFrame(data)
print(df)
print("\n")

df_Passed = df['Grade'] > 50
print(df_Passed)
