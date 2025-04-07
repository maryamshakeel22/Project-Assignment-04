
# Problem Statement
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 
# 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

#Solution

def  get_user_numbers():
    user_number: list[int] = []


    while True:
        number = input("Enter a number (press Enter to stop): ")
        if number == "":
            break
        number = int(number)
        user_number.append(number)
    return user_number

def count_nums(num_list):
    num_dict ={}
    for i in num_list:
        if i not in num_dict:
            num_dict[i]  =1
        else:
            num_dict[i] += 1
    return num_dict


def print_num_count(num_dict):
    for key in num_dict:
        print(f"{key} appears {str(num_dict[key])} times")
   

def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_num_count(num_dict)


#function to run code
if __name__ == "__main__":
    main()
