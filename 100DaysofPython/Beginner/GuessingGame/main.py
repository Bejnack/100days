from GuessingGame_art import intro_art
import random

difficulty_options = {
    "easy": 10,
    "hard": 5,    
}

def guess_number(goal_number):
    guessed_number = int(input("Make a guess: "))
    if guessed_number == goal_number:
        print(f"You got it! The answer was {guessed_number}")
        return False
    elif guessed_number > goal_number and difficulty_options[difficulty_choise] > 1:
        print("Too high!\nGuess again")
        difficulty_options[difficulty_choise] -= 1
        return True
    elif guessed_number < goal_number and difficulty_options[difficulty_choise] > 1:
        print("Too low!\nGuess again")
        difficulty_options[difficulty_choise] -= 1
        return True
    elif difficulty_options[difficulty_choise] <= 1:
        print("No attempts remaining! Game Over!")
        return False

def maingame():
    still_playing = True

    print(intro_art)
    randomnumber = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {randomnumber}.")
    global difficulty_choise
    difficulty_choise = input("Choose a difficulty! 'easy' or 'hard'. ").lower()
    #difficulty_options[difficulty_choise]
    while still_playing == True:
        still_playing = guess_number(randomnumber)
    if input("Do you want to try again? 'yes' or 'no': ").lower() == "yes":
        maingame()

maingame()

