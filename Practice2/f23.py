def f23(x):
    originalTable = [[f"{date(i[0])}",
                      f"{rounder(i[1])}",
                      f"{done(i[3])}",
                      f"{number(i[5])}"] for i in x]

    table = []
    for i in originalTable:
        if i not in table:
            table.append(i)

    return table


def rounder(x):
    num = round(float(x), 2)
    if num * 100 % 10 == 0:
        return str(num) + '0'
    else:
        return num


def number(x):
    result = ""
    for i in x:
        if i.isdigit():
            result += i
    return result[1:]


def date(x):
    result = ""
    for i in x:
        if not i.isdigit():
            result += '.'
        else:
            result += i
    return result


def done(x):
    if x == 'Не выполнено':
        return 'Нет'
    else:
        return 'Да'


print(f23([
    ['16-03-03', '0.04', None, 'Не выполнено', None, '+7 (735) 828-01-30'],
    ['21-12-03', '0.348', None, 'Выполнено', None, '+7 (057) 454-14-92'],
    ['16-03-03', '0.3', None, 'Не выполнено', None, '+7 (735) 828-01-30'],
    ['01-05-02', '0.486', None, 'Не выполнено', None, '+7 (944) 349-72-47']
]))

# print(number('+7 (735) 828-01-30'))
# print(date('16-03-03'))
