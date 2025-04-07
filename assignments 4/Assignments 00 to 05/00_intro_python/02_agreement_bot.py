
# Problem Statement
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

#  My favorite animal is also cow!

#Solution

def main():
    #Prompt the user to enter their favorite animal
    animal = input("Whats is your favorite  animal?")
    #Print the response
    print(f"My favorite animal is also {animal}!")



if __name__ == "__main__":
    main()
