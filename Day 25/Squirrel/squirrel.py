import pandas

data = pandas.read_csv("100-days-of-code\Day 25\\Squirrel\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

'''Determine how many gray, black, and cinnamon squirrels there are based off of "Primary Fur Color"'''

colors = data["Primary Fur Color"]
'''Shows how many of each at a glance'''

# grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
# cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])


grey_squirrels = colors.value_counts().Gray
black_squirrels = colors.value_counts().Black
cinnamon_squirrels = colors.value_counts().Cinnamon

print(f"Gray Squirrels: {grey_squirrels}, Black Squirrels: {black_squirrels}, Cinnamon Squirrels: {cinnamon_squirrels}")

data_dict= {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels,cinnamon_squirrels,black_squirrels]
}

df = pandas.DataFrame(data_dict)

df.to_csv(".\\100-days-of-code\\Day 25\\Squirrel\\squirrel_count.csv")