from random import randint


class ElemnetalSpellBook:

    def __init__(self) -> None:
        self._unlocked_fire_ball = True
        self._unlocked_lighting = False
        self._unlocked_elemental_annihilation = False

    def fire_ball(self, character):
        if character._mana >= 20:
            character._mana -= 20
            return 200
        else:
            print("There wasn't enough mana to complete the spell")
            return 0

    def lighting(self, character):
        if character._mana >= 100:
            character._mana -= 100
            return randint(1, 1000)
        else:
            print("There wasn't enough mana to complete the spell")
            return 0

    def elemental_annihilation(self, chatacter):
        atac = 0
        for i in range(chatacter._mana):
            atac = i * 4
        chatacter._mana = 0
        return atac

    def choose_spell(self, character):
        while True:
            try:
                print(f"a \t Fire Ball available? {self._unlocked_fire_ball}")
                print(f"b \t Lighting available? {self._unlocked_lighting}")
                print(
                    f"c \t Elemental Annihilation available? {self._unlocked_elemental_annihilation}"
                )
                print(f"e \t Close the book")
                inp = input().lower()
                if inp == "a" and self._unlocked_fire_ball:
                    return self.fire_ball(character)
                elif inp == "b" and self._unlocked_lighting:
                    return self.lighting(character)
                elif inp == "c" and self._unlocked_elemental_annihilation:
                    return self.elemental_annihilation(character)
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
                print(f"a -1000\t Fire Ball available? {self._unlocked_fire_ball}")
                print(f"b -5000g \t Lighting available? {self._unlocked_lighting}")
                print(
                    f"c -10000g \t Elemental Annihilation available? {self._unlocked_elemental_annihilation}"
                )
                print(f"e \t Close the book")
                inp = input().lower()
                if (
                    inp == "a"
                    and not self._unlocked_fire_ball
                    and character._gold >= 1000
                ):
                    self._unlocked_fire_ball = True
                elif (
                    inp == "b"
                    and not self._unlocked_lighting
                    and character._gold >= 5000
                ):
                    self._unlocked_lighting = True
                elif (
                    inp == "c"
                    and not self._unlocked_elemental_annihilation
                    and character._gold >= 10000
                ):
                    self._unlocked_elemental_annihilation = True
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
