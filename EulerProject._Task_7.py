#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Задача 7
10001-ое простое число
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?'''


# In[ ]:


# Функция для определения простого числа
def isPrime(n):
    if n < 0:
        raise ValueError('Number must be a positive')
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


# In[ ]:


number = 0
var = 1
while number < 10 ** 4 + 1:
    if isPrime(var):
        number += 1
    var += 1
print(var - 1)


# In[ ]:




