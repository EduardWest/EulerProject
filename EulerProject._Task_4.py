#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Проект Эйлера. Задача 4
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.'''


# In[9]:


#Проверка числа на палиндром
def isPalindrome(number: int) -> bool:
    return list(str(number)) == list(str(number))[::-1]


# In[15]:


# Решение через цикл for
list_Pal = []
for i in range(999, 101, -1):
    for j in range(999, 101, -1):
        if isPalindrome(i * j):
            list_Pal.append(i * j)
print(max(list_Pal))      


# In[14]:


#Решение через генератор списков
max(i * j for i in range(999, 101, -1) for j in range(999, 101, -1) if isPalindrome(i * j))


# In[20]:


# Решение через цикл while
def check_Palindrom():
    h = []
    a = 999
    b = 999
    while a >= 100:
        b = 999
        while b >= 100:
            if isPalindrome(a * b) == False:
                b -= 1
            else:
                h.append(a * b)
                b -= 1
        a -= 1
    return max(h)
print(check_Palindrom())


# In[ ]:




