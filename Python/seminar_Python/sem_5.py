# факториал

# x = int(input('введите цифру: '))

# def factorial(x):
#     if x <= 1: #нестоить писать ==
#         return 1
#     return x * factorial(x-1)
# print(factorial(x))


# фибоначи

# y = int(input('введите цифру: '))
# def fibonachi(y):
#     if y in (1, 2):
#         return 1
#     return fibonachi(y-1) + fibonachi(y-2)
# print(fibonachi(y))


# # Задача No35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 
# Output: yes
# 15 минут


z = int(input('введите число: '))
def nat(z, x = 2):
    if z == 2 or x * x > z:
        return True
    elif z % x == 0:
        return False
    return nat(z, x + 1)
print(nat(z))
 
