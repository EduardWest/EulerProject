#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Кубические перестановки
Можно найти перестановки куба 41063625 (3453), чтобы получить еще два куба: 56623104 (3843)
и 66430125 (4053). К слову, 41063625 является наименьшим кубом,
для которого ровно три перестановки также являются кубами

Найдите наименьший куб, для которого ровно пять перестановок также являются кубами.'''


# In[ ]:


# Решение
'''Опытным путем было проверено, что среди чисел до 11-значных такого куба нет, поэтому необходимо генерировать
12-значные кубы, первое число - 4642 ** 3, последнее - 9999 ** 3. Задача: взять число из списка,
пройтись по списку и посмотреть, сколько чисел с совпадающими цифрами, если число нам не подходит, то убрать его из списка'''


# In[ ]:


cubes = [i ** 3 for i in range(4642, 10000)] # Создаем список кубов


# In[ ]:


def cubik_find():
    pos = 0 # Позиция, с какого индекса в списке стартуем
    cub_list = cubes
    for i in (cub_list):
        x = 0 # Переменная, отчевающая за количество чисел
        v = []
        for j in (cub_list[pos:]): # Отбрасываем ненужные нам числа с помощью индексации
            if sorted(list(str(i))) == sorted(list(str(j))):
                x += 1
                v.append(j)
                if x == 5:
                    print(v)
        pos += 1
        if x == 5:
            print(round(i **(1/3)))
            break
    


# In[ ]:


from timeit import timeit


# In[ ]:


timeit(cubik_find, number = 1)


# In[ ]:


# Код работает в среднем за 5-6 секунд, ответ - 5027 ** 3


# In[ ]:


# Решения, которые были найдены на проекте после того, как я уже решил. Замечу, что решения работают в разы быстрее
import collections, itertools

perms = collections.defaultdict(list)
for cube in (b**3 for b in itertools.count()):
    cubes = perms[tuple(sorted(str(cube)))] # list of cubes with the same digits
    cubes.append(cube)
    if len(cubes) == 5:      
        break
#NOTE: I don't check that it has *exactly* five permutations
#      but it worked out for the problem
print(cubes[0]) # 127035954683 0.45 seconds


# In[ ]:


# Еще одно решение
d,f = {},{}

def add_cube(n):
    k = ''.join(sorted(str(x**3)))
    try:
        d[k] += 1
        f[k] = f[k] + [x]
    except:
        d[k] = 1
        f[k] = [x]

for x in range(1, 10000):
    add_cube(x)

print(min([min(f[x[0]]) for x in d.items() if x[1] ==  5]) ** 3)


# In[ ]:




