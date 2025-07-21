#Fibonacci Numbers
num = int(input("Enter a number: "))
a = 0
b = 1
found = False
while b <= num:
    if b == num:   
        found = True
        break
    a, b = b, a+b
if found or num == 0:
    print(f"{num} is a Fibonacci Number.")
else:
    print(f"{num} is not a Fibonacci Number")