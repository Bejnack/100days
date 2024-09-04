#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
        
#access starting letter
with open("D:\Repo\\100days\\100DaysofPython\Intermediate\9_File_Manipulation\\3_mail_merger\Mail Merge Project Start\Input\Letters\starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    print(letter)
    

with open(r"D:\Repo\100days\100DaysofPython\Intermediate\9_File_Manipulation\3_mail_merger\Mail Merge Project Start\Input\Names\invited_names.txt") as invited_names:
    name_list = [line.rstrip('\n') for line in invited_names]
    
#letter.replace("[name],", f"{name_list[0]},")
for name in name_list:
    with open(rf"D:\Repo\100days\100DaysofPython\Intermediate\9_File_Manipulation\3_mail_merger\Mail Merge Project Start\Output\ReadyToSend\letter_for_{name}", mode='w') as file:
        file.write(letter.replace("[name],", f"{name},"))

#print(letter)