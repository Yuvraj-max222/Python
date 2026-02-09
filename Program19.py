#Write a Python Program to Count the Occurrences of every words in a Text File.
def word_count(file_path):
    counts = {}    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
    return counts  