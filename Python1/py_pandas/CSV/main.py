import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_dict = data.to_dict()
c = 0
g = 0
b = 0
data_dict_dict = {"Fur Color": [],
                  "Count": []}
for x in data_dict["Primary Fur Color"]:
    if data_dict["Primary Fur Color"][x] == "Black":
        b = b + 1
    if data_dict["Primary Fur Color"][x] == "Gray":
        g = g + 1
    if data_dict["Primary Fur Color"][x] == "Cinnamon":
        c = c + 1
data_dict_dict["Fur Color"].append("Black")
data_dict_dict["Fur Color"].append("Gray")
data_dict_dict["Fur Color"].append("Cinnamon")
data_dict_dict["Count"].append(b)
data_dict_dict["Count"].append(g)
data_dict_dict["Count"].append(c)

data_dict_DF = pd.DataFrame(data_dict_dict)
data_dict_DF.to_csv("Squirrel_Data.csv")
