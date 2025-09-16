#Write a program to find the longest sequence in ascending order from a list.
#Sample:
#Input: [10, 40, 25, 28, 7, 11, 15, 22, 20, 35, 42, 56, 80, 100, 99]
#Output: [20, 35, 42, 56, 80, 100]
def longest_ascending_sequence(lst):
    longest_seq = []
    current_seq = []

    for i in range(len(lst)):
        if i == 0 or lst[i] > lst[i - 1]:
            current_seq.append(lst[i])
        else:
            if len(current_seq) > len(longest_seq):
                longest_seq = current_seq
            current_seq = [lst[i]]

    if len(current_seq) > len(longest_seq):
        longest_seq = current_seq

    return longest_seq
numbers = [5, 8, 12, 3, 6, 9, 15, 18, 2, 4, 7, 10, 13, 17, 20]
result = longest_ascending_sequence(numbers)
print("Longest sequence in ascending order is:")
print(result)