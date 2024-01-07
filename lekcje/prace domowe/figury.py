import math

print("Pola figur płaskich:")

print("Pole trójkąta")
a = float(input("bok a = "))
b = float(input("bok b = "))
c = float(input("bok c = "))
p = 0.5 * (a + b + c)
P = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Pole = {P}")

print("Pole kwadratu")
a = float(input("bok a = "))
P = a * a
print(f"Pole = {P}")

print("Pole prostokąta")
a = float(input("bok a = "))
b = float(input("bok b = "))
P = a * b
print(f"Pole = {P}")

print("Pole równoległoboku")
a = float(input("bok a = "))
h = float(input("wysokość h = "))
P = a * h
print(f"Pole = {P}")

print("Pole koła")
r = float(input("promień r = "))
P = math.pi * (r * r)
print(f"Pole = {P}")

print("Pole rombu - sposób 1")
a = float(input("bok a = "))
h = float(input("wysokość h = "))
P = a * h
print(f"Pole = {P}")

print("Pole rombu - sposób 2")
e = float(input("krótsza przekątna e = "))
f = float(input("dłuzsza przekątna f = "))
P = (e * f) / 2
print(f"Pole = {P}")


print("Pola brył:")

print("Pole sześcianu")
d = float(input("krawędź sześcianu = "))


p = 6 * d * d
print(f"Pole = {p}")

print(" ")

print("Pole prostopadłościanu")
e = float(input("krawedź ściany bocznej a = "))
f = float(input("krawedź ściany bocznej b = "))
g = float(input("krawedź podstawy = "))

p = 2 * e * f + 2 * e * g + 2 * f * g
print(f"Pole = {p}")

print(" ")

print("Pole walca")
h = float(input("promień podstawy = "))
i = float(input("wysokość = "))
j = math.pi

p = 2 * j * h * h + 2 * j * i
print(f"Pole = {p}")

print(" ")

print("Pole stożka")
k = float(input("promień podstawy = "))
l = float(input("przeciwprostokątna = "))
m = math.pi

p = m * (k + l)
print(f"Pole = {p}")

print(" ")

print("Pole kuli")
n = float(input("promień podstawy = "))
o = math.pi

p = 4 * o * n * n
print(f"Pole = {p}")
