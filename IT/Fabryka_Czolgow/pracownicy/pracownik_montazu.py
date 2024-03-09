from IT.Fabryka_Czolgow.pracownicy import Pracownik
# Pracownik Montazu jako komponent
class Pracownik_Montazu:
    def __init__(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
        self.pracownik = Pracownik(imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa)