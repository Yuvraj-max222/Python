#Write a Python Program to find the union of two lists. [do not use set operators]
Ist1 = [90, 34, 12, 40, 77, 100, 56, 78]
Ist2 = [12, 34, 56, 78, 90, 100, 200]
union = Ist1[:]  # Make a copy of Ist1
for item in Ist2:
    if item not in union:
        union.append(item)
print("Union of the two lists:", union)