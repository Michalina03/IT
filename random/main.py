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
