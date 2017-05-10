
# coding: utf-8

# In[ ]:

def square(a, b):
    p = (a + b) * 2
    s = a * b
    d = (a**2 + b **2) ** 0.5
    print('площадь =', s)
    print('периметр =', p)
    print('диагональ =', d)
    
print('введите сторону А')
a = int(input())
print('введите сторону В')
b = int(input())

square(a, b)


# In[ ]:



