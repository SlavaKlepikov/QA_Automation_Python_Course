list_data = [2, 6, 5, 4, 8, 9, 7, 5, 1, 2, 4, 3]
start_slice = int(input("Enter position to start the slicing\n"))
stop_slice = int(input("Enter position to end the slicing\n"))
result_slice = list_data[start_slice:stop_slice:]
print(result_slice)