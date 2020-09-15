#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Перестановки простых чисел
Арифметическая прогрессия: 1487, 4817, 8147, в которой каждый член возрастает на 3330, необычна в двух отношениях:
(1) каждый из трех членов является простым числом, 
(2) все три четырехзначные числа являются перестановками друг друга.

Не существует арифметических прогрессий из трех однозначных, двухзначных и трехзначных простых чисел,
демонстрирующих это свойство. Однако, существует еще одна четырехзначная возрастающая арифметическая прогрессия.

Какое 12-значное число образуется, если объединить три члена этой прогрессии?'''


# In[79]:


# Создаем собственнуб функцию для определения числа на простоту
def isPrime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


# In[80]:


# Генерируем 4-ех значные простые числа
def generate_prime_numbers():
    s = []
    for i in range(10 ** 3, 10 ** 4):
        if isPrime(i):
            s.append(i)
    return s


# In[81]:


def permutations_prime_numbers():
    from itertools import permutations
    s = generate_prime_numbers() # список простых чисел
    for i in s:
        list_primes = []
        perm = permutations(str(i)) # список перестановок 
        for j in perm: # опрелеляем, сколько простых чисел в данной перестановке
            number = int(''.join(map(str, j)))
            if isPrime(number):
                list_primes.append(number) # список простых чисел в данной перестановке
                for k in range(1, 4500): # макс. разница между числами: (10000 - 1000) / 2 = 4500
                    if list_primes[0] + k in list_primes and list_primes[0] + k * 2 in list_primes:
                        result = str(list_primes[0]) + str(list_primes[0] + k) + str(list_primes[0] + k * 2)
                        break
    print(result) # печатаем последний результат
            
    


# In[83]:


permutations_prime_numbers()


# In[ ]:


# Ответ - 296962999629

