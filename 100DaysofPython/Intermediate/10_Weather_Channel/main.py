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
#print(data["temp"])
data_dict = data.to_dict()
#print(data_dict)
temp_list = data["temp"].to_list()
# # avr = sum(temp_list) / len(temp_list)
# # print(avr)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
#print(monday)
monday_temp = monday.temp[0]
fahrenheit_temp = (monday_temp * 9/5) + 32
print(fahrenheit_temp)

#formaula = (0°C × 9/5) + 32 = 32°F