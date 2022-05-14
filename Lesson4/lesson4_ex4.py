"""
Задача 4

Пользователь вводит число.
Используя list comprehension создать список кубов всех чисел от нуля до числа пользователя (не включая его),
если текущее число минус 1 (число текущей итерации для которого считается куб) кратно 3.
"""
number = int(input("Please input the number, (single value) \n"))
if number == -1:
    number = 3
list_data = [i ** 3 for i in range(number)]
print(list_data)

