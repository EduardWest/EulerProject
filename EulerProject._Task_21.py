#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Дружественные числа
Пусть d ( n ) определяет как сумму делителей n (число меньше n , делящие n нацело).
Если d ( a ) = b и d ( b ) = a , где a ≠ b , то a и b называются дружественной парой, 
а каждое из чисел a и b - дружественным числом.

Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, поэтому d (220) = 284.
Делители 284 - 1, 2, 4, 71, 142, поэтому д (284) = 220.

Подсчитайте сумму всех дружественных чисел меньше 10000.'''


# In[ ]:


# Решение
from math import ceil
total = 0
for number in range(2, 10 ** 4):
    first_friend = sum(divide for divide in range(2, ceil(number / 2) + 1)
                       if number % divide == 0) + 1
    second_friend = sum(divide for divide in range(2, ceil(first_friend / 2) + 1)
                        if first_friend % divide == 0) + 1
    if number == second_friend and first_friend != second_friend:
        total += second_friend
print(total)

