#!/usr/bin/env python
# coding: utf-8

# In[7]:


def sumnums(n):
    if n == 1:
        return 1
    return n + sumnums(n - 1)


print(sumnums(3))
print(sumnums(6))
print(sumnums(9))


# In[ ]:




