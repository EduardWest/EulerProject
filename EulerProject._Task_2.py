#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Каждый следующий элемент ряда Фибоначчи получается при
сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи,
которые не превышают четыре миллиона."""
    


# In[1]:


# Вычисление чисел Фибоначчи рекурсивно
def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)


# In[2]:


#Наивный перебор через рекурсию
sum(fibonacci(i) for i in range(1, 4 * 10) if fibonacci(i) % 2 == 0 and fibonacci(i) < 4 * 10 ** 6)


# In[4]:


#Оптимальный перебор через переназначение переменных
first_fib = 1
second_fib = 0
fib = 0
total = 0
while fib < (4 * 10 ** 6):
    fib = first_fib + second_fib
    second_fib = first_fib
    first_fib = fib
    if fib % 2 == 0:
        total += fib
print(total)


# In[5]:


total = 0
limit = 4 * 10 ** 6
n = 1
while True:
    if fibonacci(n) % 2 == 0:
        total += fibonacci(n)
    if fibonacci(n) >= limit:
        break
    n += 1
print(total)


# In[6]:


# Вычисление числа Фибоначчи через формулу Бине
from math import sqrt
def fib_bine(n):
    phi = (1 + sqrt(5)) / 2
    return round((phi ** n - (-phi) ** -n) / (2 * phi - 1))


# In[7]:


total = 0
limit = 4 * 10 ** 6
n = 1
while True:
    if fib_bine(n) % 2 == 0:
        total += fib_bine(n)
    if fib_bine(n) >= limit:
        break
    n += 1
print(total)


# In[ ]:


# Перебор через рекурсию оказался дольше

