def count_words_in_file(filename):
    word_counts = {}
    with open(filename, 'r') as file:
        words = file.read().split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    return word_counts
filename = 'python.txt'
word_counts = count_words_in_file(filename)
for word, count in word_counts.items():
    print(f"'{word}': {count}")