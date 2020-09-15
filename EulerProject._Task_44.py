#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Условие
'''Пятиугольные числа вычисляются по формуле: Pn=n(3n−1)/2.
Первые десять пятиугольных чисел:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

Можно убедиться в том, что P4 + P7 = 22 + 70 = 92 = P8.
Однако, их разность, 70 − 22 = 48, не является пятиугольным числом.

Найдите пару пятиугольных чисел Pj и Pk,
для которых сумма и разность являются пятиугольными числами и значение D = |Pk − Pj| минимально,
и дайте значение D в качестве ответа.'''


# In[1]:


# Интересно посмотреть на номера чисел, а не на их разность, разность между ними вычисляется элементарно
# 1. Создадим функцию на проверку треугольного числа
def five_friag(x): # Будем проверять на целостность n
    if x < 0:
        return False
    if (1 + (1 + 24 * x) ** 0.5) / 6 == int((1 + (1 + 24 * x) ** 0.5) / 6): # Если выразить из формулы в явном виде n 
        return True
    return False
# Далее через цикл прогоним все наши числа и будет проверять соотвествие


# In[22]:


# Однострочное решение, через List-Comprehansion
def first_task_44():
     print([(int(i * (3 * i - 1) / 2), int(j * (3 * j - 1) / 2), i, j) for i in range(1, 10 ** 5 + 1) for j in range(i, 10 ** 5 + 1) if five_friag(int(j * (3 * j - 1) / 2) + int(i * (3 * i - 1) / 2)) and five_friag(int(j * (3 * j- 1) / 2) - int(i * (3 * i - 1) / 2))])


# In[77]:


# Более традиционное решение
def second_task_44():
    a = False
    for i in range(1, 10 ** 4 + 1):
        for j in range(i, 10 ** 4 + 1):
            if five_friag(int(j * (3 * j - 1) / 2) + int(i * (3 * i - 1) / 2))  and five_friag(int(j * (3 * j- 1) / 2) - int(i * (3 * i - 1) / 2)):
                print('Первое число:', str(int(i * (3 * i - 1) / 2)) + ',', 'его номер:', i)
                print('Второе число:', str(int(j * (3 * j - 1) / 2)) + ',', 'его номер:', j)
                a = True
                break
        if a:
            break
second_task_44()


# In[78]:


# Более 'питоновское' решение
def third_task_44():
    def unique_pairs(n):
        for i in range(1, n):
            for j in range(i, n):
                yield i, j


    for i, j in unique_pairs(10 ** 4 + 1):
        if five_friag(int(j * (3 * j - 1) / 2) + int(i * (3 * i - 1) / 2))  and five_friag(int(j * (3 * j- 1) / 2) - int(i * (3 * i - 1) / 2)):
            print('Первое число:', str(int(i * (3 * i - 1) / 2)) + ',', 'его номер:', i)
            print('Второе число:', str(int(j * (3 * j - 1) / 2)) + ',', 'его номер:', j)
            break
third_task_44()


# In[7]:


from timeit import timeit


# In[18]:


timeit(second_task_44, number = 1)


# In[20]:


timeit(third_task_44, number = 1)


# In[16]:


timeit(first_task_44, number = 1)


# In[ ]:


# Ответ на задачу:
# Первое число - 1560090, его номер - 1020, второе - 7042750, его номер - 2167.
# Второй алгоритм самый быстрый, справляется в среднем за 20 секунд

