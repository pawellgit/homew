
# coding: utf-8

# In[6]:

def mult5(a):
    def inner(a):
        return a * 5
    return inner(a)

a = 6
a = mult5(a)
print(a)



# In[ ]:



