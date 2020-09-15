#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Удивительно, но существует только три числа, которые могут быть записаны в виде суммы четвертых степеней их цифр:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
1 = 1^4 не считается, так как это - не сумма.

Сумма этих чисел равна 1634 + 8208 + 9474 = 19316.

Найдите сумму всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр.'''


# In[ ]:


def isFivePowerDigit(number):
    total = 0
    for counter in str(number):
        total += int(counter) ** 5
    return total == number


# In[ ]:


sum(number for number in range(2, 10 ** 6 + 1) if isFivePowerDigit(number))


# In[ ]:




