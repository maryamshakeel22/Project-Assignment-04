# Problem #1: List Practice
# Now practice writing code with lists! Implement the functionality described in the comments below.

#def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# Print the length of the list.


# Add 'mango' at the end of the list. 


# Print the updated list.



#Problem 1 solution:

def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print(len(fruit_list))
    fruit_list.append("mango")
    print(fruit_list)

if __name__ == "__main__":
    main()
