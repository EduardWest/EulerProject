#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Проект Эйлера. Задача № 1.

Если выписать все натуральные числа меньше 10, кратные 3 или 5,
то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5.'''


# In[19]:


# Solve 1. Classic
def first_solve():
    total = 0
    for i in range(1, 10 ** 3):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


# In[20]:


# Solve 2
def second_solve():
    return sum([i for i in range(1, 10 ** 3) if any([i % 3 == 0, i % 5 == 0])])


# In[26]:


# Solve 3
def third_solve():
    return sum(i for i in range(1, 10 ** 3) if i % 3 == 0 or i % 5 == 0)


# In[28]:


get_ipython().run_cell_magic('timeit', '', 'first_solve()')


# In[29]:


get_ipython().run_cell_magic('timeit', '', 'second_solve()')


# In[30]:


get_ipython().run_cell_magic('timeit', '', 'third_solve()')


# In[ ]:




