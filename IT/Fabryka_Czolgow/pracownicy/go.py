from Fabryka_Czolgow.pracownicy import Pracownik_IT
from Fabryka_Czolgow.pracownicy import Pracownik_Montazu
from Fabryka_Czolgow.pracownicy import Pracownik_Organizacji_Pracy

prac_montazu = Pracownik_Montazu("Robert", "Kowalski", 3500, 4, 3, "Monter")
prac_montazu.pracownik.zmien_pensje(5000)
prac_IT = Pracownik_IT("Maciej", "Nowak", 4000, 5, 4, "programista")
prac_IT.pracownik.zmien_ocene_pracy(3)
prac_organizacji_pracy = Pracownik_Organizacji_Pracy("Kuba", "Wójcicki", 6000, 3, 2, "mechanik")
prac_organizacji_pracy.pracownik.zmien_nazwisko("Musiał")

print(prac_montazu.pracownik.imie)
print(prac_montazu.pracownik.pensja)
prac_IT.pracownik.opis()
prac_organizacji_pracy.pracownik.opis()