"""
Exercise 1: Add a list of elements to a given set
Given:
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
Expected output:
Note: Set is unordered.
{'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
"""
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print(sampleSet)


