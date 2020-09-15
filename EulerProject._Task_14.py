#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Задача 14
Самая длинная последовательность Коллатца
Следующая повторяющаяся последовательность определена для множества натуральных чисел:

n → n/2 (n - четное)
n → 3n + 1 (n - нечетное)

Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов.
Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается,
что все сгенерированные таким образом последовательности оканчиваются на 1.

Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?

Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.'''


# In[ ]:


from timeit import timeit


# In[ ]:


#Задача 14 Самая длинная последовательность Коллатца
def collatss():
    collats_sequence = []
    for n in range(13, 1000000):
        collats = []
        collats.append(n)
        j = n
        while j != 1:
            if j % 2 == 0:
                j = int(j / 2)
                collats.append(j)
            else:
                j = 3 * j + 1
                collats.append(j)
        collats_sequence.append((len(collats),n))
    return max(collats_sequence)
timeit(collatss, number = 1)


# In[ ]:


def get_collatz(n, qty):
    if n == 1:
        return qty
    elif n % 2==0:
        return get_collatz(int(n / 2), qty + 1)
    else:
        return get_collatz(3* n + 1, qty + 1)

def collats_internet():
    n = 0
    a = 0
    for i in range(13, 1000000):
        c = get_collatz(i, 1)
        if c > n:
            a, n = i, c
    print(a, n)


# In[ ]:


print(collatss())


# In[ ]:


# Оптимизация своего кода (Задача 14)
def collatss2():
    l, t = 0, 0
    for n in range(837799, 837800):
        if n % 2 == 0:
            continue
        j, x = n, 1
        while j != 1:
            if j % 2 == 0:
                j = j / 2
                x += 1
            else:
                j = 3 * j + 1
                x += 1
        if l < x:
            t, l = n, x
    print((l, t))
timeit(collatss2, number = 1)


# In[ ]:




