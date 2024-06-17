from db import my_dict
# The Above code help you to use the data of some other file in your file

# print(my_dict)

# TODO 1: Find How many student live in Mohali and Chandigarh
city_filter_List = ['Mohali', 'Chandigarh']  # by using list we can easily select and filter the cities.
live = 0
for student in my_dict:
    student_city = my_dict[student]['Address']['City']
    if student_city in city_filter_List:
        live += 1
print(f'Total {live} students live in {city_filter_List}')


# TODO 3: Show the marks of each student in Math.
# Output Must be like this: <Student Name> got <Marks> in English.

subject_to_search = 'Math'
for student in my_dict.values():
    # print(student['Subjects'])
    if subject_to_search in student['Subjects']:
        index = student['Subjects'].index('Math')
        print(f"{student['Name']}(RollNo: {student['RollNo.']}) got {student['Marks'][index]} "
              f"in {student['Subjects'][index]}")


# TODO 2: Show the marks of each student in English.
# Output Must be like this: <Student Name> got <Marks> in English.

for student in my_dict.values():
    index = student['Subjects'].index('Math')
    # here you can also pass subject through a variable like
    # Subject = 'Maths'
    # doing this code will work Dynamically.
    print(f"{student['Name']} got {student['Marks'][index]} in {student['Subjects'][index]}")
