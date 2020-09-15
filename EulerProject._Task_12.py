#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Задача 12
Треугольное число с большим количеством делителей
Последовательность треугольных чисел образуется путем сложения натуральных чисел.
К примеру, 7-ое треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Первые десять треугольных чисел:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Перечислим делители первых семи треугольных чисел:

 1: 1
 3: 1, 3
 6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28
Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.

Каково первое треугольное число, у которого более пятисот делителей?'''


# In[ ]:


# Задача 12 Треугольное число с большим количеством делителей
from math import ceil, sqrt
def count_dividers(number):
    count = 2
    for counter in range(2, ceil(sqrt(number))):
        if number % counter == 0:
            count += 2
    if ceil(sqrt(number)) * ceil(sqrt(number)) == number:
        count -= 1 
    return count


# In[ ]:


number = 0
iterator = 1
while True:
    number = number + iterator
    if count_dividers(number) >= 500:
        break
    iterator += 1
print(number)

