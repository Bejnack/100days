# with open (r"Intermediate\10_Weather_Channel\weather_data.csv", 'r') as weather_data_doc:
#     data = weather_data_doc.readlines()
# print(data)

# -------------------------------------------------------------------------------------------------------

# import csv
# with open (r"Intermediate\10_Weather_Channel\weather_data.csv", 'r') as data_file:
#     data =csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

# -------------------------------------------------------------------------------------------------------

import pandas
data = pandas.read_csv(r"Intermediate\10_Weather_Channel\weather_data.csv")
print(data)