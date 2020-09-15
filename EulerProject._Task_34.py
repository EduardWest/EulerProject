#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.

Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.

Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.'''


# In[ ]:


from math import factorial

super_sum = 0
for number in range(111, 99999):
    candidate = 0
    for digit in str(number):
        candidate += factorial(int(digit))
    if candidate == number:
        super_sum += number
print(super_sum)

