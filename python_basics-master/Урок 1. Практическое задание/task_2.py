"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
my_lst = input("1 2 3 4"). split(' ')
i, j = 0, 1
while len(my_lst) > j:
    my_lst[i], my_lst[j] = my_lst [j], my_lst[i]
    i += 2
    j += 2
    print('2 1 3', *my_lst)