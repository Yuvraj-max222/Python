#Write a program to find the value of the function:
#F(x) = 3x² + 5 if x <= 10
#     = 5x if x > 10 and x <= 20
#     = 2x² - x + 9 if x > 20
#Input the value of x in Python.

def calculate_F(x):
    if x <= 10:
        return 3 * x**2 + 5
    elif x <= 20:
        return 5 * x
    else:
        return 2 * x**2 - x + 9
try:
    x = float(input("Enter the value of x: "))
    result = calculate_F(x)
    print(f"F({x}) = {result}")
except ValueError:
    print("Please enter a valid number.")