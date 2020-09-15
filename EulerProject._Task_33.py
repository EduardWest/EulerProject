#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Дроби, сократимые по цифрам
Дробь 49/98 является любопытной, поскольку неопытный математик, 
пытаясь сократить ее, будет ошибочно полагать, что 49/98 = 4/8, являющееся истиной, 
получено вычеркиванием девяток.

Дроби вида 30/50 = 3/5 будем считать тривиальными примерами.

Существует ровно 4 нетривиальных примера дробей подобного типа, 
которые меньше единицы и содержат двухзначные числа как в числителе, так и в знаменателе.

Пусть произведение этих четырех дробей дано в виде несократимой дроби 
(числитель и знаменатель дроби не имеют общих сомножителей). Найдите знаменатель этой дроби.'''


# In[ ]:


# Создадим функцию на проверку дроби на 'тривиальность'
def is_trivial(i, j):
    if str(i)[1] == '0' or str(j)[1] == '0' or str(i)[0] == str(i)[1] or str(j)[0] == str(j)[1]:
        return True
    return False


# In[ ]:


# Через цикл добавил в список все числители и знаменатели
a, b = [], [] 
for i in range(11, 100):
    for j in range(i + 1, 100):
        if not is_trivial(i, j): # если дробь 'нетривиальна'
            # вычеркиваем первую цифру из числителя и вторую из знаменателя или наоборот
            if (int(str(i)[0]) / int(str(j)[1]) == i / j) or (int(str(i)[1]) / int(str(j)[0]) == i / j):
                # вычеркиваемые цифры должны быть одинаковыми
                if int(str(i)[0]) == int(str(j)[1]) or int(str(j)[0]) == int(str(i)[1]):
                    a.append(i)
                    b.append(j)
print(a)
print(b)


# In[ ]:


# Умножим все числа и числителе и в знаменателе
import numpy as np
numerator, denominator  = np.prod(a), np.prod(b)


# In[ ]:


# Сократим дробь, используя алгоритм Евклида
def evklid_algrorithm(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    while True:
        b1 = a % b
        a1 = b
        b = b1
        a = a1
        if a1 % b1 == 0:
            return b
        
        
    


# In[ ]:


evklid_algrorithm(147, 21)


# In[ ]:


1071 % 462


# In[ ]:


# Или алгоритм Евклида через рукурсию
def evklid_recursion(a, b):
    if a % b == 0:
        return b
    return evklid_recursion(b, a % b)
    


# In[ ]:


answer = denominator // evklid_algrorithm(denominator, numerator)


# In[ ]:


answer


# In[ ]:


# Решение, которое было найдено в интернете. Здесь используется встроенная функция для нахождения НОД 'fractions.gcd'
import fractions

def compute():
    numer = 1
    denom = 1
    for d in range(10, 100):
        for n in range(10, d):
            # вычленение каждого числа из числителя и знаменателя
            n0 = n % 10
            n1 = n // 10
            d0 = d % 10
            d1 = d // 10
            # здесь автор использует правило пропорции для дроби
            if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
                numer *= n
                denom *= d
    return str(denom // fractions.gcd(numer, denom))

if __name__ == "__main__":
    print(compute())

