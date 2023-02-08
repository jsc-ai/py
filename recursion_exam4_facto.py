#!/usr/bin/env python
# coding: utf-8

# In[5]:


def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num - 1)


print('{}! is {}'.format(4, factorial(4)))
print('{}! is {}'.format(2, factorial(2)))


# In[ ]:




