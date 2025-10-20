# Program to count occurrences of every word in a text file
def count_words(filename):
    word_count = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.lower().strip(".,!?;:\"'()[]{}")
                if word:
                    word_count[word] = word_count.get(word, 0) + 1
    return word_count
filename = "python.txt"
counts = count_words(filename)
for word, count in counts.items():
    print(f"{word}: {count}")