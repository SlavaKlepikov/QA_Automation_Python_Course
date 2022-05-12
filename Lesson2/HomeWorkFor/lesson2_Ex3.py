# Exercise 3: Print the following pattern using for loop
n = 5
for i in range(0, n):
    for j in range(0, n-i):
        print(n - j, end=" ")
    print()
