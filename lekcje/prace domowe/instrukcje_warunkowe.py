# 1. Napisz program, który poprosi użytkownika o wprowadzenie liczby i sprawdzi, czy jest dodatnia, ujemna czy równa zero.
#  Wyświetl odpowiedni komunikat.
# while True:
#     print("Wpisz liczbe aby sprawdzić czy jest dodatnia, ujemna czy równa 0")
#     a = float(input())
#     if a > 0:
#         print("dodatnia")
#     elif a < 0:
#         print("ujemna")
#     elif a == 0:
#         print("równa 0")

# 2. Poproś użytkownika o podanie swojego wieku. Jeśli wiek jest większy lub równy 18,
#  wyświetl komunikat "Jesteś pełnoletni". W przeciwnym razie wyświetl komunikat "Jesteś niepełnoletni".
# print("Podj swój wiek")
# a = float(input())
# if a >= 18:
#     print("Jesteś pełnoletni")
# elif a < 18:
#     print("Jesteś niepełnoletni")

# 3. Poproś użytkownika o wprowadzenie dwóch liczb.
# Sprawdź, która liczba jest większa i wyświetl odpowiedni komunikat.
# while True:
#     print("Wprowadz 2 liczby aby sprawdzić która jest wieksza")
#     a = float(input())
#     b = float(input())
#     if a > b:
#         print("Większa liczba:")
#         print(a)
#     elif a < b:
#         print("Większa liczba:")
#         print(b)

# 5. Poproś użytkownika o podanie oceny szkolnej. Jeśli ocena jest większa lub równa 4,
# wyświetl komunikat "Zaliczone". W przeciwnym razie wyświetl komunikat "Niezaliczone".
# while True:
#     print("Podaj ocene szkolną")
#     a = float(input())
#     if a >= 4:
#         print("Zaliczone")
#     elif a < 4:
#         print("Niezaliczone")

# 6. Napisz program, który poprosi użytkownika o wprowadzenie roku.
# Sprawdź, czy podany rok jest rokiem przestępnym. Wyświetl odpowiedni komunikat
# while True:
#     print("Wpisz rok aby sprawdzić czy jest przystępny")
#     a = int(input())
#     if a % 4 == 0:
#         print("przystępny")
#     else:
#         print("nieprzystępny")

# 7. Poproś użytkownika o podanie liczby. Sprawdź, czy liczba jest parzysta czy nieparzysta.
# Wyświetl odpowiedni komunikat.
# while True:
#     a = int(input())
#     if a % 2 == 0:
#         print("Parzysta")
#     else:
#         print("Nieparzysta")

# 8. Napisz program, który sprawdzi, czy podane trzy liczby mogą być bokami trójkąta. Wyświetl odpowiedni komunikat.
# import math
# a = float(input())
# b = float(input())
# c = float(input())
# if a + b > c and a + c > b and b + c > a:
#     print("to jest trójkt")
#     p = 1 / 2 * (a + b + c)
#     pp = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print(pp)
# else:
#     print("to nie jest trójkt")

# 9. Poproś użytkownika o podanie liczby. Sprawdź, czy liczba jest podzielna przez 3 i 5 jednocześnie.
# Wyświetl odpowiedni komunikat
# while True:
#     a = int(input())
#     if a % 3 == 0 and a % 5 == 0:
#         print("podzielna")
#     else:
#         print("niepodzielna")
