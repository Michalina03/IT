class Człowiek:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def wyswietl_info(self):
        print(
            f"Człowiek o imieniu {self.imie}, nazwisku {self.nazwisko} i wieku {self.wiek}"
        )


czlowiek = Człowiek("Basia", "Kociszewska", 19)
czlowiek.wyswietl_info()


class Czołg:
    def __init__(self, moc, model, marka):
        self.moc = moc
        self.model = model
        self.marka = marka

    def wyswietl_info(self):
        print(f"Czołg o mocy {self.moc}, model {self.model} i marce {self.marka}")


czołg = Czołg("1500 KM", "2A4", "leopard")
czołg.wyswietl_info()


class Laptop:
    def __init__(self, pamięć_RAM, model, marka):
        self.pamięć_RAM = pamięć_RAM
        self.model = model
        self.marka = marka

    def wyswietl_info(self):
        print(
            f"Laptop o pamięci {self.pamięć_RAM}, model {self.model} i marce {self.marka}"
        )


laptop = Laptop("32 GB", "Inspiron 3520-9997 15.6", "Dell")
laptop.wyswietl_info()
