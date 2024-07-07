programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}


travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

travel_log_list = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    },
]

print(type(travel_log["France"]))

programming_dictionary["hello"] = "Hello World"
print(programming_dictionary)

travel_log["France"][0] = "France_Paris"
print(travel_log["France"][0])
