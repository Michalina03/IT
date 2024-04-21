with open("xxx.txt", "w") as text_file:
    text = "Ala ma kota"
    text_file.write(text)


with open("xxx.txt", "r") as xxx:
    print(xxx)
    xxx_contents = xxx.readline()
    print(xxx_contents)

with open("xxx.txt", "a") as text_file:
    text = "\n" + "Nie, Ula ma kota"
    text_file.write(text)

# -------------------------------------

# Napisz funkcję generującą plik tekstowy zawierający liczby “od kiedy do kiedy co ile -range”


def genrate_text(file_name: str, content: str):
    file_name = file_name + ".txt"
    with open(file_name, "w") as text_file:
        text_file.write(content)


def numbers_range(n: int, m: int, k: int):
    text = ""
    for i in range(n, m, k):
        text += f" {i}"
    return text


text = numbers_range(-10, 100, 2)
genrate_text("numbers", text)


# Napisz funkcję generującą plik tekstowy zawierający liczby ciągu arytmetycznego..


def genrate_text(file_name: str, content: str):
    file_name = file_name + ".txt"
    with open(file_name, "w") as text_file:
        text_file.write(content)


def cig_arytmetyczny(p_el, dr_el, n):
    el = p_el
    co_ile = dr_el - p_el
    text = f"{p_el} "
    for _ in range(n):
        text += f"{el+co_ile} "
        el += co_ile
    return text


text = cig_arytmetyczny(5, 10, 20)
genrate_text("ary", text)


# Napisz funkcję generującą plik tekstowy zawierający liczby ciągu geometrycznego.


def genrate_text(file_name: str, content: str):
    file_name = file_name + ".txt"
    with open(file_name, "w") as text_file:
        text_file.write(content)


def cig_gem(p_el, dr_el, n):
    el = p_el
    co_ile = dr_el / p_el
    text = f"{p_el} "
    for _ in range(n):
        text += f"{el*co_ile} "
        el *= co_ile
    return text


text = cig_gem(3, 9, 10)
genrate_text("geom", text)


# Napisz funkcję generującą plik tekstowy zawierający liczby ciągu fibonacciego.


def genrate_text(file_name: str, content: str):
    file_name = file_name + ".txt"
    with open(file_name, "w") as text_file:
        text_file.write(content)


def fibonacci_sequence(n):
    el_1 = 1
    el_2 = 1
    nex_el = 0
    text = f"{el_1} {el_2}"
    for _ in range(n):
        nex_el = el_1 + el_2
        text += f" {nex_el}"
        el_1 = el_2
        el_2 = nex_el
    return text


text = fibonacci_sequence(10)
genrate_text("fibo", text)


# Napisz funkcję generującą pliki tekstowy zwierjacy tabliczke mnożenia 10 na x10.


def multiplication_tables(n):
    s = ""
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            s += f"{i*k}\t"
        s += "\n"
    return s


def genrate_text(file_name: str, content: str):
    file_name = file_name + ".txt"
    with open(file_name, "w") as text_file:
        text_file.write(content)


multiplication_data = multiplication_tables(10)


genrate_text("multiplication_tables", multiplication_data)


# ---- CZYTANIE PLIKÓW ----------- pamiętaj aby najpierw wygenerować plik,
# ten kod linijka po linijce przeczyta Ci tekst  wygenerowanego pliku tekstowego


def linijka_po_linijce(sciezka_do_pliku):
    try:
        with open(sciezka_do_pliku, "r") as plik:
            for linijka in plik:
                inf = linijka.strip()
                print(inf)
                inf = inf.split("-")
                print(inf)
    except FileNotFoundError:
        print("Ups! Nie mogę znaleźć pliku. Sprawdź ścieżkę.")


linijka_po_linijce("xxx.txt")

# ====== ZADANIE KARTKÓWKOWE ====================
# np. kto zarabia więcej, ile mężczyzn do kobiet proporcje, ile średnio zarabiają kobiety
# -- (ten kod chyba nie działa, aby wyciagną osoby z pliku lepiej użyć tego wyżej) --


def linijka_po_linijce(sciezka_do_pliku):
    k = 0
    zarobki = 0
    try:
        with open(sciezka_do_pliku, "r") as plik:
            for linijka in plik:
                inf = linijka.strip()
                inf = inf.split("-")
                if inf[4] == "Kobieta":
                    k += 1
                    zarobki += float(inf[3])

    except FileNotFoundError:
        print("Ups! Nie mogę znaleźć pliku. Sprawdź ścieżkę.")

    print(zarobki / k)


linijka_po_linijce("xxx.txt")


# -----------KOD GENERUJĄCY TABELKE MNOŻENIA ---------------------
def generate_multiplication_table(n):
    table = ""

    table += "   "
    for i in range(1, n + 1):
        table += f"{i:4}"
    table += "\n"

    for i in range(1, n + 1):
        table += f"{i:2}"
        for j in range(1, n + 1):
            result = i * j
            table += f"{result:4}"
        table += "\n"
    return table


table_size = 10

multiplication_table = generate_multiplication_table(table_size)

file_name = "tabliczka_mnozenia.txt"

try:
    with open(file_name, "w") as file:
        file.write(multiplication_table)
    print("Plik został pomyślnie wygenerowany.")
except Exception as e:
    print("Wystąpił błąd podczas generowania pliku:", str(e))


# =================== HOMWORK ========================
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

# ======= TRÓJKĄT PTOSTOKĄTNY ========


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

# ======= TRÓJKĄT RÓWNORAMIENNY========


def generate3(ilosc):
    tekst = ""
    for i in range(ilosc):
        stars = 2 * i + 1
        spaces = ilosc - i - 1
        tekst += " " * spaces + "*" * stars + "\n"
    return tekst


ilość_gwiazdek3 = 4

trojkat2 = generate3(ilość_gwiazdek3)

file_name = "trojkat.txt"

with open(file_name, "w") as file:
    file.write(trojkat2)
