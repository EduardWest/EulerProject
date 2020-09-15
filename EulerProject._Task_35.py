#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Круговые простые числа
Число 197 называется круговым простым числом, потому что все перестановки его цифр
с конца в начало являются простыми числами: 197, 719 и 971.

Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.

Сколько существует круговых простых чисел меньше миллиона?'''


# In[5]:


def isPrime(n):
    n = int(n)
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


# In[15]:


def round_prime(n):
    if not isPrime(n):
        return False
    n = str(n)
    x = 0
    a = n
    for i in range(1, len(n)):
        a = a[-1] + a[:-1]
        if isPrime(a):
            x += 1
    if x == len(a) - 1:
        return True
    return False


# In[45]:


def time1():
    x = 0
    for i in range(2, 10 ** 6):
        if round_prime(i):
            x += 1
    print(x)
        


# In[46]:


def time2():
    print(len([i for i in range(2, 10 ** 6) if round_prime(i)]))


# In[47]:


from timeit import timeit


# In[51]:


timeit(time1, number = 1)


# In[52]:


timeit(time2, number = 1)


# In[ ]:


# - Ответ на задачу: 55 круговых чисел

