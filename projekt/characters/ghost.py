from characters.basic_character import BasicCharacter
from random import randint


class Ghost(BasicCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.basic_attack = randint(1, 10)
        self._max_hp = 85
        self._hp = 85
        self._max_mana = 45
        self._mana = 45

    def faight(self):
        print("==" * 10)
        print("--------- Watch out for ghost !!! ---------")
        super().print_basic_statistic()
        return self.basic_attack

    def drop(self):
        return randint(10, 45)
