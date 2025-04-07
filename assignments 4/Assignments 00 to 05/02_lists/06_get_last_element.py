# Problem Statement
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element
#  in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.


#solution

def get_last_element(lst):
    """Function to print the last element of the list"""
    print("Here's the last element of the list:" ,lst[len(lst) - 1])
     #or
    # print(list[-1]) 

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
    get_last_element(lst)


if __name__ == "__main__":
    main()