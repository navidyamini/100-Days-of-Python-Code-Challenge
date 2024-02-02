import pandas as pd

# read data
squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# find unique colors
unique_colors = squirrel_data["Primary Fur Color"].unique().tolist()
# Remove the nan value
unique_colors.remove(unique_colors[0])
# count the number of each color
count_color = []
for color in unique_colors:
    count_color.append(squirrel_data["Primary Fur Color"].value_counts()[color])
# create dictionary
data_dict = {
    "Fur Color": unique_colors,
    "Count": count_color
}
# convert dictionary to pandas df
data = pd.DataFrame(data_dict)
# save dataframe into csv file
data.to_csv("squirrel_count.csv")
