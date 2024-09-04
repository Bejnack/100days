# with open("D:\\Repo\\100days\\100DaysofPython\\Intermediate\\9_File_Manipulation\\2_file_man\\my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("D:\\Repo\\100days\\100DaysofPython\\Intermediate\\9_File_Manipulation\\2_file_man\\my_file.txt", mode ='w') as file:
#     file.write("New Text")
    
# with open("D:\\Repo\\100days\\100DaysofPython\\Intermediate\\9_File_Manipulation\\2_file_man\\my_file.txt", mode ='a') as file:
#     file.write("\nNew Text")
    
# with open("D:\\Repo\\100days\\100DaysofPython\\Intermediate\\9_File_Manipulation\\2_file_man\\new_file.txt", mode ='w') as file:
#     file.write("\nNew Text")
    
with open(r".\100DaysofPython\Intermediate\9_File_Manipulation\2_file_man\new_file.txt", mode ='w') as file:
    file.write("\nNew Text")