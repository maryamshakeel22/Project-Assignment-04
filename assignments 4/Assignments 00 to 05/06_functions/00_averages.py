
# Write a function that takes two numbers and finds the average between the two.

# Solution



def find_average(num1, num2):
    """function that takes two numbers and finds the average"""
    return (num1 + num2) / 2

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        avg = find_average(num1, num2)
        print(f"The average of {num1} and {num2} is: {avg}")
    except Exception:
        print("Invalid input! Please enter numeric values.")
