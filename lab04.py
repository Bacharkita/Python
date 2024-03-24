def fibonacci(number): 
    a, b = 0, 1
    while True: 
        if a > number:
            return
        yield a
        a,b = b, a + b

for x in fibonacci(1000000):
    print(x)
        