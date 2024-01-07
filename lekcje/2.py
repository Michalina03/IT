import math

a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    print("to jest trójkt")
    p = 1 / 2 * (a + b + c)
    pp = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(pp)
    if (
        a**2 + b**2 == c**2
        or a**2 + c**2 == b**2
        or b**2 + c**2 == a**2
    ):
        print("prostoktny")
else:
    print("to nie jest trójkt")
