#Write a Python Program to Count the Occurrences of every words in a Text File.
def word_count_in_file(file_path):
    freq = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1
    return freq