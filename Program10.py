#Write a recursive function to find HCF of two numbers. Use the function to find the LCM of set of numbers.
def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)
def lcm(x, y):
    return (x * y) // hcf(x, y)
def lcm_of_list(numbers):
    from functools import reduce
    return reduce(lcm, numbers)
try:
    numbers = list(map(int, input("Enter a set of numbers separated by spaces: ").split()))
    if len(numbers) < 2:
        print("Please enter at least two numbers.")
    else:
        result = lcm_of_list(numbers)
        print(f"LCM of the set of numbers {numbers} is {result}")
except ValueError:
    print("Please enter valid integers.")