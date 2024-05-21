from random import randint
import random


class TrapersKit:

    def __init__(self) -> None:
        self._unlocked_stealth_mastery = True
        self._unlocked_frost_bite = False
        self._unlocked_earth_shatter = False

    def stealth_mastery(self, character):
        if character._mana >= 200:
            character._mana -= 200
            return 60
        else:
            print("There wasn't enough mana to complete the power")
            return 0

    def frost_bite(self, character):
        if character._mana >= 50:
            character._mana -= 100
            freeze_chance = 0.3
            freeze_effect = "freeze" if random.random() < freeze_chance else None
            print(
                f"Frost Bite deals 30 damage."
                + (" Freezes the enemy." if freeze_effect else "")
            )
            return 70
        else:
            print("There wasn't enough mana to complete the spell")
            return 0

    def earth_shatter(self, character):
        if character._mana >= 60:
            character._mana -= 160
            stun_chance = 0.35
            stun_effect = "stun" if random.random() < stun_chance else None
            print(
                f"Earth Shatter deals 40 damage."
                + (" Stuns the enemy." if stun_effect else "")
            )
            return 90
        else:
            print("There wasn't enough mana to complete the spell")
            return 0

    def choose_spell(self, character):
        while True:
            try:
                print(
                    f"a \t Stealth mastery available? {self._unlocked_stealth_mastery}"
                )
                print(f"b \t Deadly accuracy available? {self._unlocked_frost_bite}")
                print(
                    f"c \t Shadow camouflage available? {self._unlocked_earth_shatter}"
                )
                print(f"e \t Close the kit")
                inp = input().lower()
                if inp == "a" and self._unlocked_stealth_mastery:
                    return self.stealth_mastery(character)
                elif inp == "b" and self._unlocked_frost_bite:
                    return self.frost_bite(character)
                elif inp == "c" and self._unlocked_earth_shatter:
                    return self.earth_shatter(character)
                elif inp == "e":
                    print("Close the book")
                    return 0
                else:
                    print("This spell has not been unlocked yet or does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def unlock_spels(self, character):
        while True:
            try:
                print(
                    f"a) free spell! \t Stealth mastery available? | - 200 mana | you deal - 60 hp | {self._unlocked_stealth_mastery}"
                )
                print(
                    f"b) -900 gold \t Frost bite available? | - 100 mana | you deal - 70 hp + freeze | {self._unlocked_frost_bite}"
                )
                print(
                    f"c) -1500 gold \t Earth shatter available? | - 160 mana | you deal - 90 hp + stun | {self._unlocked_earth_shatter}"
                )
                print(f"e \t Close the kit")
                inp = input().lower()
                if (
                    inp == "a"
                    and not self._unlocked_stealth_mastery
                    and character._gold >= 1000
                ):
                    self._unlocked_stealth_mastery = True
                elif (
                    inp == "b"
                    and not self._unlocked_frost_bite
                    and character._gold >= 900
                ):
                    character._gold -= 900
                    self._unlocked_frost_bite = True
                elif (
                    inp == "c"
                    and not self._unlocked_earth_shatter
                    and character._gold >= 1500
                ):
                    character._gold -= 1500
                    self._unlocked_earth_shatter = True
                elif inp == "e":
                    print("You don't have enough gold")
                    break
                else:
                    if inp in ["a", "b", "c"]:
                        print("Not enough gold or you know this power.")
                    else:
                        print("This option do not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")
