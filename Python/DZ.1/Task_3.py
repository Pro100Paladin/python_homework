# Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета
# с номером n и выводит на экран yes или no.

n = 385916
m = str(n)

if int(m[0])+int(m[1])+int(m[2])==int(m[3])+int(m[4])+int(m[5]):
    print('yes')
else:
    print('no')

ticketLeft = n//1000

one = ticketLeft//100
two = (ticketLeft//10)%10
three = ticketLeft%10

ticketRight = n%1000

four = ticketRight//100
five = (ticketRight//10)%10
six = ticketRight%10


if (one+two+three) == (four+five+six):
    print('Yes')
else:
    print('No')