from characters.mage import Mage
from characters.warrior import Warrior
from characters.goblin import Goglin
from characters.skeleton import Skeleton
import os

# =======================================================================


def one_on_one_fight(hero: Mage | Warrior, enemy):
    if enemy == "a":
        opponent = Goglin()
    elif enemy == "b":
        opponent = Skeleton()
    opponent.regeneration()
    hero.regeneration()
    while hero.is_alive() and opponent.is_alive():
        hero.reduce_hp(opponent.faight())
        opponent.reduce_hp(hero.faight())
    if not (hero.is_alive()):
        print("you gave your all today !!!")
        return None
    hero.add_gold(opponent.drop())


def main_game():
    print("Select a Character Class")
    print("a - magician")
    print("b - warrior")

    inp = input().lower()
    if inp == "a":
        my_hero = Mage()
    elif inp == "b":
        my_hero = Warrior()

    while my_hero.is_alive():
        day = 1
        os.system("clear")
        print(f"======================DAY: {day}============================")
        print("a - go to the dark forest")
        print("b - go to the dark castle")
        print("r - rest")
        print("e - exsit")
        my_hero.inf()
        print("==" * 20)

        inp = input().lower()
        if "a" == inp or "b" == inp:
            one_on_one_fight(my_hero, inp)
        elif "r" == inp:
            my_hero.total_rest()
        elif "e" == inp:
            print("the program has ended")
        else:
            print("there is no such command")


# =======================================================================


if __name__ == "__main__":
    main_game()

print("Thank you for playing !!!")
