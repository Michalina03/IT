# oceny=[1,4,6,3]
# i=0
# suma=0
# while i<len(oceny):
#     suma+=1/oceny[i]
#     i+=1
# print(suma/len(oceny))

# 1.Stwórz listę zawierającą x liczb
# wprowadzonych przez użytkownika od (1 do 200)
# liczby=[]
# while True:
#     inp=input()
#     if inp =="stop":
#         break
#     inp = float(inp)
#     if inp<=200 and inp>=1:
#         liczby.append(inp)
#     else:
#         print("liczba nie spełnia zaakresu")
# print(liczby)


# 2.Na podstawie otrzymanej listy stwórz nową listę gdzie znajdują się:
#  Liczby parzyste większe od 50 ale mniejsze od  70.Wyświetl je
# w konsoli z informacją ile zawierają elementów.
# nowa_liczba=[]
# i=0
# while i<len(liczby):
#     if inp%2==0 and inp<=70 and inp>=50:
#         liczby.append(inp)
#         i+=1
   

# 3.Napisz program co wprowadzi x ocen (1 do 6) a następnie obliczy nam średnią  arytmetyczną.
# Jeśli ktoś wprowadzi liczby inne niż 1 i 6 niech program wyświetli m….
# podałeś złe liczby Nobie!
# oceny=[]
# i=0
# while True:
#     inp = input()
#     if inp=="stop":
#         break
#     if float(inp) <1 or float(inp) >6:
#         print("podałeś złe liczby Nobie!")
#     oceny.append(float(inp))

# print(oceny)
# print(sum(oceny)/len(oceny))
