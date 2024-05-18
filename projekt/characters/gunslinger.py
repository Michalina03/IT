from characters.basic_character import BasicCharacter
from characters.quick_blade.quick_blade import QuickBlade


class Gunslinger(BasicCharacter):
    def __init__(self) -> None:
        super().__init__()
        self._basic_attack += 10
        self._max_hp = 200
        self._hp = 200
        self._hp_regeneration = 1
        self._max_mana = 1500
        self._mana = 1500
        self._mana_regeneration = 5
        self._health_potion = 0
        self._mana_potion = 0
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

    def use_health_potion(self):
        if self._health_potion > 0:
            self._health_potion -= 1
            self._hp += 100
        else:
            print("You don't have health potion")

    def use_mana_potion(self):
        if self._mana_potion > 0:
            self._mana_potion -= 1
            self._mana += 200
        else:
            print("You don't have mana potion")

    def faight(self):
        while True:
            self.inf()
            print("a - basic_attack ( - 10 hp )")
            print("b - open QuickBlade")
            print("c - use mana potion")
            print("d - use health potion")
            damage = 0

            inp = input().lower()

            if inp == "c":
                self.use_mana_potion()
            elif inp == "d":
                self.use_health_potion()
            if inp == "a":
                return self._basic_attack
            elif inp == "b":
                return self._spell_book.choose_spell(self)
            else:
                print("there is no such attack")
