import pandas as pd 
import matplotlib.pyplot as plt
import requests
import numpy as np 

# 1
arr = np.arange(1, 11)
print("NumPy Array:", arr)
print("Mean of array:", np.mean(arr))

# 2
data = {
    'Name': ['Fabian', 'Barak', 'Jas'],
    'Score': [55, 70, 82],
    'Age': [25, 24, 26]
}

df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

# 3
response = requests.get('https://api.github.com')
if response.status_code == 200:
    print("\nGitHub API Response:")
    data = response.json()
    print("Current User URL:", data.get('current_user_url'))

# 4
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker='o', linestyle='-', color='yellow')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.tight_layout()
plt.show()