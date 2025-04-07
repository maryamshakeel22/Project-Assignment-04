
# Problem Statement
# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first
#  element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.


#Solution

def get_first_element(lst):
    """fumnction to print the first element of the list"""

    print("Here's the first element of the list:" , lst[0])


def prompt_list():
    "prompt the user to get the elements f the list"
    lst: list = []
    prompt = input("Please enter the element to add to the list:")
    while prompt != "":
        lst.append(prompt)
        prompt = input("please enter the next elemnet to add to the list or press enter to stop:")
    return lst
    

def main():
    lst = prompt_list()
    get_first_element(lst)


if __name__ == "__main__":
    main()    




    
