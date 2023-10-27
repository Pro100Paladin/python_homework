# Требуется найти в массиве list_1 самый близкий по величине элемент 
# к заданному числу k и вывести его.


list_1 = [8,7,5,4,3,2,1]
k = 6
cound = 0

for i in list_1:
    if abs(i - k) < abs(cound - k):
        cound = i
print(cound)

# эталон
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)
