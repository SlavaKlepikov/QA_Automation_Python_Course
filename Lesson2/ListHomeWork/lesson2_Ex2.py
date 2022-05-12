"""
Exercise 2: Concatenate two lists index-wise
Given:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
Expected output:
['My', 'name', 'is', 'Kelly']
"""

list_data1 = ["M", "na", "i", "Ke"]
list_data2 = ["y", "me", "s", "lly"]
result = [v + k for v, k in zip(list_data1, list_data2)]
print(result)