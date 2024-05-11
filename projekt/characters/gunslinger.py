from characters.basic_character import BasicCharacter
from characters.quick_blade.quick_blade import QuickBlade


class Gunslinger(BasicCharacter):
    def __init__(self) -> None:
        super().__init__()
        self._basic_attack += 10
        self._max_hp = 100
        self._hp = 100
        self._hp_regeneration = 1
        self._max_mana = 500
        self._mana = 500
        self._mana_regeneration = 5
        # --------------------------
        self._spell_book = QuickBlade()
        self._equipment = []

    def inf(self):
        print("===" * 10)
        print("Your character")
        print(f"max_hp: {self._max_hp} \t max_mana: {self._max_mana}")
        print(f"hp: {self._hp} \t mana: {self._mana}")
        print(f"GOLD:  {self._gold}")
        print("===" * 10)

    def faight(self):
        while True:
            self.inf()
            print("a - basic_attack")
            print("b - open QuickBlade")
            damage = 0
            inp = input().lower()
            if inp == "a":
                return self._basic_attack
            elif inp == "b":
                return self._spell_book.choose_spell(self)
            else:
                print("there is no such attack")
