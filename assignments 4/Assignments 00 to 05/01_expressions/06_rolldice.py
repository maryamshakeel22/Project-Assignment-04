# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.


#Solution:

from random import randint
import time

def roll_dice():
    print("Rolling the dice... 🎲")
    time.sleep(1)  # Ek second ka delay for better effect
    dice1 = randint(1 , 6)
    dice2 = randint(1 , 6)
    result = dice1 + dice2
    print(f"Dice 1 : {dice1} , Dice 2 : {dice2} => Total : {result}")


def main():
    for i in range(3):
        print(f"Roll { i + 1}:")
        roll_dice()
        print()


if __name__ == "__main__":
    main()