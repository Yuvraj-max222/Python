#Write a function to generate a random alphanumeric string with 6 characters. There must be one uppercase, one lower case, one digit in the string and all string should start with an uppercase letter.
#Call the function 100 times and check how many times a digit is available at second position.
import random
import string
def generate_string():
    first = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    others = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))
    rest = list(lower + digit + others)
    random.shuffle(rest)
    return first + ''.join(rest)
count = 0
for _ in range(100):
    s = generate_string()
    if s[1].isdigit():
        count += 1
print("Digit at 2nd position:", count)