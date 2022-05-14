"""
Задача 1

Пользователь вводит одно число - любое значение которое гарантированное можно перевести в int.
Определить его кратность 2, 3, 5, 7 или самому себе.
Вывести строку f"multiple of {val}" где val - значение кратности.
Если число кратно нескольким значениям - выводить только наименьшее.
Не используйте циклы в этой задаче.
Используйте конструкцию if/elif/.../elif/else для того что бы проверить каждый из вариантов кратности.
"""
number = int(input("Please input the number, (single value) \n"))
if number % 2 == 0:
    print(f"multiple of {2}")
elif number % 3 == 0:
    print(f"multiple of {3}")
elif number % 5 == 0:
    print(f"multiple of {5}")
elif number % 7 == 0:
    print(f"multiple of {7}")
else:
    print(f"multiple of {number}")
