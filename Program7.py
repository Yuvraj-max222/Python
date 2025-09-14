#Write a Python program that takes two strings and displays which letter are in the first string but not in the second string.
def unique_letters(str1, str2):
    unique = set(str1) - set(str2)
    return ''.join(sorted(unique))
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print("Letters in the first string but not in the second:", unique_letters(string1, string2))