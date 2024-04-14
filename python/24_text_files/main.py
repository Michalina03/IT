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
