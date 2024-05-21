from characters.mage import Mage
from characters.warrior import Warrior
from characters.ninja import Ninja
from characters.hunter import Hunter
from characters.monk import Monk
from characters.goblin import Goglin
from characters.skeleton import Skeleton
from characters.revenant import Revenant
from characters.witch import Witch
from characters.ghost import Ghost
from city.mage_shop import MageShop
from city.warrior_shop import WarriorShop
from city.ninja_shop import NinjaShop
from city.hunter_shop import HunterShop
from city.monk_shop import MonkShop
from game_events.boss import Boss
import os

# =======================================================================


def one_on_one_fight(hero: Mage | Warrior | Ninja | Hunter | Monk, enemy):
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
    elif enemy == "h":
        opponent = Boss()
    opponent.regeneration()
    hero.regeneration()
    while hero.is_alive() and opponent.is_alive():
        os.system("cls" if os.name == "nt" else "clear")
        hero.reduce_hp(opponent.faight())
        opponent.reduce_hp(hero.faight())

    if not (hero.is_alive()):
        print("---- You gave your all today !!! ----")
        return None
    hero.add_gold(opponent.drop())


def chose_shop(my_hero):
    try:
        if isinstance(my_hero, Mage):
            shop = MageShop()
        elif isinstance(my_hero, Warrior):
            shop = WarriorShop()
        elif isinstance(my_hero, Ninja):
            shop = NinjaShop()
        elif isinstance(my_hero, Hunter):
            shop = HunterShop()
        elif isinstance(my_hero, Monk):
            shop = MonkShop()
        return shop
    except UnboundLocalError:
        print("--- Check korekt option ---")


def chose_class():
    print("=====  Select a Character Class  =====")
    print(" a - magician ")  # hp: 100 mana: 500
    print(" b - warrior")  # hp: 125 mana: 700
    print(" c - ninja")  # hp: 150 mana: 1000
    print(" d - hunter")  # hp: 175 mana: 1250
    print(" e - monk")  # hp: 200 mana: 1500

    inp = input().lower()
    try:
        if inp == "a":
            my_hero = Mage()
        elif inp == "b":
            my_hero = Warrior()
        elif inp == "c":
            my_hero = Ninja()
        elif inp == "d":
            my_hero = Hunter()
        elif inp == "e":
            my_hero = Monk()
        return my_hero
    except UnboundLocalError:
        print("--- Check korekt option ---")


def main_game():
    my_hero = chose_class()
    if my_hero is None:
        my_hero = chose_class()
    shop = chose_shop(my_hero)
    day = 1
    while my_hero.is_alive():
        os.system("cls" if os.name == "nt" else "clear")
        print(f"======================DAY: {day}============================")
        print(
            "a - go to the dark forest"
        )  # goblin: hp: 40 mana: 20 drop: 10-20 attack: 1-10
        print(
            "b - go to the dark castle"
        )  # skeletor: hp: 70 mana: 45 drop: 20-40 attack: 10-15
        print(
            "c - go to the dark cosmos"
        )  # revenant: hp: 120 mana: 80 drop: 40-100 attack: 15-20
        print(
            "d - go to the dark caves"
        )  # witch: hp: 150 mana: 100 drop: 100-200 attack: 20-40
        print(
            "e - go to the haunted house"
        )  # ghost: hp: 200 mana: 160 drop: 200-400 attack: 40-100
        print("f - city")
        print("g - change class ( 10000 gold )")
        print("h - BOSS !!! ")
        print("r - rest")
        print("x - exit")
        my_hero.inf()
        print("==" * 20)

        inp = input().lower()
        if (
            "a" == inp
            or "b" == inp
            or "c" == inp
            or "d" == inp
            or "e" == inp
            or "h" == inp
        ):
            one_on_one_fight(my_hero, inp)
        elif "f" == inp:
            shop.choose_modification(my_hero)
        elif "r" == inp:
            my_hero.total_rest()
            day += 1
        elif "g" == inp:
            if my_hero._gold >= 10000:
                my_hero._gold -= 10000
                my_hero = chose_class()
                shop = chose_shop(my_hero)
            else:
                print("---- Not enough gold ----")
        elif "x" == inp:
            print("------ The program has ended ------")
            my_hero.is_alive = False
        else:
            print("--- There is no such command ---")


# =======================================================================


if __name__ == "__main__":
    print("")
    print(
        "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  Welcome to Battle Masters.  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
    )
    print(
        "|                                                                                                        |"
    )
    print(
        "|  Choose better and better but more expensive characters.                                               |"
    )
    print(
        "|  Explore worlds where dangerous goblins and difficult to defeat ghosts await you.                      |"
    )
    print(
        "|  Kill monsters, get gold and go to the city where you can improve your character and buy powers for it |"
    )
    print(
        "|  If your power value is True you can use it,                                                           |"
    )
    print(
        "|  if its value is False go to the city where you can buy it for a certain amount of gold.               |"
    )
    print(
        "|                                                                                                        |"
    )
    print(
        "-------------------------------------          Good luck !          --------------------------------------"
    )
    print("")
    main_game()
print("")
print("=-=-=-=-=-=- Thank you for playing !!! -=-=-=-=-=-=")
