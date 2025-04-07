
# Problem Statement
# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

# Here's a sample run of the program (user input is in blue):

# Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!


#Solution 

def repeat(message:str , repeat_count: int):
   return " ".join([message] * repeat_count)


def main():
    message = str(input("Please type a message: "))
    repeat_count = int(input("Enter a number of times to repeat your message:"))
    repeat_message = repeat(message , repeat_count)
    print(repeat_message )


if __name__ == "__main__":
    main()    
