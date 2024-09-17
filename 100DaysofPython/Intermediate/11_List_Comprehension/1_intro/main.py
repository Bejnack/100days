
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

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
caps_names = [name.upper() for name in names if len(name) > 4]
print(caps_names)