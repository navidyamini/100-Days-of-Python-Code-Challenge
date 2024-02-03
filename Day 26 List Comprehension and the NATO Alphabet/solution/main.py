import random
import pandas


# How to create lists using comprehension
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)    
# We can convert it to
new_list = [n + 1 for n in numbers]
print(new_list)
# you can also work with strings
name = "Davide"
letters_list = [letter for letter in name]
print(letters_list)
# you can do it with the range
double_list = [n *2 for n in range(1,5)]
print(double_list)
# Conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
upper_case_names = [name.upper() for name in names if len(name) > 4]
print(upper_case_names)
# How to use dictionary comprehension
# loop over list
student_scores = {student: random.randint(1,100) for student in names}
print(student_scores)
# loop over dictionary
passed_students = {student: value for (student,value) in student_scores.items() if value > 74}
print(passed_students)
# Iterate over Pandas dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
student_data_frame = pandas.DataFrame(data_dict)
print(student_data_frame)
# Loop through rows of data frame
for(index, row) in student_data_frame.iterrows():
    print(row)
for(index, row) in student_data_frame.iterrows():
    print(row.scores)
for(index, row) in student_data_frame.iterrows():
    if row.students == "Amy":
        print(row.scores)