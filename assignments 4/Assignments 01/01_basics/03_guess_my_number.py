# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48


#Solution

import random
random_number = random.randint(0 , 99)

def guess(guess: int) -> int:
    while guess != random_number:
        if guess > random_number:
            print("Your guess is too high")
        elif guess < random_number:    
            print("Your guess is too low")    
        
        guess = int(input("Enter a new  number:"))
    print("Congrats! The number was: " , guess)   

def main():
    print("I am thinking of a number between 0 and 99... ")

    number = int(input("Enter a guess:"))
    guess(number)

if __name__ == "__main__":
    main()
