from typing import List
import time as t
import random as r


# main function Entry Point:
def main():
    print("\n\t\tWelcome To! Text Based Adventure Game")
    print("\t====================================================")

    player = Player()
    player_health = player.player_health

    player.print_players()

    selected_player = player.get_player()
    print(f"\n'{selected_player}' be ready.")

    enemy = Enemy()
    enemy_health = enemy.enemy_health
    enemy.print_enemies()

    selected_enemy = enemy.get_enemy()
    print(f"\nYour enemy is '{selected_enemy}' it looks tough.")

    weapons = Weapon()
    weapons.print_weapons()

    selected_weapon = weapons.get_weapon()
    print(f"\nYou have to fight with '{selected_weapon}' looks good.")

    battle = Battle(
        selected_player, selected_enemy, selected_weapon, enemy_health, player_health
    )

    while True:
        battle.start_fight()
        battle.print_options()
        battle.call_method()
        if battle.enemy_health <= 0 or battle.player_health <= 0:
            break


# creating a Player class to allow user to select anyone player
class Player:

    def __init__(self) -> None:
        self.players: List[str] = ["Hamza", "Saim", "Abdul Rafay", "Haris"]
        self.player_health: int = 100
        self.player: str = ""

    # method to print all the players name
    def print_players(self):
        print("\nEnter the number of player with which you want to play:")
        for i, player in enumerate(self.players, start=1):
            print(f"\n{i}. {player}.")

    # method to get the user select player
    def get_player(self):
        while True:
            user_input = input("\nEnter The number: ").strip()
            # check if the input is number
            if user_input.isdigit():
                index = int(user_input)

                # check if it is a valid number
                if 1 <= index <= len(self.players):
                    self.player = self.players[index - 1].title()
                    return self.player
                    break
                else:
                    print("Enter a valid number please!")
                    self.print_players()

            else:
                print("Enter a positive number please!")
                self.print_players()


# creating an enemy class to allow the user to select it's enemy
class Enemy:

    def __init__(self) -> None:
        self.enemies: List[str] = ["Huzaifa", "Saad", "Taheer", "Hunain"]
        self.enemy_health: int = 100
        self.enemy: str = ""

    # method to display all enemies name
    def print_enemies(self):
        print("\nEnter the number of your enemy with which you want to fight:")
        for i, enemy in enumerate(self.enemies, start=1):
            print(f"\n{i}. {enemy}.")

    # method to get the selected enemy
    def get_enemy(self):
        while True:
            user_input = input("\nEnter the number: ").strip()

            # checks if it is a number
            if user_input.isdigit():
                index = int(user_input)

                # check if it is a valid number
                if 1 <= index <= len(self.enemies):
                    self.enemy = self.enemies[index - 1].title()
                    return self.enemy
                    break
                else:
                    print("Enter a valid numbr please!")
                    self.print_enemies()

            else:
                print("Enter a positive number please!")
                self.print_enemies()


# creating a class to allow the user to select any weapon
class Weapon:
    def __init__(self) -> None:
        self.weapons: List[str] = ["Sword", "Sniper", "Axe", "SMG", "Assault Rifle"]
        self.damage: int = 20
        self.weapon: str = ""

    # method to show these weapons to the user
    def print_weapons(self):
        print(
            "\nEnter the number of your weapon (Your enemy will also have the same weapon):"
        )
        for i, weapon in enumerate(self.weapons, start=1):
            print(f"\n{i}. {weapon}.")

    # method to get the user select weapon
    def get_weapon(self):
        while True:
            user_input = input("\nEnter the number of your weapon: ").strip()

            # check it it is a number
            if user_input.isdigit():
                index = int(user_input)

                # check if the number is valid
                if 1 <= index <= len(self.weapons):
                    self.weapon = self.weapons[index - 1].title()
                    return self.weapon
                    break
                else:
                    print("Enter a valid number please!")
                    self.print_weapons()

            else:
                print("Enter a positive number please!")
                self.print_weapons()


