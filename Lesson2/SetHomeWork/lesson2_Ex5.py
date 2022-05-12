"""
Exercise 5: Remove items 10, 20, 30 from the following set at once
set1 = {10, 20, 30, 40, 50}
Expected output:
{40, 50}

Note. Try to use “difference_update” method of “set” object.
"""
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)


