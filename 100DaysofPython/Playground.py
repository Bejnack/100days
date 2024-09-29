# seasons = ["Spring", "Summer", "Fall", "Winter"]

# for i, season in enumerate(seasons):
#     print(i, season)

dict1 = {
    'dict_in_dict1':{'cris': 1, 'beji':2, 'dorner':3},
    'dict_in_dict2':{'snow':4, 'snowy':5, 'cris':6},
}

dict_dynamic = {}
for item,key in dict1.items():
    print(item)
    print(key)
    for item1, key1 in dict1[item].items():
        if item1 not in dict_dynamic:
            dict_dynamic[item1] = 0
for item, key in dict_dynamic.items():
    for item1, key1 in dict1.items():
        for item2, key2 in dict1[item1].items():
            if item2 == item:
                #for ticket style add a for loop to check and after go into the if
                #out[typ][name] = price / in our case it will be dict[user][ticket_type] = number --- ticket type will be from the for loop condition
                dict_dynamic[item] += 1
print(dict_dynamic)

# names = []
# for item, key in dict1.items():
#     for item1, key1 in dict1[item].items():
#         if item1 not in names:
#             names.append(item1)
# print(names)

# amount={}
# for name in names:
#     for item, key in dict1.items():
#         for item1, key1 in dict1[item].items():
#             if name == item1:
#                 amount[name] += 1
# print(amount)