import math
import random
import datetime

print(math.sqrt(16))
print(math.pi)
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
print("Tomorrow's date is:", tomorrow)

print("Today's date is:", today)

now = datetime.datetime.now()
print("Current time:", now.strftime("%H:%M:%S"))


