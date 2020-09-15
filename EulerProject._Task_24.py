#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Словарные перестановки
Перестановка - это упорядоченная выборка объектов.
К примеру, 3124 является одной из возможных перестановок из цифр 1, 2, 3 и 4. 
Если все перестановки приведены в порядке возрастания или алфавитном порядке, 
то такой порядок будем называть словарным. 
Словарные перестановки из цифр 0, 1 и 2 представлены ниже:

012   021   102   120   201   210

Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?'''


# In[ ]:


from itertools import permutations
perm = list(permutations('0123456789',10))
print(''.join(map(''.join,perm[999999])))


# In[ ]:


# Более традиционный код
def oox():
    mill = 0
    t = False
    for i in range(0, 10):
        for j in range(0, 10):
            if t:
                break
            for a in range(0, 10):
                if t:
                    break
                for b in range(0, 10):
                    if t:
                        break
                    for c in range(0, 10):
                        if t:
                            break
                        for d in range(0, 10):
                            if t:
                                break
                            for e in range(0, 10):
                                if t:
                                    break
                                for f in range(0, 10):
                                    if t:
                                        break
                                    for h in range(0, 10):
                                        if t:
                                            break
                                        for g in range(0, 10):
                                            if len({i,j,a,b,c,d,e,f,h,g}) == len((i,j,a,b,c,d,e,f,h,g)):
                                                mill += 1
                                                print(''.join(map(str,[i,j,a,b,c,d,e,f,h,g])), mill)
                                                if mill == 10 ** 6:
                                                    t = True
                                                    return ''.join(map(str,[i,j,a,b,c,d,e,f,h,g])), mill
        if t:
            break

    print(''.join(map(str,[i,j,a,b,c,d,e,f,h,g])))
                                            
                                            
                                        


# In[ ]:


from timeit import timeit
timeit(oox, number = 1)


# In[ ]:


# 2783915460 - ответ

