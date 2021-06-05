import random

logo = """
 _______           _______  _______  _______    _______    _                 _______  ______   _______  _______ 
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \  (  ___  )  ( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )
| (    \/| )   ( || (    \/| (    \/| (    \/  | (   ) |  |  \  ( || )   ( || () () || (   ) )| (    \/| (    )|
| |      | |   | || (__    | (_____ | (_____   | (___) |  |   \ | || |   | || || || || (__/ / | (__    | (____)|
| | ____ | |   | ||  __)   (_____  )(_____  )  |  ___  |  | (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)
| | \_  )| |   | || (            ) |      ) |  | (   ) |  | | \   || |   | || |   | || (  \ \ | (      | (\ (   
| (___) || (___) || (____/\/\____) |/\____) |  | )   ( |  | )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__
(_______)(_______)(_______/\_______)\_______)  |/     \|  |/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/
"""

print(logo)
random_number = int(random.randint(0, 100))
print("Welcome to the number game.")
skill_level = input(
    "Do you want to play on easy or hard? Type 'easy' or 'hard'\n")

if skill_level == 'easy':
    counter = 10
elif skill_level == 'hard':
    counter = 5

while counter != 0:
    print(f"You have {counter} guesses remaining.")
    guess = int(input("Guess a number: "))

    if guess == random_number:
        print("That's correct! You win!")
        counter = 0
    elif guess > random_number:
        print("Too high.")
        counter -= 1
    elif guess < random_number:
        print("Too low.")
        counter -= 1
