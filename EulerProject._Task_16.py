#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Задача 16
Сумма цифр степени
215 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2^1000?'''


# In[ ]:


print(sum(int(i) for i in str(2 ** 1000)))

