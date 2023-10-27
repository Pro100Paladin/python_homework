# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.


n = int(input("введите число n "))

first = n//100
second = (n//10)%10
third = n%10
res = first + second + third

print(f"{res} ({first} + {second} + {third})")