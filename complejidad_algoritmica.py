import time
import sys

sys.setrecursionlimit(100000000)

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 6000:
        print('chola')
    if n == 1:
        print('hola')
        return 1
    
    return n * factorial_r(n - 1)

if __name__ == '__main__':
    print(sys.getrecursionlimit())
    n = 10000
    print('hola')
    start = time.time()
    print(f'{start} primer comiezo')
    factorial(n)
    tiempo = time.time() - start
    print(f'{tiempo} final uno')
    print('')
    start = time.time()
    print(f'{start} segundo comiezo')

    factorial_r(n)
    tiempo2 = time.time() - start
    print(f'{tiempo2} final dos')

