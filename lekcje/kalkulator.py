print("Hej !")
a = float(input("a:"))
b = float(input("b:"))
c = input("Wybierz opcje: a- dodawanie, b- odejmowanie, c- mnożenie, d- dzielenie")

if c == "a":
    print(f"{a}+{b}={a+b}")
elif c == "b":
    print(f"{a}-{b}={a-b}")
elif c == "c":
    print(f"{a}*{b}={a*b}")
elif c == "d":
    print(f"{a}/{b}={a/b}")
else:
    print("Nie ma takiej opcji")
