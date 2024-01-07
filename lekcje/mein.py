import math

a = float(input())
b = float(input())
c = float(input())
if a + b > c and b + c > a and a + c > b:
    p = 1 / 2 * (a + b + c)
    w = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(w)
else:
    print("nie")
