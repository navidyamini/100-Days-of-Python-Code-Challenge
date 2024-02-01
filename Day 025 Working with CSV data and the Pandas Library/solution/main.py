import csv
import pandas

# working with CSV
with open("weather_data.csv", mode="r") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# Using Pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

# Convert Pandas Dataframe to dictionary
data_dict = data.to_dict()
print(data_dict)

# Convert Pandas column to list
temp_list = data["temp"].tolist()
print(temp_list)

# calculate the mean value
avg = data["temp"].mean()
print(avg)

# find the max value
print(data["temp"].max())

# get data in columns
print(data["condition"])
print(data.condition)

# get the row
# find the row where day is equal to Monday
print(data[data.day == "Monday"])

# Print row with max temperature
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)

# Write into csv
data.to_csv("new_data.csv")
