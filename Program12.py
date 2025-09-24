#The program takes a string and counts the frequency of words appearing in that string using a dictionary.
def word_frequency(s):
    words = s.split()
    freq = {}
    for word in words:
        word = word.lower()
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
            return freq
input_string = input("Enter a string: ")
frequency = word_frequency(input_string)
print("Word frequency in the given string:")
for word, count in frequency.items():
    print(f"{word}: {count}")