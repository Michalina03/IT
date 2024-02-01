class Telefon:
    def __init__(
        self,
        pamięć_RAM,
        pamięć_GB,
        wersja_systemu,
        wyświetlacz,
        procesor,
        marka,
        kolor_obudowy,
        aparat,
        model,
    ):
        self._pamięć_RAM = pamięć_RAM
        self._pamięć_GB = pamięć_GB
        self._wersja_systemu = wersja_systemu
        self._wyświetlacz = wyświetlacz
        self._procesor = procesor
        self._marka = marka
        self._kolor_obudowy = kolor_obudowy
        self._aparat = aparat
        self._model = model

    def inf(self):
        print(f"Pamięć RAM:{self._pamięć_RAM}")
        print(f"Pamięć GB:{self._pamięć_GB}")
        print(f"Wersja systemu:{self._wersja_systemu}")
        print(f"Wyświetlacz:{self._wyświetlacz}")
        print(f"Procesor:{self._procesor}")
        print(f"Marka:{self._marka}")
        print(f"Kolor obudowy:{self._kolor_obudowy}")
        print(f"Aparat:{self._aparat}")
        print(f"Model:{self._model}")


Samsung = Telefon(
    "4 GB",
    128,
    "Android 13",
    "6.7, 2400 x 1080px, PLS",
    "Qualcomm Snapdragon 680, Ośmiordzeniowy",
    "Samsung",
    "Biały",
    "Tylny 50 Mpx + 2x2 Mpx, Przedni 13 Mpx",
    "SAMSUNG Galaxy A05s",
)

iPhone = Telefon(
    "16 GB",
    128,
    "Apple A17 Pro",
    " 6,1  2556 x 1179 pikseli OLED",
    "Apple A17 Pro",
    "iPhone",
    "Szary",
    "48 Mpix + 12 Mpix + 12 Mpix",
    " Apple iPhone 15 Pro",
)

Motorola = Telefon(
    "12 GB",
    256,
    "Android 13",
    "6.55",
    "Qualcomm Snapdragon 695",
    "Motorola",
    "Czarny",
    "Tylny 50 Mpx + Przedni 16 Mpx",
)


Samsung.inf()
iPhone.inf()
Motorola.inf()
