import random

topOfRange = int(input("Type a number: "))

if topOfRange <= 0:
    print("Please enter a number larger than 0")
    quit()

randomNumber = random.randint(1, topOfRange)

userGuesses = 0

while True:
    userGuesses += 1
    guess = int(input("Please enter the guess: "))

    if guess == randomNumber:
        print("You got it Right!")
        break
    elif guess > randomNumber:
        print("You are above the number!")
    else:
        print("You are below the number!")

print("You got it in" , userGuesses , "guesses!")
