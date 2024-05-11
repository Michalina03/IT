from random import randint


class NinjutsuTechniques:

    def __init__(self) -> None:
        self._unlocked_mistral_strike = True
        self._unlocked_shadow_dance = False
        self._unlocked_serpent_sting = False

    def mistral_strike(self, character):
        if character._mana >= 25:
            character._mana -= 25
            return 250
        else:
            print("There wasn't enough mana to complete the attack")
            return 0

    def shadow_dance(self, character):
        if character._mana >= 90:
            character._mana -= 90
            return randint(1, 900)
        else:
            print("There wasn't enough mana to complete the attack")
            return 0

    def serpent_sting(self, chatacter):
        atac = 0
        for i in range(chatacter._mana):
            atac = i * 3
        chatacter._mana = 0
        return atac

    def choose_spell(self, character):
        while True:
            try:
                print(f"a \t Mistral strike available? {self._unlocked_mistral_strike}")
                print(f"b \t Shadow dance available? {self._unlocked_shadow_dance}")
                print(f"c \t Serpent sting available? {self._unlocked_serpent_sting}")
                print(f"e \t Close the techniques")
                inp = input().lower()
                if inp == "a" and self._unlocked_mistral_strike:
                    return self.mistral_strike(character)
                elif inp == "b" and self._unlocked_shadow_dance:
                    return self.shadow_dance(character)
                elif inp == "c" and self._unlocked_serpent_sting:
                    return self.serpent_sting(character)
                elif inp == "e":
                    print("Close the techniques")
                    break
                else:
                    print("This attack has not been unlocked yet or does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")

    # ready for use by you, my dears ;)
    def unlock_spels(self, character):
        while True:
            try:
                print(
                    f"a -1000 gold\t Mistral strike available? {self._unlocked_mistral_strike}"
                )
                print(
                    f"b -5000 gold \t Shadow dance available? {self._unlocked_shadow_dance}"
                )
                print(
                    f"c -10000 gold \t Serpent sting available? {self._unlocked_serpent_sting}"
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
                    and not self._unlocked_shadow_dance
                    and character._gold >= 5000
                ):
                    self._unlocked_shadow_dance = True
                elif (
                    inp == "c"
                    and not self._unlocked_serpent_sting
                    and character._gold >= 10000
                ):
                    self._unlocked_serpent_sting = True
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
