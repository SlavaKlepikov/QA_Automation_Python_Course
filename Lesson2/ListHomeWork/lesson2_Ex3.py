"""
Exercise 3: Given a Python list of numbers. Turn every item of a list into its square

Given:
aList = [1, 2, 3, 4, 5, 6, 7]
Expected output:
[1, 4, 9, 16, 25, 36, 49]
"""

list_data = [1, 2, 3, 4, 5, 6, 7]
square_list = [i ** 2 for i in list_data]
print(square_list)
