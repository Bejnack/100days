import random
#new_numbers = [new_item for item in list]
#How to remember
# #
# numbers = [1,2,3]
# new_number = [n+1 for n in numbers]

# name = "Angela"
# new_list =[letter for letter in name]
# print(new_list)

# list =[number + 1 for number in range(1,5)]
# print(list)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# caps_names = [name.upper() for name in names if len(name) > 4]
# print(caps_names)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# student_score ={
#     student:random.randint(1,100) for student in names
# } 

# #passed_students = {new_key:new_value for (key,value) in dictionary.items() if test}


# passed_students = {student:score for (student, score) in student_score.items() if score >= 60}
# print(passed_students)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(temp * 9/5)+32 for (day, temp) in weather_c.items()}

print(weather_f)

for key in weather_c:
    print(key)
    print(weather_f[key])