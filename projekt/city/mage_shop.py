from city.basic_shop import BasicShop
from characters.elemental_magic_book import elemental_magic_book


class MageShop(BasicShop):

    def __init__(self) -> None:
        super().__init__()
        self.add_mana = 100

    def choose_modification(self, character):
        while True:
            try:
                print(f"a \t Add health ? {self.add_health}")
                print(f"b \t Add mana ? {self.add_mana}")
                print(f"c \t Add spell")
                print(f"e \t Quit the shop")
                inp = input().lower()
                if inp == "a" and character._gold > 100:
                    character._gold -= 100
                    character._max_hp += self.add_health

                elif inp == "b" and character._gold > 100:
                    character._gold -= 100
                    character._max_mana += self.add_mana
                elif inp == "c":
                    character._spell_book.unlock_spels(character)
                elif inp == "e":
                    print("Quit the shop")
                    break
                else:
                    print("Not enought gold")
            except Exception as e:
                print(f"An error occurred: {e}")
