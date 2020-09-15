#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Задача 10
Сложение простых чисел
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.'''


# In[ ]:


def isPrime(number):
    if number < 0:
        raise ValueError('Number must be a positive')
    if number == 1:
        return False
    if number % 2 == 0:
        return number == 2
    counter = 3
    while counter * counter <= number and number % counter != 0:
        counter += 2
    return counter * counter > number


# In[ ]:


# Решение через while
total_prime = 0
counter = 1
while counter < 2 * 10 ** 6:
    candidate = isPrime(counter)
    if candidate:
        total_prime += counter
    counter += 1
print(total_prime)


# In[ ]:


# Решение через for
total = 0
for counter in range(1, 2 * 10 ** 6):
    candidate = isPrime(counter)
    if candidate:
        total += counter
print(total)


# In[ ]:


# Решение через генератор
print(sum(candidate for candidate in range(1, 2 * 10 ** 6) if isPrime(candidate)))


# In[ ]:




