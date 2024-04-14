# ======= KWADRAT =======
def generate(ilosc):
    tekst = ""
    for i in range(ilosc):
        if i == 0 or i == ilosc - 1:
            tekst += "* " * ilosc + "\n"
        else:
            tekst += "* " + "  " * (ilosc - 2) + "*\n"
    return tekst


ilość_gwiazdek = 10

kwadrat = generate(ilość_gwiazdek)

file_name = "kwadrat.txt"

with open(file_name, "w") as file:
    file.write(kwadrat)

# ======= TRÓJKĄT ========


def generate2(ilosc):
    tekst = ""
    for i in range(1, ilosc + 1):
        tekst += "* " * i + "\n"
    return tekst


ilość_gwiazdek2 = 7

trojkat = generate2(ilość_gwiazdek2)

file_name = "trojkat.txt"

with open(file_name, "w") as file:
    file.write(trojkat)
