#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Задача 9
Особая тройка Пифагора
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

a2 + b2 = c2
Например, 32 + 42 = 9 + 16 = 25 = 52.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.'''


# In[ ]:


from math import sqrt


# In[ ]:


#Функция для определения тройки Пифагора
def is_pifagor(a, b, c):
    return (a * a) + (b * b) == c * c


# In[ ]:


def thousand_pifagor():
    for a in range(1, 500):
        for b in range(a, 500):
            c = 1000 - a - b
            if is_pifagor(a, b, c):
                    return(a * b * c)
thousand_pifagor()


# In[ ]:


# Другая реализация
def two_pifagor():
    for a in range(1,1000):
        for b in range(a, 1000):
            c = sqrt((a * a + b * b))
            if a + b + c == 1000:
                return(a * b * c)
two_pifagor()


# In[ ]:




