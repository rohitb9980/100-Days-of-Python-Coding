# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])


#
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260712.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_direct = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "count" : [gray_squirrels_count, cinnamon_squirrel_count, black_squirrel_count]
    }

df = pandas.DataFrame(data_direct)
df.to_csv("output.csv", index=False)



