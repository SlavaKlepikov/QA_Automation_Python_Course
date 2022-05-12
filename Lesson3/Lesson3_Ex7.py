data1 = {0, 1, 2, 3, 4, 6, 8, 9}
print(data1)
data_len = len(data1)
data2 = set(range(0, data_len+1))
print(data2)
difference_data = data2.difference(data1)
print(difference_data)

