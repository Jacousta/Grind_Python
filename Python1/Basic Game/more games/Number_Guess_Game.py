import random

number = random.randint(1, 100)
print("Welcome to number guess game:")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if difficulty == "easy":
    guess_right = True
    i = 1
    while guess_right:
        while i < 11 and guess_right:
            typed_number = int(input("Make a Guess:\n"))
            if i == 10 and typed_number != number:
                print("You've run out of guesses, you lose.")
            elif typed_number > number:
                print("Too high.")
                print("Guess again.")
                print("You have", 10 - i, " attempts remaining to guess the number.")
            elif typed_number < number:
                print("Too low.")
                print("Guess again.")
                print("You have", 10 - i, " attempts remaining to guess the number.")

            else:
                print("You Guessed Correct.\n")
                guess_right = False
            i = i + 1
elif difficulty == "hard":
    guess_right = True
    i = 1
    while guess_right:
        while i < 6 and guess_right:
            typed_number = int(input("Make a Guess:\n"))
            if i == 5 and typed_number != number:
                print("You've run out of guesses, you lose.")
            elif typed_number > number:
                print("Too high.")
                print("Guess again.")
                print("You have", 5 - i, " attempts remaining to guess the number.")
            elif typed_number < number:
                print("Too low.")
                print("Guess again.")
                print("You have", 5 - i, " attempts remaining to guess the number.")
            else:
                print("You Guessed Correct.\n")
                guess_right = False
            i = i + 1
else:
    print("Type Correct Input")
