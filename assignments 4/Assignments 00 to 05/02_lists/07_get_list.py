# Problem Statement
# Write a program which continuously asks the user to enter values which are added one by one into a list. 
# When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']



def get_list(lst):
    """Function to print the entire element of the list"""
    print("Here's the list:" , lst) 

def prompt_list():
    """Prompt the user to enter elements for the list"""
    lst = []
    prompt = input("Enter an element to add to the list (press Enter to stop): ")
    while prompt != "":
        lst.append(prompt)
        prompt = input("Enter the next element (press Enter to stop): ")
    return lst
    

def main():
    lst = prompt_list()
    get_list(lst)


if __name__ == "__main__":
    main()