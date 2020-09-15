#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Эйлер опубликовал свою замечательную квадратичную формулу:

n^2+n+41
Оказалось, что согласно данной формуле можно получить 40 простых чисел,
последовательно подставляя значения 0≤n≤39. Однако, при n=40,
40^2+40+41=40(40+1)+41 делится на 41 без остатка, и, очевидно, при n=41,412+41+41 делится на 41 без остатка.

При помощи компьютеров была найдена невероятная формула n^2−79n+1601,
согласно которой можно получить 80 простых чисел для последовательных значений n от 0 до 79.
Произведение коэффициентов −79 и 1601 равно −126479.

Рассмотрим квадратичную формулу вида:

n2+an+b, где |a|<1000 и |b|≤1000

где |n| является модулем (абсолютным значением) n.
К примеру, |11|=11 и |−4|=4
Найдите произведение коэффициентов a и b квадратичного выражения,
согласно которому можно получить максимальное количество простых чисел для последовательных значений n,
начиная со значения n=0.'''


# In[41]:


def isPrime(number):
    if number < 0:
        return False
    if number == 1:
        return False
    if number % 2 == 0:
        return number == 2
    counter = 3
    while counter * counter <= number and number % counter != 0:
        counter += 2
    return counter * counter > number


# In[42]:


prime_list = [number for number in range(1, 1001) if isPrime(number)]
#prime_list


# In[46]:


get_ipython().run_cell_magic('timeit', '', 'total_prime = 0\nmax_first = 0\nmax_second = 0\nfor second_number in prime_list:\n    for first_number in range(-999, 1000, 2):\n        number = 0\n        while isPrime(number * number + first_number * number + second_number): number += 1\n        if number > total_prime:\n            total_prime = number\n            max_first = first_number\n            max_second = second_number\n            #print(number, max_first, max_second)\nprint(max_first * max_second)     ')


# In[47]:


get_ipython().run_cell_magic('timeit', '', 'flag = [0] * 204\nprimes = []\n\ndef ifc(n): return flag[n>>6]&(1<<((n>>1)&31))\n\ndef isc(n): flag[n>>6]|=(1<<((n>>1)&31))\n\ndef sieve():\n    for i in range(3, 114, 2):\n        if ifc(i) == 0:\n            for j in range(i*i, 12996, i<<1): isc(j)\n\ndef store():\n    primes.append(2)\n    for i in range(3, 1000, 2):\n        if ifc(i) == 0: primes.append(i)\n\ndef isprime(n):\n    if n < 2: return 0\n    if n == 2: return 1\n    if n & 1 == 0: return 0\n    if ifc(n) == 0: return 1\n    return 0    \n\ndef main():\n    sieve()\n    store()\n    mmax, ret = 0, 0\n    for b in primes:\n        for a in range(-999, 1000, 2):\n            n = 1\n            while isprime(n*n + a*n + b): n += 1\n            if n > mmax:\n                mmax, ret = n, a * b\n                #print(a, b, n)\n                \n    print(ret)\n\nmain()')

