#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exercise1
#Fibonacci -- > F_n=F_{n-1}+F_{n-2}
def F(n):
    #There are initial values.
    a = 0
    b = 1
    result = [a,b]
    for i in range(n):
        c = a + b
        a = b
        b = c
        result.append(c)
    return (result[n])
n = int(input("Enter number of elements : "))
print("F({})=".format(n),F(n))



           


# In[5]:


#Exercise2
def A(m,n):
    if m == 0:
        return (n+1)
    elif m > 0 and n == 0:
        return(A(m-1,1))
    elif m > 0 and n > 0:
        return (A(m-1 , A(m,n-1)))
m = int(input("Enter number of elements for m : "))
n = int(input("Enter number of elements for n : "))
print("A({})=".format((m,n)),A(m,n))


# In[3]:


#Exercise3
import math
import numpy as np
x = int(input("Enter number of elements: "))
if n < 0:
    print ("Invalid number!!!")
else:
    print("{}!=".format(x),(math.prod(np.arange(1,x+1))))
   

