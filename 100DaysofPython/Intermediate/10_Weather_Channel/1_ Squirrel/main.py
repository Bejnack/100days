import pandas
data = pandas.read_csv(r"100DaysofPython\Intermediate\10_Weather_Channel\1_ Squirrel\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data["Primary Fur Color"])
grey = len(data[data["Primary Fur Color"] == "Gray"])
#print(grey)
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Grey", "Cinnemon", "Black"],
    "Count": [grey, cinnamon, black]
}
new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv(r"100DaysofPython\Intermediate\10_Weather_Channel\1_ Squirrel\new_data.csv")