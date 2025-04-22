import matplotlib.pyplot as plt

countries = ['Kenya', 'India', 'Germany', 'Brazil', 'China']
populations = [43, 1391, 83, 213, 1440]  # in millions

plt.bar(countries, populations, color='blue')
plt.title("Population of 5 Countries (in millions)")
plt.xlabel("Country")
plt.ylabel("Population (millions)")
plt.tight_layout()
plt.show()


activities = ['Sleep', 'Classes', 'Study', 'Meals', 'Other']
hours = [6, 8, 3, 2, 5]

plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=90)
plt.title("Student's Daily Time Distribution")
plt.axis('equal')  # Makes the pie a circle
plt.tight_layout()
plt.show()


times = ['Morning', 'Noon', 'Evening', 'Night']
temperatures = [21, 28, 24, 20]  # in °C

plt.plot(times, temperatures, marker='o', linestyle='-', color='orange')
plt.title("Temperature Changes During the Day")
plt.xlabel("Time of Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()
