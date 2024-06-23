# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("Greeting ")
    print("Coders")
    print("!")

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(location = "Mexico", name = "Beji")