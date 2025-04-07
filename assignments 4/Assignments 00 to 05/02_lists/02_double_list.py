# Problem Statement
# Write a program that doubles each element in a list of numbers. For example, if you start 
# with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]


def main():
    #list
    numbers: list[int] = [1, 2, 3, 4]
    #loop through the list
    for i in range(len(numbers)):
        index_elem = numbers[i] 
        numbers[i] = index_elem * 2
    print(numbers)    

    

# function to run the code
if __name__ == "__main__":
    main()