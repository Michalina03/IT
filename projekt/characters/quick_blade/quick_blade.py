from random import randint
import random


class QuickBlade:

    def __init__(self) -> None:
        self._unlocked_bullet_storm = True
        self._unlocked_wind_blade = False
        self._unlocked_shadow_burst = False

    def bullet_storm(self, character):
        if character._mana >= 300:
            character._mana -= 300
            return 150
        else:
            print("There wasn't enough mana to complete the power")
            return 0

    def wind_blade(self, character):
        if character._mana >= 400:
            character._mana -= 400
            base_damage = 15
            additional_hits = random.randint(1, 3)
            total_damage = base_damage * (1 + additional_hits)
            print(
                f"Wind Blade deals {base_damage} damage per hit, hitting {additional_hits} additional times for a total of {total_damage} damage."
            )
            return total_damage
        else:
            print("There wasn't enough mana to complete the spell")
            return 0

    def shadow_burst(self, character):
        if character._mana >= 450:
            character._mana -= 450
            base_damage = 120
            crit_chance = 0.25
            if random.random() < crit_chance:
                crit_damage = base_damage * 2
                print(f"Shadow Burst critically hits for {crit_damage} damage!")
                return crit_damage, "crit"
            else:
                print(f"Shadow Burst deals {base_damage} damage.")
                return base_damage
        else:
            print("There wasn't enough mana to complete the spell")
            return 0

    def choose_spell(self, character):
        while True:
            try:
                print(f"a \t Bullet storm available? {self._unlocked_bullet_storm}")
                print(f"b \t Wind blade available? {self._unlocked_wind_blade}")
                print(f"c \t Shadow burst available? {self._unlocked_shadow_burst}")
                print(f"e \t Close the blade")
                inp = input().lower()
                if inp == "a" and self._unlocked_bullet_storm:
                    return self.bullet_storm(character)
                elif inp == "b" and self._unlocked_wind_blade:
                    return self.wind_blade(character)
                elif inp == "c" and self._unlocked_shadow_burst:
                    return self.shadow_burst(character)
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
                    f"a) free spell! \t Bullet storm available? | - 300 mana | you deal - 150 hp | {self._unlocked_bullet_storm}"
                )
                print(
                    f"b) -1500 gold \t Wind blade available? | - 400 mana | you deal - total damage | {self._unlocked_wind_blade}"
                )
                print(
                    f"c) -2000 gold \t Shadow burst available? | - 450 mana | you deal - 120 hp + crit | {self._unlocked_shadow_burst}"
                )
                print(f"e \t Close the blade")
                inp = input().lower()
                if (
                    inp == "a"
                    and not self._unlocked_bullet_storm
                    and character._gold >= 1200
                ):
                    self._unlocked_bullet_storm = True
                elif (
                    inp == "b"
                    and not self._unlocked_wind_blade
                    and character._gold >= 1500
                ):
                    character._gold -= 1500
                    self._unlocked_wind_blade = True
                elif (
                    inp == "c"
                    and not self._unlocked_shadow_burst
                    and character._gold >= 2000
                ):
                    character._gold -= 2000
                    self._unlocked_shadow_burst = True
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
