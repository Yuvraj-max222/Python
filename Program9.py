#Write a function to find all odd length palindromes from a list. Call the function from a program.
def is_palindrome(s):
    return s == s[::-1]
def odd_length_palindromes(words):
    return [word for word in words if is_palindrome(word) and len(word) % 2 == 1]
words_list = ["madam", "racecar", "hello", "level", "world", "noon", "python", "civic"]
result = odd_length_palindromes(words_list)
print("Odd length palindromes in the list are:")
print(result)