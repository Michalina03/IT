from random import randint

lista = []

i = 0
while i < 50:
    if i % 5 == 0:
        lista.append(i)
    i += 1
print(lista)
i = 0
suma = 0
while i < 10:
    suma += lista[i]
    i += 1
print(suma)
