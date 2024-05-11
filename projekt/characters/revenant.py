from characters.basic_character import BasicCharacter
from random import randint


class Revenant(BasicCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.basic_attack = randint(1, 11)
        self._max_hp = 80
        self._hp = 80
        self._max_mana = 40
        self._mana = 40

    def faight(self):
        print("==" * 10)
        print("--------- Watch out for revenant !!! ---------")
        super().print_basic_statistic()
        return self.basic_attack

    def drop(self):
        return randint(5, 40)
