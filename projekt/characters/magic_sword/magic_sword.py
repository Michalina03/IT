from random import randint


class MagicSword:

    def __init__(self) -> None:
        self._unlocked_astral_slash = True
        self._unlocked_elemental_strike = False
        self._unlocked_airon_storm = False

    def astral_slash(self, character):
        if character._mana >= 10:
            character._mana -= 10
            return 300
        else:
            print("There wasn't enough mana to complete the attack")
            return 0

    def elemental_strike(self, character):
        if character._mana >= 50:
            character._mana -= 50
            return randint(1, 500)
        else:
            print("There wasn't enough mana to complete the spell")
            return 0

    def airon_storm(self, chatacter):
        atac = 0
        for i in range(chatacter._mana):
            atac = i * 4
        chatacter._mana = 0
        return atac

    def choose_spell(self, character):
        while True:
            try:
                print(f"a \t Fire Ball available? {self._unlocked_astral_slash}")
                print(f"b \t Lighting available? {self._unlocked_elemental_strike}")
                print(
                    f"c \t Elemental Annihilation available? {self._unlocked_airon_storm}"
                )
                print(f"e \t Close the book")
                inp = input().lower()
                if inp == "a" and self._unlocked_astral_slash:
                    return self.astral_slash(character)
                elif inp == "b" and self._unlocked_elemental_strike:
                    return self.elemental_strike(character)
                elif inp == "c" and self._unlocked_airon_storm:
                    return self.airon_storm(character)
                elif inp == "e":
                    print("Close the book")
                    break
                else:
                    print("This spell has not been unlocked yet or does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")

    # ready for use by you, my dears ;)
    def unlock_spels(self, character):
        while True:
            try:
                print(f"a -1000\t Fire Ball available? {self._unlocked_astral_slash}")
                print(
                    f"b -5000g \t Lighting available? {self._unlocked_elemental_strike}"
                )
                print(
                    f"c -10000g \t Elemental Annihilation available? {self._unlocked_airon_storm}"
                )
                print(f"e \t Close the book")
                inp = input().lower()
                if (
                    inp == "a"
                    and not self._unlocked_astral_slash
                    and character._gold >= 1000
                ):
                    self._unlocked_astral_slash = True
                elif (
                    inp == "b"
                    and not self._unlocked_elemental_strike
                    and character._gold >= 5000
                ):
                    self._unlocked_elemental_strike = True
                elif (
                    inp == "c"
                    and not self._unlocked_airon_storm
                    and character._gold >= 10000
                ):
                    self._unlocked_airon_storm = True
                elif inp == "e":
                    print("You don't have enough gold")
                    break
                else:
                    if inp in ["a", "b", "c"]:
                        print("Not enough gold or you know this spell.")
                    else:
                        print("This option do not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")
