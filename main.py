# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather-data.csv")
# print(data["temp"])

# this prints Pandas Dataframe
# print(type(data))

# this prints Pandas Series
# print(type(data["temp"]))

# turn dataframe into a dictionary
# data_dict = data.to_dict()
# print(data_dict)
#
# # turn series into a list
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # finding average temperature
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# # finding average temperature with series methods
# print(data["temp"].mean())
#
# # get data in columns. these are the same
# print(data["condition"])
# print(data.condition)

# get data in rows. this prints Monday 12 Sunny
# print(data[data.day == "Monday"])

# create a dataframe from scratch
# data_dict = {
#         "students": ["Amy", "James", "Angela"],
#         "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# # create a csv file from a dataframe
# data.to_csv("new_data.csv")

import pandas

# copy needed data from csv file and save squirrel's count for their fur color
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

# use squirrel's count to create dictionary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

# convert dictionary into dataframe and use that to create a csv
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")