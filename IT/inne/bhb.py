# class Samochod:
#     def __init__(self, marka, model):
#         self.marka = marka
#         self.model = model


#     def wyswietl_info(self):
#         print(f"Samochód marki {self.marka} model {self.model}")


# # Utworzenie instancji klasy
# moj_samochod = Samochod("Toyota", "Corolla")
# moj_samochod.wyswietl_info()
# # Klasa Zegar: Utwórz klasę Zegar, która będzie reprezentować czas. Klasa powinna mieć atrybuty godzina, minuta i
# sekunda. Dodaj metodę do ustawiania czasu oraz inną do wyświetlania aktualnego czasu.


class Zegar:
    def __init__(self, godzina: int = 0, minuta: int = 0, sekunda: int = 0) -> None:
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda

    def ustaw_czas(self, godzina: int, minuta: int, sekunda: int) -> None:
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda

    def wyswietl_czas(self) -> None:
        return f"{self.godzina:02d}:{self.minuta:02d}:{self.sekunda:02d}"


zegar = Zegar()
zegar.ustaw_czas(10, 25, 30)
print(zegar.wyswietl_czas())
