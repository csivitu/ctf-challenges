import math
import sys

def fancy(x):
    a = (1/2) * x
    b = (1/2916) * ((27 * x - 155) ** 2)
    c = 4096 / 729
    d = (b - c) ** (1/2)
    e = (a - d - 155/54) ** (1/3)
    f = (a + d - 155/54) ** (1/3)
    g = e + f + 5/3
    return g

def notfancy(x):
    return x**3 - 5*x**2 + 3*x + 10

def mathStuff(x):
    if (x < 3 or x > 100):
        exit()

    y = fancy(notfancy(x))

    if isinstance(y, complex):
        y = float(y.real)

    y = round(y, 0)
    return y

print("Enter a number: ")
sys.stdout.flush()
x = round(float(input()), 0)
if x == mathStuff(x):
    print('Fail')
    sys.stdout.flush()
else:
    print(open('namo.txt').read())
    sys.stdout.flush()
    