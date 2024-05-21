from random import randint
import random


class NinjutsuTechniques:

    def __init__(self) -> None:
        self._unlocked_mistral_strike = True
        self._unlocked_flame_wave = False
        self._unlocked_thunder_clap = False

    def mistral_strike(self, character):
        if character._mana >= 150:
            character._mana -= 150
            return 60
        else:
            print("There wasn't enough mana to complete the attack")
            return 0

    def flame_wave(self, character):
        if character._mana >= 45:
            character._mana -= 45
            burn_damage = 5
            burn_duration = 4
            print(
                f"Flame Wave burns the enemy for {burn_damage} damage over {burn_duration} turns."
            )
            return 50
        else:
            print("There wasn't enough mana to complete the spell")
            return 0

    def thunder_clap(self, character):
        if character._mana >= 55:
            character._mana -= 55
            stun_chance = 0.4
            stun_effect = "stun" if random.random() < stun_chance else None
            print(
                f"Thunder Clap deals 35 damage."
                + (" Stuns the enemy." if stun_effect else "")
            )
            return 55
        else:
            print("There wasn't enough mana to complete the spell")
            return 0

    def choose_spell(self, character):
        while True:
            try:
                print(f"a \t Mistral strike available? {self._unlocked_mistral_strike}")
                print(f"b \t Flame wave available? {self._unlocked_flame_wave}")
                print(f"c \t Thunder clap available? {self._unlocked_thunder_clap}")
                print(f"e \t Close the techniques")
                inp = input().lower()
                if inp == "a" and self._unlocked_mistral_strike:
                    return self.mistral_strike(character)
                elif inp == "b" and self._unlocked_flame_wave:
                    return self.flame_wave(character)
                elif inp == "c" and self._unlocked_thunder_clap:
                    return self.thunder_clap(character)
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
                    f"a) free spell! \t Mistral strike available? | - 150 mana | you deal - 60 hp | {self._unlocked_mistral_strike}"
                )
                print(
                    f"b) -500 gold \t Flame wave available? | - 45 mana | you deal - 50 hp + burn | {self._unlocked_flame_wave}"
                )
                print(
                    f"c) -800 gold \t Thunder clap available? | - 55 mana | you deal - 55 hp + stun | {self._unlocked_thunder_clap}"
                )
                print(f"e \t Close the techniques")
                inp = input().lower()
                if (
                    inp == "a"
                    and not self._unlocked_mistral_strike
                    and character._gold >= 1000
                ):
                    self._unlocked_l = True
                elif (
                    inp == "b"
                    and not self._unlocked_flame_wave
                    and character._gold >= 500
                ):
                    character._gold -= 500
                    self._unlocked_flame_wave = True
                elif (
                    inp == "c"
                    and not self._unlocked_thunder_clap
                    and character._gold >= 800
                ):
                    character._gold -= 800
                    self._unlocked_thunder_clap = True
                elif inp == "e":
                    print("You don't have enough gold")
                    break
                else:
                    if inp in ["a", "b", "c"]:
                        print("Not enough gold or you know this attack.")
                    else:
                        print("This option do not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")
