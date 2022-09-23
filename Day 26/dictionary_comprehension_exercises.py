sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
result = {key:len(key) for key in sentence.split(" ")}
# Write your code below:

#{'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

weather_f = {day:(temp*1.8 + 32) for (day, temp) in weather_c.items()}
# Write your code 👇 below:



print(weather_f)


