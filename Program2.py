#Sample List
numbers = [12, 4, 56, 8, 33, 7]
#Bubble Sort Logic
n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print("Sorted List in ascending order is: ")
print(numbers)