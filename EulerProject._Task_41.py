#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Пан-цифровое простое число
Будем считать n-значное число пан-цифровым, если каждая из цифр от 1 до nиспользуется в нем ровно один раз. 
К примеру, 2143 является 4-значным пан-цифровым числом, а также простым числом.

Какое существует наибольшее n-значное пан-цифровое простое число?'''


# In[1]:


# Решение
# 1) Создадим функцию для идентификации протсого числа
def isPrime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


# In[5]:


# Через permutations будем генерировать пан-цифровые числа и проверять каждое из них на простоту
from itertools import permutations
for digit in range(10, 0, -1):
    break_var = False
    perm = permutations([str(k) for k in range(1, digit)])
    for number in reversed(sorted(perm)):
        number = int(''.join(map(''.join, number)))
        if isPrime(number):
            print(number)
            break_var = True
            break
    if break_var:
        break


# In[24]:


# Как можно увидеть - самое большое число - 7652413 

