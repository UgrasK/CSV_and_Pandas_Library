# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather-data.csv")
# print(data["temp"])

# this prints Pandas Dataframe
# print(type(data))

# this prints Pandas Series
# print(type(data["temp"]))

# turn dataframe into a dictionary
data_dict = data.to_dict()
print(data_dict)

# turn series into a list
temp_list = data["temp"].to_list()
print(temp_list)

# finding average temperature
average = sum(temp_list) / len(temp_list)
print(average)

# finding average temperature with series methods
print(data["temp"].mean())

# these are the same
print(data["condition"])
print(data.condition)
