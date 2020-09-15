#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Пан-цифровые произведения
Каждое n-значное число, которое содержит каждую цифру от 1 до n ровно один раз, 
будем считать пан-цифровым; к примеру, 5-значное число 15234 является пан-цифровым, 
т.к. содержит цифры от 1 до 5.

Произведение 7254 является необычным, поскольку равенство 39 × 186 = 7254, состоящее из множимого, 
множителя и произведения является пан-цифровым, т.е. содержит цифры от 1 до 9.

Найдите сумму всех пан-цифровых произведений, для которых равенство "множимое × множитель = произведение" 
можно записать цифрами от 1 до 9, используя каждую цифру только один раз.

ПОДСКАЗКА: Некоторые произведения можно получить несколькими способами, поэтому убедитесь, что включили их в 
сумму лишь единожды.'''


# In[ ]:


# Напишем функцию для инициализации пан-цифрового числа
def is_pan_digit(number):
    number = str(number)
    return list(map(int, sorted(list(number)))) == list(range(1, len(number) + 1))


# In[ ]:


pan_list = []
for first_digit in range(1, 2000):
    for second_digit in range(1, 2000):
        candidate = str(first_digit) + str(second_digit) + str(first_digit * second_digit)
        if is_pan_digit(candidate) and len(candidate) == 9:
            if (first_digit * second_digit) not in pan_list:
                pan_list.append(first_digit * second_digit)
                print(first_digit, second_digit, first_digit * second_digit)
print(sum(pan_list))


# In[ ]:


# Решение из интернета
def sqrt(x):
    assert x >= 0
    i = 1
    while i * i <= x:
        i *= 2
    y = 0
    while i > 0:
        if (y + i) ** 2 <= x:
            y += i
        i //= 2
    return y

def has_pandigital_product(n):
    for i in range(1, sqrt(n) + 1):
        if n % i == 0:
            temp = str(n) + str(i) + str(n // i)
            if "".join(sorted(temp)) == "123456789":
                return True
    return False

def compute():
    ans = sum(i for i in range(1, 10000) if has_pandigital_product(i))
    return str(ans)
if __name__ == "__main__":
    print(compute())


# In[ ]:




