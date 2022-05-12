"""
Exercise 5: Given a two Python list. Iterate both lists simultaneously
such that list1 should display item in original order and list2 in reverse order
Given
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected output:
10 400
20 300
30 200
40 100
"""
list_data1 = [10, 20, 30, 40]
list_data2 = [100, 200, 300, 400]

for k, v in zip(list_data1, list_data2[::-1]):
    print(k, v)
