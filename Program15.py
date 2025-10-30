#Generate 100 random numbers between 101 and 200. Count the frequency of numbers in the different ranges.
import random
numbers = [random.randint(101, 200) for _ in range(100)]
ranges = {}
for i in range(101, 201, 25):
    range_key = f"{i}-{i+24}"
    count = sum(1 for num in numbers if i <= num <= i+24)
    ranges[range_key] = count
print("Frequency of numbers in different ranges:")
for range_key, count in ranges.items():
    print(f"Range {range_key}: {count} numbers")