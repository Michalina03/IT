# Napisz skrypt co wygeneruje 20 liczb pierwszych w pliku tekstowym ppp.txt.
def generator_lp(n):
    lst = []
    liczba = 2
    while len(lst) < n:
        if all(liczba % i != 0 for i in range(2, int(liczba**0.5) + 1)):
            lst.append(liczba)
        liczba += 1
    return lst


lista = generator_lp(20)

with open("ppp.txt", "w") as file:
    file.write("\n".join(map(str, lista)))


# Napisz skrypt co wygeneruje 20 liczb ciągu fibonacciego w pliku tekstowym fff.txt
def generator_f(n):
    f = [0, 1]
    while len(f) < n:
        f.append(f[-1] + f[-2])
    return f


list = generator_f(20)

with open("fff.txt", "w") as file:
    file.write("\n".join(map(str, list)))


# 1 Napisz skrypt co przepisze liczby pierwsze do zzz.txt jeśli znajdują się one w obu plikach  ppp.txt / fff.txt
def read(filename):
    with open(filename, "r") as file:
        numbers = set(int(line.strip()) for line in file)
    return numbers


def write(numbers, filename):
    with open(filename, "w") as file:
        for number in sorted(numbers):
            file.write(f"{number}\n")


ppp_numbers = read("ppp.txt")
fff_numbers = read("fff.txt")

numbers = ppp_numbers.intersection(fff_numbers)

write(numbers, "zzz.txt")


# 1 Napisz skrypt co zmieni wszystkie z pliku zzz.txt na liczby binarne
def na_binary(input_file, output_file):
    with open(input_file, "r") as file:
        binary_numbers = [bin(int(line.strip()))[2:] for line in file]

    with open(output_file, "w") as file:
        file.write("\n".join(binary_numbers))


na_binary("zzz.txt", "zzz_bin.txt")


# 2Napisz skrypt co  przepisze  liczby z pliku fff.txt + rozłoży liczby na czynniki pierwsze i zapisze je z pliku ccc.txt.
def czynniki_pierwsze(n):
    factors = []
    d = 2  # dzielnik
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    return factors


def zapis_do_pliku(input_file, output_file):
    with open(input_file, "r") as file:
        numbers = [int(line.strip()) for line in file]

    result = []  # Lista do przechowywania krotek (liczba, czynniki_pierwsze)
    for number in numbers:
        factors = czynniki_pierwsze(number)  # Poprawiono wywołanie funkcji
        result.append((number, factors))

    with open(output_file, "w") as file:
        for number, factors in result:  # Poprawiono zmienną zapis_do_pliku na result
            file.write(f"{number} {' '.join(map(str, factors))}\n")


zapis_do_pliku("fff.txt", "ccc.txt")


# 2Napisz skrypt co powie ile występuje liczb pierwszych (wszystkie liczby pierwsze) w pliku zzz.txt.
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def count_prime_numbers(filename):
    with open(filename, "r") as file:
        return sum(1 for line in file if is_prime(int(line.split()[0])))


ccc_prime_count = count_prime_numbers("ccc.txt")
print(f"Liczba liczb pierwszych w pliku 'ccc.txt': {ccc_prime_count}")
