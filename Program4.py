#Write a program to find the second largest number among three numbers using nested if else statement.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b:
    if a >= c:
        if b >= c:
            second_largest = b
        else:
            second_largest = c
    else:
        second_largest = a