# the main battle class
class Battle:
    def __init__(
        self,
        player_name: str,
        enemy_name: str,
        weapon: str,
        enemy_health: int,
        player_health: int,
    ) -> None:

        self.player: str = player_name  # store the selected player name
        self.enemy: str = enemy_name  # - - enemy name
        self.weapn: str = weapon  # - - weapon name
        self.player_health: int = player_health  # player health
        self.enemy_health: int = enemy_health  # -- enemy health
        self.options: List[str] = ["Attack", "Defend", "Heal (Increase 5% Health)"]
        self.selected_option: int = 0

    # print the message and both player and enemy name
    def start_fight(self):
        print(f"\n\t======== {self.player} V/S {self.enemy} ========")
        print(f"\n\tHealth = {self.player_health}%. \t\tHealth = {self.enemy_health}%.")

    def print_options(self):
        print("\nEnter the option number which you want to do:")
        for i, opt in enumerate(self.options, start=1):
            print(f"\n{i}. {opt.title()}.")

    def user_option(self):
        while True:
            user_input = input("\nEnter the option number: ").strip()
            # check if it is a number
            if user_input.isdigit():
                index = int(user_input)

                # check if it is a valid number
                if 1 <= index <= len(self.options):
                    self.selected_option = index - 1
                    return self.selected_option
                else:
                    print("Enter a valid number please!")
                    self.print_options()

            else:
                print("Enter a positive number please!")
                self.print_options()

    def call_method(self):
        option_num = self.user_option()
        if option_num == 0:
            self.attack()
        elif option_num == 1:
            self.defend()
        else:
            self.heal()

    def attack(self):
        if self.enemy_health <= 0:
            print(f"\n{self.player} already won the game!")
            return

        elif self.player_health <= 0:
            print(f"\n{self.enemy} already won the game!")
            return

        else:
            # player is attacking
            print(f"\n{self.player} is attacking using {self.weapn}.")
            t.sleep(2)
            random_num = r.randint(5, 40)
            self.enemy_health = self.enemy_health - random_num

            if self.enemy_health <= 0:
                print(
                    f"\n{self.player} has decreased {self.enemy_health + random_num}% health of it's enemy {self.enemy}."
                )
                print(f"\n{self.player} has won the game!")
                self.enemy_health = 0
                self.start_fight()
                return
            else:
                print(
                    f"\n{self.player} has decreased {random_num}% health of his enemy {self.enemy}."
                )
                t.sleep(2)
                self.start_fight()

            # enemy is attacking
            print(f"\nNow {self.enemy} is attacking using {self.weapn}.")
            t.sleep(2)
            random_num = r.randint(5, 40)
            self.player_health = self.player_health - random_num

            if self.player_health <= 0:
                print(
                    f"\n{self.enemy} has decreased {self.player_health + random_num}% health of it's enemy {self.player}."
                )
                print(f"\n{self.enemy} has won the game!")
                self.player_health = 0
                self.start_fight()
                return
            else:
                print(
                    f"\n{self.enemy} has decreased {random_num}% health of his enemy {self.player}."
                )
                t.sleep(2)

    # method which defends both players
    def defend(self):
        if self.enemy_health <= 0:
            print(f"\n{self.player} already won the game!")
            return

        elif self.player_health <= 0:
            print(f"\n{self.enemy} already won the game!")
            return

        else:
            print(f"\n{self.player} & {self.enemy} both are defending (for 5 seconds).")
            t.sleep(5)
            print("\nThe battle has started again.")

    # method which heal both players
    def heal(self):
        if self.enemy_health <= 0:
            print(f"\n{self.player} already won the game!")
            return

        if self.player_health <= 0:
            print(f"\n{self.enemy} already won the game!")
            return

        if self.enemy_health > 20 and self.player_health > 20:
            print("\nBoth players have more than 20% health. Healing is not needed.")
            return

        if self.enemy_health <= 20 and self.player_health <= 20:
            print(f"\nBoth players are healing (for 5 seconds).")
            self.enemy_health += 5
            self.player_health += 5
            t.sleep(5)
            print(f"\n5% increase in both {self.enemy}'s and {self.player}'s health.")
            return

        if self.enemy_health <= 20:
            print(f"\n{self.enemy} is healing (for 5 seconds).")
            self.enemy_health += 5
            t.sleep(5)
            print(f"\n5% increase in {self.enemy}'s health.")
            return

        if self.player_health <= 20:
            print(f"\n{self.player} is healing (for 5 seconds).")
            self.player_health += 5
            t.sleep(5)
            print(f"\n5% increase in {self.player}'s health.")
            return


if __name__ == "__main__":
    main()
