class Pracownik:
    def __init__(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
        self.ocena_pracy = ocena_pracy
        self.doswiadczenie = doswiadczenie
        self.podgrupa = podgrupa

    def zmien_pensje(self, nowa_pensja):
        self.pensja = nowa_pensja

    def zmien_ocene_pracy(self, nowa_ocena):
        self.ocena_pracy = nowa_ocena

    def zmien_doswiadczenie(self, nowe_doswiadczenie):
        self.doswiadczenie = nowe_doswiadczenie

    def zmien_nazwisko(self, nowe_nazwisko):
       self.nazwisko = nowe_nazwisko
    

    def opis(self):
        print(f"Imię: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Pensja: {self.pensja}")
        print(f"Ocena pracy: {self.ocena_pracy}")
        print(f"Doświadczenie: {self.doswiadczenie}")
        print(f"Podgrupa: {self.podgrupa}")