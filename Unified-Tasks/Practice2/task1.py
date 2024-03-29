import sys
import random

economy_data = [
    ["Коллеги,", "В то же время,", "Однако,", "Тем не менее,", "Следовательно,",
     "Соответственно,", "Вместе с тем,", "С другой стороны,"],
    ["парадигма цифровой экономики", "контекст цифровой трансформации",
     "диджитализация бизнес-процессов",
     "прагматичный подход к цифровым платформам",
     "совокупность сквозных технологий", "программа прорывных исследований",
     "ускорение блокчейн-транзакций", "экспоненциальный рост Big Data"],
    ["открывает новые возможности для", "выдвигает новые требования",
     "несёт в себе риски", "расширяет горизонты", "заставляет искать варианты",
     "не оставляет шанса для", "повышает вероятность", "обостряет проблему"],
    ["дальнейшего углубления", "бюджетного финансирования",
     "синергетического эффекта", "компрометации конфиденциальных",
     "универсальной коммодитизации", "несанкционированной кастомизации",
     "нормативного регулирования", "практического применения"],
    ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.",
     "опасных экспериментов.", "государственно-частных партнёрств.",
     "цифровых следов граждан.", "нежелательных последствий.",
     "внезапных открытий."]
]


def conv_to_int(s):
    # Преобразование элементов списка s из строковой в числовую форму.
    # :param s: Исходный список со строковымии числами.
    # :return: Список с числами типа int.
    return [int(i) for i in s]


def distinct_el_num(s):
    # Подсчёт количества различных элементов в последовательности s.
    # :param s: Исходная последовательность.
    # :return: Число уникальных значений.
    return len(set(s))


def reverse_list(s):
    # Обращение последовательности s без использования функций.
    # :param s: Исходная последовательность.
    # :return: Обращённая последовательность.
    return s[::-1]


def find_idx(x, s):
    # Выдача списка индексов, на которых найден элемент x в последовательности s.
    # :param x: Элемент, индексы которого необходимо найти.
    # :param s: Исходная последовательность.
    # :return: Список индексов.
    return [i for i in range(len(s)) if x == s[i]]


def sum_on_even_idx(s):
    # Сложение элементов списка s с чётными индексами.
    # :param s: Исходный список.
    # :return: Сумма элементов, находящиихся на чётных индексах.
    return sum(s[::2])


def find_longest_str(s):
    # Поиск строки максимальной длины в списке строк s.
    # :param s: Исходный список.
    # :return: Самая длинная строка в списке.
    return max(s, key=len)


def shorter():
    # Сократите код до 19 символов без использования функций.
    # return ["much", "code", "wow"][i] # 24 символа
    # :return: Первый элемент списка.
    i = 0
    return "muchcodewow"[:i + 4]  # 19 символов


def generate_groups(group_str):
    # Напишите генерацию всех названий групп в том виде, в котором используется
    # в выпадающем списке на сайте с результатами от робота kispython.
    # :param group_str: Название группы.
    # :return: Преобразованное название группы.
    return "{0}{1}".format(group_str[1], int(group_str[5:7]))


def zip_work():
    # Изучите, как работает функция zip().
    # :return: Список из кортежей, содержащих пары по позициям.
    a = [77, 44, 5]
    b = [3.5, 0.0, -1.0]
    c = ["java", "python", "kotlin"]
    zipped = zip(a, b, c)
    return list(zipped)


def mul_digits(*digits):
    # Разберите роль операции * в создании функций с переменным числом
    # аргументов, а также для распаковки последовательностей.
    # :param digits: Переменное число входных параметров (чисел).
    # :return: Произведение чисел.
    res = 1
    for d in digits:
        res *= d
    return res


def transpose(matrix):
    # Реализуйте с помощью zip() функцию transpose() для транспонирования матрицы.
    # :param matrix: Исходная матриица.
    # :return: Транспонированная матрица.
    return list(list(i) for i in zip(*matrix))


def digital_economy_report_generator():
    # Реализуйте генератор докладов по цифровой экономике.
    # :return: Сгенерированный доклад
    return " ".join(random.choice(i) for i in economy_data)


def my_print(*args, sep=" ", end="\n"):
    # Реализуйте свою версию print(). Постарайтесь использовать максимум
    # возможностей настоящей print(). Для вывода используйте функцию
    # sys.stdout.write().
    # :param args: Аргументы для вывода.
    # :param sep: Разделитель данных для вывода.
    # :param end: Последний символ строки вывода.
    # :return: Ничего не возвращает. Происходит вывод.
    sys.stdout.write(sep.join(str(i) for i in args) + end)


def only_named_args(**args):
    # Реализуйте функцию, которая принимает только именованные аргументы. При
    # передаче позиционного аргумента Питон должен выдать ошибку.
    # :param args: Исходные аргументы
    # :return: Словарь из ключей и значений.
    return args


def generate_array(*dim):
    # Напишите функцию generate_array(dim1, dim2, dim3, ...) для создания
    # многомерного массива с помощью вложенных списков.
    # :param dim: Исходная последовательность аргументов.
    # :return: Многомерный массив.
    return [*dim]


# Задача 1
assert conv_to_int(["2", "13", "1", "0"]) == [2, 13, 1, 0]

# Задача 2
assert distinct_el_num(["python", "hello", "world", "python"]) == 3

# Задача 3
assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

# Задача 4
assert find_idx(4, [0, 4, 1, 4, 4, 2, 4]) == [1, 3, 4, 6]

# Задача 5
assert sum_on_even_idx([2, -1, -7, 4, 2, 8, 9, 1]) == 6

# Задача 6
assert find_longest_str(["java", "python", "c++", "sql"]) == "python"

# Задача про 24 символа
assert shorter() == "much"

# Задача про генерацию названий групп
assert generate_groups("ИКБО-20-19") == "К20"

# Задача, связанная с работой с zip
assert zip_work() == [
    (77, 3.5, "java"),
    (44, 0.0, "python"),
    (5, -1.0, "kotlin")
]

# Задача о переменном числе параметров в функции
assert mul_digits(-1, 3, 5, 7, 9) == -945
# Задача о транспонировании матрицы
assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

# Задача о генерациии докладов по цифровой экономике
for _ in range(5):
    print(digital_economy_report_generator())

# Задача о реализации своего print()
print("print():", "java", [1, 2], None, True, sep="\t->\t", end="%\n")
my_print("my_print():", "java", [1, 2], None, True, sep="\t->\t", end="%\n")

# Задача о только именованных аргументах
assert only_named_args(
    group="ИКБО-20-19",
    university="РТУ МИРЭА",
    year=2021) == {
           "group": "ИКБО-20-19",
           "university": "РТУ МИРЭА",
           "year": 2021
       }

# Задача о генерации многомерного массива
assert generate_array([1, 2], [3, 4], [5, 6]) == [[1, 2], [3, 4], [5, 6]]

print("\nWorks as intended :^)")