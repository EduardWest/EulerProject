#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Целые прямоугольные треугольники
Если p - периметр прямоугольного треугольника
с целочисленными
длинами сторон { a , b , c },
то существует ровно три решения
для p = 120: {20,48,52}, {24,45,51}, {30,40,50}

Какое значение p ≤ 1000 дает лучшее число решений?'''


# In[42]:


# Функция для определения треугольника через теорему Пифагора
def is_triangular(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if c ** 2 == a ** 2 + b ** 2:
        return True
    return False


# In[43]:


# Функция для определения количества треугольников для заданного p
def generate_triangular(p):
    x = 0
    for i in range(1, p):
        for j in range(1, i):
            k = p - i - j
            if is_triangular(i, j, k):
                x += 1
            if i > k:
                break
        
    return x
    


# In[45]:


max_triangular = 0
for i in range(1, 10 ** 3 + 1):
    if generate_triangular(i) > max_triangular:
        max_triangular = generate_triangular(i)
        print(max_triangular, i)  


# In[ ]:


# Ответ - p = 840. 8 различных треугольников

