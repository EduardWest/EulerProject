#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


matrix =np.array([[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
 [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
 [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
 [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
 [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
 [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
 [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
 [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
 [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
 [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
 [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
 [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
 [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
 [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
 [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
 [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
 [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]])


# In[ ]:


def general_diagonal(n):
    totalresult2 = []
    def first_diagonal(): #[fullh2[t][z-u] for u in range(n-1,-1, 1)]
        fullh = []
        for i in range(n, 21):
            h = []
            for j in range(i):
                h.append(matrix[i-j-1][j])
            fullh.append(h)
        for t in range(len(fullh)):
            for y in range(len(fullh[t]) - n + 1):
                iters = 1
                for z in range(y, y + n):
                    iters *= fullh[t][z]
                totalresult2.append((iters,[fullh[t][z-u] for u in range(n-1,-1, -1)],(t-2,z)))
    first_diagonal()
    def second_diagonal():
        fullh2 = []
        for i in range(19, n-1,-1):
            h2 = []
            for j in range(i):
                h2.append(matrix[19-j][j + 1 - i + 19])
            fullh2.append(h2)
        for t in range(len(fullh2)):
            for y in range(len(fullh2[t]) - n+1):
                iters2 = 1
                for z in range(y, y + n):
                    iters2 *= fullh2[t][z]
                totalresult2.append((iters2,[fullh2[t][z-u] for u in range(n-1,-1, -1)],(t-2,z)))
    second_diagonal()
    def third_diagonal():
        fullh3 = []
        for i in range(n, 21):
            h3 = []
            for j in range(i):
                h3.append(matrix[j][20+j-i])
            fullh3.append(h3)
        for t in range(len(fullh3)):
            for y in range(len(fullh3[t]) - n+1):
                iters3 = 1
                for z in range(y, y + n):
                    iters3 *= fullh3[t][z]
                totalresult2.append((iters3,[fullh3[t][z-u] for u in range(n-1,-1, -1)],(t-2,z)))
    third_diagonal()
    def fourth_diagonal():
        fullh4 = []
        for i in range(19, n-1, -1):
            h4 = []
            for j in range(i):
                h4.append(matrix[19-j][18-j-19+i])
            fullh4.append(h4)
        for t in range(len(fullh4)):
            for y in range(len(fullh4[t]) - n+1):
                iters4 = 1
                for z in range(y, y + n):
                    iters4 *= fullh4[t][z]
                totalresult2.append((iters4,[fullh4[t][z-u] for u in range(n-1,-1, -1)],(t-2,z)))
    fourth_diagonal()
    return totalresult2


# In[ ]:


def fuuh(n):
    totallist3 = []
    for i in range(20):
        for j in range(20 - n + 1):
            iters = 1
            for d in range(j, j + n):
                iters *= matrix[i][d]
            totallist3.append((iters,[matrix[i][d-u] for u in range(n-1,-1, -1)],(i,d)))
    return totallist3


# In[ ]:


def fuuh2(n):
    totallist3 = []
    for i in range(20):
        for j in range(20 - n + 1):
            iters = 1
            for d in range(j, j + n):
                iters *= matrix.transpose()[i][d]
            totallist3.append((iters,[matrix[i][d-u] for u in range(n-1,-1, -1)],(i,d)))
    return totallist3


# In[ ]:


def consecutive_matrix(matrix,n):
    first = general_diagonal(n)
    second = fuuh(n)
    third = fuuh2(n)
    print('Total cases:',len(first + second +third))
    if max(first) > max(second) and max(first) > max(third):
        print("It's a Diagonal")
    else:
        print("It's a Line")
    a = max(max(first),max(second),max(third))
    print('Multiply: ',a[0])
    print('String: ',a[1])
    print('Start point to find: ',a[2])


# In[ ]:


consecutive_matrix(matrix,4)


# In[ ]:




