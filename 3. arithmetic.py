
# coding: utf-8

# In[48]:

def arithmetic(a, b, x):
    if x == '*':
        res = a * b
        print(res)
        return(res)
    elif x == '/':
        res = a / b
        print(res)
        return(res)
    elif x == '+':
        res = a + b
        print(res)
        return(res)
    elif x == '-':
        res = a - b
        print(res)
        return(res)
    else: 
        print('неизвестная операция')

print('введите первое число')        
a = int(input())
print('введите второе число')
b = int(input())
print('введите знак операции')
x = (input())

(arithmetic(a, b, x))
        

        


# In[ ]:



