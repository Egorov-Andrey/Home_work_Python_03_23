# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input())
# one_count = 0
# eagle_count = 0

# for i in range(n):
#     x = int(input()) 
#     if x == 0:
#         one_count += 1
#     else:
#         eagle_count += 1
# if eagle_count > one_count:
#     print(one_count)
# else:
#     print(eagle_count)


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# x = int(input("Введите число x: "))
# y = int(input("Введите число y: "))

# for i in range(x):
#     for j in range(y):
#         if x == i * j and y == i + j:
#             print (i, j)


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input())
# i = 0

# while 2 ** i < n:
#     print (2 ** i)
#     i + 1

