
# Problem Statement
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how 
# variable scope works.


#Solution:

from random import randint

def roll_dice():
    dice1 = randint(1 , 6)
    dice2 =randint(1 , 6)
    result = dice1 + dice2
    print(f"Die 1: {dice1}, Die 2: {dice2} → Total: {result}")



def main():
    for i in range(3):
        print(f"Roll {i+1}:")
        roll_dice()
        print()  # Ek empty line for readability



if __name__ == "__main__":
    main()    

