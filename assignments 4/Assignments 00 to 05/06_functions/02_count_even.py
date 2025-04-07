
# Problem Statement
# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the
#  prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on


def count_even(lst):
    even_number = []
    
    while True:
        values = input("Enter an integer or press enter to stop")
        if values == "":
            break
        lst.append(int(values))

    for num in lst:
        if num % 2 == 0:
         even_number.append(num)
    print("Your list :" , lst)        
    print(f"Even numbers in the list are {even_number}")  
        

def main():
    
    list = []
    count_even(list)

if __name__ == "__main__":
    main()       
