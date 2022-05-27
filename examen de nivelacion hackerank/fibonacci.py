n=1
z=10

def fibonacci(n,z):
    if n <= 0:
        n = 1
    grupo = [n]
    a = n
    i=1
    while i <= z:
        b = n + a
        n = a
        a = b
        i+=1
        grupo.append(b)

    return grupo


for i in fibonacci(n,z):
    print(f' El Numero Fibonacci es: {i}')



