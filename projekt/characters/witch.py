from characters.basic_character import BasicCharacter
from random import randint


class Witch(BasicCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.basic_attack = randint(1, 10)
        self._max_hp = 95
        self._hp = 95
        self._max_mana = 55
        self._mana = 55

    def faight(self):
        print("==" * 10)
        print("--------- Watch out for witch !!! ---------")
        super().print_basic_statistic()
        return self.basic_attack

    def drop(self):
        return randint(10, 50)
