def fib(a):
    b = 0
    c = 1
    l1 = []
    while c <= a:
        l1.append(b)
        l1.append(c)
        b += c
        c += b
    return(l1)

print('Введите число')
a = int(input())
print(fib(a))