from random import randint


class QuickBlade:

    def __init__(self) -> None:
        self._unlocked_bullet_storm = True
        self._unlocked_kill_zone = False
        self._unlocked_deadly_aim = False

    def bullet_storm(self, character):
        if character._mana >= 30:
            character._mana -= 30
            return 400
        else:
            print("There wasn't enough mana to complete the power")
            return 0

    def kill_zone(self, character):
        if character._mana >= 110:
            character._mana -= 110
            return randint(1, 1100)
        else:
            print("There wasn't enough mana to complete the power")
            return 0

    def deadly_aim(self, chatacter):
        atac = 0
        for i in range(chatacter._mana):
            atac = i * 4
        chatacter._mana = 0
        return atac

    def choose_spell(self, character):
        while True:
            try:
                print(f"a \t Bullet storm available? {self._unlocked_bullet_storm}")
                print(f"b \t Kill zone available? {self._unlocked_kill_zone}")
                print(f"c \t Deadly aim available? {self._unlocked_deadly_aim}")
                print(f"e \t Close the blade")
                inp = input().lower()
                if inp == "a" and self._unlocked_bullet_storm:
                    return self.bullet_storm(character)
                elif inp == "b" and self._unlocked_kill_zone:
                    return self.kill_zone(character)
                elif inp == "c" and self._unlocked_deadly_aim:
                    return self.deadly_aim(character)
                elif inp == "e":
                    print("Close the blade")
                    break
                else:
                    print("This power has not been unlocked yet or does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")

    # ready for use by you, my dears ;)
    def unlock_spels(self, character):
        while True:
            try:
                print(
                    f"a -1000 gold \t Bullet storm available? {self._unlocked_bullet_storm}"
                )
                print(
                    f"b -5000 gold \t Kill zone available? {self._unlocked_kill_zone}"
                )
                print(
                    f"c -10000 gold \t Deadly aim available? {self._unlocked_deadly_aim}"
                )
                print(f"e \t Close the blade")
                inp = input().lower()
                if (
                    inp == "a"
                    and not self._unlocked_bullet_storm
                    and character._gold >= 1000
                ):
                    self._unlocked_bullet_storm = True
                elif (
                    inp == "b"
                    and not self._unlocked_kill_zone
                    and character._gold >= 5000
                ):
                    self._unlocked_kill_zone = True
                elif (
                    inp == "c"
                    and not self._unlocked_deadly_aim
                    and character._gold >= 10000
                ):
                    self._unlocked_deadly_aim = True
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
