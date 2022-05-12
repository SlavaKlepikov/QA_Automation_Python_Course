"""
Exercise 6: Add item 7000 after 6000 in the following Python List
Given:
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Expected output:
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""

list_data = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list_data[2][2].insert(2, 7000)
print(list_data)
