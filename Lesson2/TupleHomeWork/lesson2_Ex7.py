"""
Exercise 7: Modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
Expected output:
tuple1: (11, [222, 33], 44, 55)
"""
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)