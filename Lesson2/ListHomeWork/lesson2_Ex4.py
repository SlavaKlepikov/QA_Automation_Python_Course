"""
Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
"""
list_data_1 = ["Hello ", "take "]
list_data_2 = ["Dear", "Sir"]
result = [x + y for x in list_data_1 for y in list_data_2]
print(result)