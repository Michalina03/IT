from random import randint


class Uczen:
    liczba_uczniow = 0

    # Zad1
    # Dodaj brakującą metodę i wywołaj ją w konstruktorze. Metoda do liczenia średniej.
    def __init__(self, _imie: int, _nazwisko) -> None:
        self.imie = _imie
        self.nazwisko = _nazwisko
        self.oceny_mat = [2, 3, 4, 5, 6]
        self.srednia_ocen_mat = 0
        self.oceny_ang = [5, 6, 6, 6, 6, 6, 6, 6]
        self.srednia_ocen_ang = 0
        Uczen.liczba_uczniow += 1

    def inf(self):
        print(f"imię {self.imie}")
        print(f"nazwisko {self.nazwisko}")
        print(f"matematyka {self.oceny_mat}")
        print(f"średnia matematyka {self.srednia_ocen_mat}")
        print(f"ang {self.oceny_ang}")
        print(f"średnia ang {self.srednia_ocen_ang}")

    @classmethod
    def ilosc(cls):
        print(cls.liczba_uczniow)

    def zmień_imie(self, imie: int):
        self.imie = imie

    def usun_ocene(self, oceny_mat):
        print(oceny_mat)


u = Uczen("TwojStary", "Pijany")

u.ilosc()
u.zmień_imie("lol")
u.usun_ocene
u.inf()


class Matematyka:

    @staticmethod
    def ile_liczb_parzystych():
        return 0

    @staticmethod
    def czy_pierwsza(liczba: int):
        pass

    @staticmethod
    def ile_liczb_pierwszych():
        return 0


from random import randint

liczby = [i for i in range(100)]
