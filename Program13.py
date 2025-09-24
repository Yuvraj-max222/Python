#Write a program which will take a list of integer as input and create a dictionary with number as key and its prime factor as list of integers.
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n = i
            if i not in factors:
                factors.append(i)
    if n > 1 and n not in factors:
        factors.append(n)
    return factors
input_numbers = input("Enter a list of integers separated by commas: ")
try:
    numbers = list(map(int, input_numbers.split(',')))
    result = {num: prime_factors(num) for num in numbers}
    print("Dictionary of numbers and their prime factors:")
    print(result)
except ValueError:
    print("Please enter valid integers separated by commas.")