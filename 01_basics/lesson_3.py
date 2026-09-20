print(abs(-5))

print(min(1,3,4,8))
print(max(1,3,4,8))

print(pow(49, 0.5))

print(round(0.5))
print(round(1.5))

print(round(1.5323, 2))

print(max(1 , 2, 3 , abs(-7), -10))
print(max(1 , 2, 3 , abs(min(-17,3,5)), -10))

import math
# Округление в большу сторону
print(math.ceil(5.2))
print(math.ceil(-5.2))
#В меньшую
print(math.floor(5.2))
print(math.floor(-5.2))

print(math.factorial(6))

#отброс дробной части
print(math.trunc(5.2))

print(math.log2(4))
print(math.log10(1000))
print(math.log(2.7))
print(math.log(27 , 3))

print(math.sqrt(256))

print(math.sin(3.14/2))
print(math.cos(0))

print(math.pi)
print(math.e)

# ввод данных (переменные n, k в программе не менять)
n, k = map(int, input().split())

# здесь продолжите программу
Cnk = math.factorial(n)/(math.factorial(k) * math.factorial(n-k))# в этой переменной сохраняйте результат
print(Cnk)