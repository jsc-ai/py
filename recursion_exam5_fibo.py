#!/usr/bin/env python
# coding: utf-8

# In[6]:


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = 14

print('Fibonacci sequence:')
for i in range(number):
    print(fibonacci(i))


# In[ ]:




