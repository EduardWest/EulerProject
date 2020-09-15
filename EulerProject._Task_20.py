#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!.'''


# In[ ]:


# Задача 20
from math import factorial


# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'sum(int(i) for i in str(factorial(100)))')


# In[ ]:


# Вычисление фактоиала через рекурсию
def recurcuve_factorial(number):
    if number == 1:
        return 1
    return number * recurcuve_factorial(number - 1)


# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'sum(int(i) for i in str(recurcuve_factorial(100)))')


# In[ ]:


# Вычисление факториала через цикл
def loop_while_factorial(number):
    counter = 2
    var = 1
    while counter <= number:
        var *= counter
        counter += 1
    return var


# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'sum(int(i) for i in str(loop_while_factorial(100)))')


# In[ ]:


def loop_for_factorial(number):
    var = 1
    for counter in range(2, number + 1):
        var *= counter
    return var


# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'sum(int(i) for i in str(loop_for_factorial(100)))')


# In[ ]:




