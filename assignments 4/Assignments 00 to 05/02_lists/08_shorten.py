# Problem Statement
# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, 
# and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than
#  MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes 
# it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but 
# feel free to change it around to test your program.


#Solution

def shorten(lst):
    """Function to remove elements from the end of the list until it is MAX_LENGTH items long"""
    MAX_LENGTH = 3
    while len(lst) > MAX_LENGTH:
        removed_element = lst.pop()
        print(f"Removing {removed_element} from the list")

def prompt_list():
    """Prompt the user to enter elements for the list"""
    lst = []
    elem = input("Enter an element to add to the list (press Enter to stop): ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter the next element (press Enter to stop): ")
    return lst        

def main():
    lst = prompt_list()
    shorten(lst)
    #print the final list after shorten
    print(f"Final list after shortening: {lst}")  


#function to run the code
if __name__ == "__main__":
    main()