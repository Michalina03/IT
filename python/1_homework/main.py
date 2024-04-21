def binarne_na_naturalne(liczba):
    liczba = list(liczba)
    int_num = []
    for index, value in enumerate(reversed(liczba)):
        if value == "1":
            int_num.append(2**index)
    return sum(int_num)


def naturalne_na_binarne(liczba):
    my_list_bin = []
    while liczba > 0:
        remainder = liczba % 2
        my_list_bin.append(remainder)
        liczba = liczba // 2
    my_list_bin.reverse()
    b = ""
    for el in my_list_bin:
        b += str(el)
    return b


from random import randint


def numbers(n):
    with open("numbers.txt", "w") as text_file:
        for i in range(n + 1):
            liczba = randint(1, 100000)
            if i == n:
                text_file.write(f"{liczba}")
            else:
                text_file.write(f"{liczba}-")


numbers(10000)


def zamiana_na_liste_pliku_textowego(sciezka_do_pliku):
    lst = []
    with open(sciezka_do_pliku, "r") as plik:
        for linijka in plik:
            inf = linijka.strip()
            inf = inf.split("-")
            for el in inf:
                lst.append(int(el))
    return lst


lst = zamiana_na_liste_pliku_textowego("numbers.txt")

# Tworzenie pliku my_bin z reprezentacją binarną liczb z pliku numbers.txt
with open("my_bin.txt", "w") as my_bin_file:
    for i, number in enumerate(lst):
        if i == len(lst) - 1:
            my_bin_file.write(naturalne_na_binarne(number))
        else:
            my_bin_file.write(f"{naturalne_na_binarne(number)}-")

# Tworzenie pliku my_int z liczbami całkowitymi z pliku my_bin.txt
with open("my_bin.txt", "r") as my_bin_file:
    with open("my_int.txt", "w") as my_int_file:
        for line in my_bin_file:
            numbers_str = line.strip().split("-")
            for i, num_str in enumerate(numbers_str):
                num_int = binarne_na_naturalne(num_str)
                my_int_file.write(f"{num_int}")
                if i != len(numbers_str) - 1:
                    my_int_file.write("-")
