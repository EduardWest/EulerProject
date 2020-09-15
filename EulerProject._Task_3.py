#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Проект Эйлера. Задача 3
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?'''


# In[ ]:


from math import sqrt, ceil

# Решение через оптималные перебор простого числа
def isPrime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def maxPrime(n):
    for i in range(ceil(sqrt(n)), 2, -1):
        if n % i == 0 and isPrime(i):
            return i
number = 600851475143
print(maxPrime(number))


# In[ ]:


# Другой способ решения
max((i for i in range(ceil(sqrt(number)), 2, -1) if number % i == 0 and isPrime(i)))


# In[ ]:




