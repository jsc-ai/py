#!/usr/bin/env python
# coding: utf-8

# In[8]:


def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


reverseme = 'Star'
print(reverse(reverseme))

reverseme = 'Sun'
print(reverse(reverseme))

reverseme = 'Moon'
print(reverse(reverseme))


# In[ ]:




