
# for i in range(10):
#     print(i)
# ______________________________________________________________________________________

# coins = [0,1,1,1,0,0,0,0,0]
# count_zero = 0
# count_one = 0

# for coin in coins:
#     if coin == 0:
#         count_zero += 1
#     else:
#         count_one += 1

# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)

# простейший калькулятор_____________________________________________________________
# a = float(input('введите число: '))
# c = input('оператор: ')
# b = float(input('введите число: '))

# if c == '*':
#     print(a*b)
# elif c == '+':
#     print(a+b)
# elif c == '-':
#     print(a-b)
# elif c == '/':
#     print(a/b)
# else:
#     print('error')


# операции со множетелями_____________________________________________________________
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                                    # c = {1,2,3,5,8}
# u = a.union(b)                                  # u = {1,2,3,5,8,13,21}
# i = a.intersection(b)                           # i = {8,2,5}
# d1 = a.difference(b)                            # d1 = {1,3}
# d2 = b.difference(a)                            # d2 = {13,21}
# q = a.union(b).difference(a.intersection(b))    # q = {1,21,3,13}
# print(d2)

# a = {1,2,3,4,5,6,7}
# b = frozenset(a)
# print(b)

# создать список, состоящий из четных чисел в деапозоне

list_1 = [i for i in range(1, 101)if i % 2 == 0]
print(list_1)