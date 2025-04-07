
# Problem Statement
# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high 
# is guaranteed to be greater than low. """


def in_range(n , low , high):
     return n >= low and n <= high  #comparision operator return True or false so we dont need to use if else statement
          

def main():
    print(in_range(5, 1, 10))  #return True
    print(in_range(15, 1, 10))   #return False


if __name__ == "__main__":
     main()            
