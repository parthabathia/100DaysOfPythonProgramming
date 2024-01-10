import pandas as pd

squirrel_data = pd.read_csv("squirrel_data.csv")

# print(squirrel_data.columns)

fur_color_count = squirrel_data["Primary Fur Color"].value_counts()

print(fur_color_count)

fur_color_count.to_csv("squirrel_count.csv")