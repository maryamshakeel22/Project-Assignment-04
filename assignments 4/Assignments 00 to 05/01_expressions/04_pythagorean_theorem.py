# Problem Statement
# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle 
# and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in
#  geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square 
# of the other two sides.

# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean
#  theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). 
# You will probably find math.sqrt() to be useful.

# Here's a sample run of the program (user input is in bold italics):

# Enter the length of AB: 3

# Enter the length of AC: 4

# The length of BC (the hypotenuse) is: 5.0



from math import sqrt

def main():
    #prompt the user to enter the length of two perpendicular of the righ triangle
    side1 = float(input("Enter the length of AB:"))
    side2 = float(input("Enter the length of AC:"))

    #calculate the hypotenuse
    side3 = sqrt(side1**2  +  side2 **2)
    hypothesis = side3

    #print the hypotenuse
    print(f"The length of BC (the hypothenuse) is: {hypothesis}")


if __name__ == "__main__":
    main()