from characters.mage import Mage
from characters.warrior import Warrior
from characters.ninja import Ninja
from characters.tracker import Tracker
from characters.gunslinger import Gunslinger
from characters.goblin import Goglin
from characters.skeleton import Skeleton
from characters.revenant import Revenant
from characters.witch import Witch
from characters.ghost import Ghost
import os

# =======================================================================


def one_on_one_fight(hero: Mage | Warrior | Ninja | Tracker | Gunslinger, enemy):
    if enemy == "a":
        opponent = Goglin()
    elif enemy == "b":
        opponent = Skeleton()
    elif enemy == "c":
        opponent = Revenant()
    elif enemy == "d":
        opponent = Witch()
    elif enemy == "e":
        opponent = Ghost()
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
    print("c - ninja")
    print("d - tracker")
    print("e - gunslinger")

    inp = input().lower()
    if inp == "a":
        my_hero = Mage()
    elif inp == "b":
        my_hero = Warrior()
    elif inp == "c":
        my_hero = Ninja()
    elif inp == "d":
        my_hero = Tracker()
    elif inp == "e":
        my_hero = Gunslinger()

    while my_hero.is_alive():
        day = 1
        os.system("clear")
        print(f"======================DAY: {day}============================")
        print("a - go to the dark forest")
        print("b - go to the dark castle")
        print("c - go to the dark cosmos")
        print("d - go to the dark caves")
        print("e - go to the haunted house")
        print("r - rest")
        print("x - exsit")
        my_hero.inf()
        print("==" * 20)

        inp = input().lower()
        if "a" == inp or "b" == inp or "c" == inp or "d" == inp or "e" == inp:
            one_on_one_fight(my_hero, inp)
        elif "r" == inp:
            my_hero.total_rest()
        elif "x" == inp:
            print("the program has ended")
        else:
            print("there is no such command")


# =======================================================================


if __name__ == "__main__":
    main_game()

print("Thank you for playing !!!")
