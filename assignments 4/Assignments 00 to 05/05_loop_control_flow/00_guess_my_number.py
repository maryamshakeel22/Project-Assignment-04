
# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48


#Solution
import random

def guess_number():
    number = random.randint(0 , 99)
    guess = int(input("Enter a guess between 1 to 99: "))

    while guess != number:
        if guess > number:
            print("Your guess is too high")
        else:
            print("Your guess is too low ")    

        guess = int(input("Enter a new guess: ")) 
    # This runs only when the user correctly guesses the number
    print("Congrats! The number was:", number)

if __name__ == "__main__":
    guess_number()
