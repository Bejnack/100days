print("The Love Calculator is calculating your score...")
name1 = input("Please type in your name!\n") # What is your name?
name2 = input("Please type in your name!\n") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

def loveinName(namex, namey):
    
    name = namex + namey
    name_lower = str.lower(name)

    
    truenumber_t = name_lower.count("t")
    truenumber_r = name_lower.count("r")
    truenumber_u = name_lower.count("u")
    truenumber_e = name_lower.count("e")

    final_count_true = truenumber_t + truenumber_r + truenumber_u + truenumber_e
    #print(f"true = {final_count_true}")

    lovenumber_l = name_lower.count("l")
    lovenumber_o = name_lower.count("o")
    lovenumber_v = name_lower.count("v")
    lovenumber_e = name_lower.count("e")

    final_count_love = lovenumber_l + lovenumber_o + lovenumber_v + lovenumber_e
    #print(f"love = {final_count_love}")

    
    final_score = int(str(final_count_true)+str(final_count_love))

    #print(f"Your score is {final_score}")
    return final_score

if loveinName(name1, name2) < 10 or loveinName(name1, name2) > 90:
    print(f"Your score is {loveinName(name1, name2)}, you go together like coke and mentos.")
elif loveinName(name1, name2) >= 40 and loveinName(name1, name2) <= 50:
    print(f"Your score is {loveinName(name1, name2)}, you are alright together.")
else:
    print(f"Your score is {loveinName(name1, name2)}.")