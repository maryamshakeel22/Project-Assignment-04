
# Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() 
# function for you which asks the user for a number, calls your code for double(num) , and prints the result.

# Here's a sample run of the program (user input in bold italics):

# Enter a number: 2 Double that is 4


def main(number):
    double_number = number * 2
    return double_number


if __name__ == "__main__":
    number = int(input("Enter a number:"))
    result = main(number)
    print(f"{number} Double that is {result}")
   
