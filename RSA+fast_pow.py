from math import gcd
def fast_pow(x, y, n):
    if y == 0:
        return 1
    if y == -1:
        return 1. / x
    p = fast_pow(x, y // 2, n)
    p = (p * p)% n
    if y % 2:
        p = (p * x) % n
    return p
#Создание открытого и закрытого ключа
p = 11
q = 13
n = p * q
f = (p-1) * (q-1)
e = 6
while (gcd(e, f) != 1) and (e < f): #е должно быть взаимно простым с f, а также меньше f
    e += 1
d = 0
while (d * e) % f != 1: #d мультипликативно обратно к числу e по модулю f
    d += 1
m = 25

#Шифрование
c = fast_pow(m,e,n) 
#m**e % n

#Расшифрование
m_new = c**d % n

print('Открытый ключ:', e, n)
print('Закрытый ключ:', d, n)
print('Зашифрованное сообщение:', c)
print('Расшифрованное сообщение:', m_new)
