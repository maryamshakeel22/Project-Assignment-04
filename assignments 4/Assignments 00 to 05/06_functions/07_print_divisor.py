
# Problem Statement
# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors
#  (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the 
# division). Don't forget to call your function in main()!

# Here's a sample run (user input is in blue):

# Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12

#Solution

def divisors(num):
    for i in range(num):
        curr_divisor = i +1
        if num % curr_divisor == 0:
            print(curr_divisor , end=" ")

def main():
    num = int(input("Enter a number:"))
    print(f"The divisors of {num} are :" , end=" ")
    divisors(num)


if __name__  == "__main__":
    main()
