def is_even(a):
    """
    Принимает один аргумент
    Возвращает True - если он четный
    Возвращает False - если не четный
    """
    return a % 2 == 0

assert is_even(1) is False
assert is_even(10) is True


def is_odd(a):
    """
    Принимает один аргумент
    Использует функцию is_even из глобальной области видимости
    Внути нельзя использовать if/else
    Возвращает False - если он четный
    Возвращает True - если не четный
    """
    return not is_even(a)

assert is_odd(2) is False
assert is_odd(11) is True


def custom_max(a, b):
    """
    Принимает два аргумента
    Не использовать фнукцию max внути
    Возвращает наибольший из двух элементов
    """
    return a if a > b else b

assert custom_max(1, 10) == max(1, 10)
assert custom_max(100, 10) == max(100, 10)


def multiply(*list_data, base=1):
    """
    Принимает любое кол-во аргументов и один дополнительный необязательный именованный аргумент base
    base по умолчанию равен 1
    Возвращает результат перемножения всех переданных аргументов и необязательного
    """
    for x in list_data:
        base *= x
    return base


example_list = list(range(1, 10))

assert multiply(*example_list) == 362880
assert multiply(*example_list, base=2) == 725760


def reverse(a):
    """
    Принимает один аргумент, строку
    Возвращает развернутую строку
    """
    return a[::-1]


assert reverse("") == ""
assert reverse("QWERqwer123!@#") == "#@!321rewqREWQ"


def upper_count(a):
    """
    Принимает один агрумент, строку
    Возвращает кол-во букв в верхнем регистре
    """
    return len([i for i in a if i.isupper()])

assert upper_count("") == 0
assert upper_count("QWER qwer 123 !@#") == 4


def unique(a):
    """
    Принмает один аргумент, список
    Возвращает список уникальных элементов этого списка отсортированных от меньшего к большему
    """
    return sorted(set(a))

assert unique([2, 2, 1, 5, 5, 2, 7]) == [1, 2, 5, 7]


def is_pangram(a):
    """
    Функция принимает один аргумент, строку
    Возвращает True если в строке хотя бы раз встречается каждая буква английского алфавита
    иначе возвращает False
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in a.lower():
            return False
        return True

assert is_pangram("The five boxing wizards jump quickly") is True
