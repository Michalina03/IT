from characters.basic_character import BasicCharacter
from random import randint

class Goglin(BasicCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.basic_attack  = randint(1,10)
        self._max_hp = 90
        self._hp = 90
        self._max_mana =50
        self._mana = 50

    def faight(self):
        print("=="*10)
        print("Evil goblin !!!")
        super().print_basic_statistic()
        return self.basic_attack
    
    def drop(self):
        return randint(10,50)
    

