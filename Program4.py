#Write a program to find the second largest number among three numbers using nested if else statement.
a = input("Enter the first number: ")
b = input("Enter the second number: ")
c = input("Enter the third number: ")
if a > b:
    if a < c:
        second = a
    elif b > c:
        second = b
    else:
        second = c
else:
    if b < c:
        second = b
    elif a > c:
        second = a
    else:
        second = c
print(f"The second largest number is: {second}")