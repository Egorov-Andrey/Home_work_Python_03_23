# Задача 2:
# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# 1 вариант
# n = int(input("Введите трехзначное число"))
# print(n)
# c = n % 10
# n = n // 10
# b = n % 10
# a = n // 10
# print(a + b + c)

# 2 вариант

# n = int(input("Введите трехзначное число"))
# n, c = divmod(n, 10)
# a, b = divmod(n, 10)
# print(a, b, c)
# print(a + b + c)

# Задача 4:
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

# total_number_cranes = int(input("Введите общее количество журавлей?"))
# Piter_cranes = total_number_cranes // 6
# Sergey_cranes = total_number_cranes // 6
# Kate_cranes = (total_number_cranes // 6) * 4
# print(total_number_cranes)
# print(Piter_cranes)
# print(Kate_cranes)
# print(Sergey_cranes)

# Задача 6:
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# number_ticket = int(input("Введите шестизначный номер билета: "))
# number_ticket_str = str(number_ticket)
# count_number_ticket = len(number_ticket_str)

# sum_first_three_number = (int(number_ticket_str[0]) + int(number_ticket_str[1]) + int(number_ticket_str[2]))
# sum_second_three_number = (int(number_ticket_str[3]) + int(number_ticket_str[4]) + int(number_ticket_str[5]))

# if sum_first_three_number == sum_second_three_number:
#     print("Happy of ticket")
# else:
#     print("Regular ticket")

# Задача 8: Требуется определить, можно ли от шоколадки
#  размером n × m долек отломить k долек, если разрешается
#  сделать один разлом по прямой между дольками
#  (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input("Введите длину размера шоколадки?: "))
# m = int(input("Введите ширину размера шоколадки?: "))
# k = int(input("Введите количество кусочков шоколадки?: "))

# if (k < m*n) and (k % n == 0 or k % m == 0):
#     print("Yes")
# else:
#     print("No")






