from IT.Fabryka_Czolgow.pracownicy import Pracownik
class Pracownik_Organizacji_Pracy:
    def __init__(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
       self.pracownik = Pracownik(imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa)