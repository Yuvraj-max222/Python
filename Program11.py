#Python program to Sort a List of Tuples in Increasing Order by the Second element in Each Tuple.
def sort_tuples_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])
tuples_list = [(5, 15, 8), (12, 3, 7), (7, 20, 11, 50)]
sorted_list = sort_tuples_by_second_element(tuples_list)
print("List of Tuples sorted by the second element in each tuple:")
print(sorted_list)
