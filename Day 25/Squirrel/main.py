import csv

'''Reading all of the CSV File'''
# with open("100-days-of-code\Day 25\weather_data.csv") as data:
#     print(data.readlines())

'''Using CSV Reader to navigate through columns/rows'''
# with open("100-days-of-code\Day 25\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if(row[1] != "temp"):
#             temperatures.append(int(row[1]))
#     print(temperatures)


'''Using pandas library to read CSV'''
import pandas
data = pandas.read_csv("100-days-of-code\Day 25\\Squirrel\weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# average = data["temp"].mean()
# # average = sum(temp_list)/len(temp_list)
# print(average)
max = data["temp"].max()
# print(max)
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

