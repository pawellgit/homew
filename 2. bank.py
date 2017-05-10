
# coding: utf-8

# In[35]:

def bank(n, m, years):
    while years > 0:
        n = n * 1.1
        n = n + m
        years = years - 1 
    return(n)
                  

print('введите начальный вклад')
n = int(input())
print('введите сумму ежегодных пополнений')
m = int(input())
print('введите количество лет')
years = int(input())

print('итоговая сумма накоплений:', bank(n, m, years))

        


# In[ ]:



