# 2.Wygeneruj listę 20 liczb losowych z przedziału 100 do 200. Parzystych niepodzielnych przez 5.
# import random
# lst = []
# while len(lst) !=20:
#     rnd = random.randint(100,200)
#     if rnd % 5 != 0:
#         lst.append(rnd)
# print(lst)
# 3.Napisz program do którego możemy wprowadzić dowolne zdanie. Niech nasz program wyświetli:
# Ile mamy d,v,b,n,k.
# inp=input()
# d_ile=0
# v_ile=0
# b_ile=0
# n_ile=0
# k_ile=0
# for el in inp:
#     if el =='d':
#         d_ile +=1
#     if el =='v':
#         v_ile +=1
#     if el =='b':
#         b_ile +=1
#     if el =='n':
#         n_ile +=1
#     if el =='k':
#         k_ile +=1

# print(f"d--{d_ile} v--{v_ile} b--{b_ile} n--{n_ile} k--{n_ile}")

# 5.Napisz funkcję która z przyjmuje jako argument powyższą listę i zwróci mi ile jest liczb mniejszych od 0.
# from random import randint
# lista=[randint(-10,10)for el in range(100)]
# print(lista)
# # mniejsze_od_0=0


# # for el in lista:
# #     if el <0:
# #         mniejsze_od_0 +=1
# # print(mniejsze_od_0)

# # 6.Napisz funkcję która z przyjmuje jako argument powyższą listę i zwrócić mi ile jest większych lub równych 0.
# # print(len(lista)-mniejsze_od_0)
# # 7.Napisz funkcję która z przyjmuje jako argument powyższą listę i zwrócić mi sumę wszystkich elementów parzystych.
# xxx=0
# for el in lista:
#     if el %2 == 0:
#         xxx+=el
# print(xxx)
# # 8.Napisz funkcję która z przyjmuje jako argument powyższą listę i zwrócić mi sumę wszystkich elementów nieparzystych .
# xxx=0
# for el in lista:
#     if el %2 != 0:
#         xxx+=el
# print(xxx)
# # 9.Napisz funkcję która przyjmuje jako argument powyższą listę i zwrócić mi sumę wszystkich elementów podzielnych przez 5 i 7.
# xxx=0
# for el in lista:
#     if el %5==0 and el %7 == 0:
#         xxx+=el
# print(xxx)
# # 10.Napisz funkcję która z przyjmuje jako argument powyższą listę poprosi o podanie liczby przez użytkownika i powie ile takich liczb występuje na tej liście.

# 11.Zwrócić lisy w których będę zawrte idexy pod którymi występują największe wartości i najmniejsze wartości.

# 12.Napisz funkcję która wygeneruje listę o n wielkości i “zasięgu” podanego przez użytkownika.
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
