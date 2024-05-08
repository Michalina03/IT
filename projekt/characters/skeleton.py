from characters.basic_character import BasicCharacter
from random import randint


class Skeleton(BasicCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.basic_attack = randint(1, 10)
        self._max_hp = 100
        self._hp = 110
        self._max_mana = 70
        self._mana = 80

    def faight(self):
        print("==" * 10)
        print("Evil skeleton !!!")
        super().print_basic_statistic()
        return self.basic_attack

    def drop(self):
        return randint(10, 50)
