#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Двухосновные палиндромы
Десятичное число 585 = 10010010012 (в двоичной системе), является палиндромом по обоим основаниям.

Найдите сумму всех чисел меньше миллиона, являющихся палиндромами по основаниям 10 и 2.

(Пожалуйста, обратите внимание на то, что палиндромы не могут начинаться с нуля ни в одном из оснований)'''


# In[ ]:


# Задача 36 Двухосновные палиндромы
# Напишем функцию для перевода из десятичной системы в двоичную
def double(n):
    number = ''
    next_step = n 
    while next_step != 1:
        if next_step / 2 == int(next_step / 2):
            number += '0'
            next_step = int(next_step / 2)
        else:
            number += '1'
            next_step = int(next_step / 2)
    number = number + '1'
    return int(number[::-1])

# Напишем функцию для определения палиндрома
def palindrom2(n):
    return str(n) == str(n)[::-1]
# Запустим сам алгоритм
sub = 0
for i in range(1, 10 ** 6 + 1):
    if palindrom2(i) and palindrom2(double(i)):
        print(i, double(i))
        sub += i
print(sub)


# In[ ]:




