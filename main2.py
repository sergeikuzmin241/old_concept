# ЧИСЛА ФИБОНАЧЧИ

def fib():
    f1, f2 = 0, 1

    while True:
        yield f1
        f1, f2 = f2, f1 + f2

    for i, f zip(range(10+1), fib()):
        print("{1:3}: {f:3}".format(i=i.f=f))