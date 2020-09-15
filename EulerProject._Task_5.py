#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?'''


# In[ ]:


#Первое решение
number = 2520
while True:
    if all(number % dividers == 0 for dividers in range(11, 21)) == True:
        print(number)
        break
    number += 10
    
    


# In[1]:


#Второе решение
number = 2520
boolean = False
#Остальные делители ушли ввиду свойств умножения
dividers = (11,12,13,14,15,16,17,18,19,20)
while boolean is False:
    for divide in dividers:
        if number % divide == 0:
            boolean = True
        else:
            boolean = False
            number += 10
            break
print(number)


# In[ ]:




