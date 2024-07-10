from menu import MENU

choise = input("espresso: ").lower()
for key in MENU[choise]["ingredients"]:
    print(key)
    print(MENU[choise]["ingredients"][key])
    MENU[choise]["cost"] += 1.5
    print(MENU[choise]["cost"]) 
    
    #print(MENU[choise]["ingredients"][key])