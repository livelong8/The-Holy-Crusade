import random
import json

# Load enemy data from the JSON file
with open("/Users/HESCHRAI000/code/enemyData.json", "r") as enemy_file:
    enemy_data = json.load(enemy_file)

def main():
    difficulty = get_difficulty()
    play_game(difficulty)

def get_difficulty():
    while True:
        difficulty = input("How hard do you want the game to be (1-5 is recommended)?: ")
        confirm = input(f"You've chosen {difficulty}, are you sure? (y/n): ")
        if confirm.lower() == "y":
            return int(difficulty)

def play_game(difficulty):
    global points
    player_hp = 100
    enemy_names = list(enemy_data.keys())

    while player_hp > 0:
        enemy = random.choice(enemy_names)
        enemy_stats = enemy_data[enemy]
        enemy_hp = enemy_stats['hp'] * difficulty
        enemy_dmg = enemy_stats['dmg'] * difficulty
        enemy_ac = enemy_stats['ac'] + difficulty

        print(f"You find a {enemy} with {enemy_hp} health.")
        choice = input("Do you want to fight or run? ")

        if choice.lower() == "run":
            if points <= 50:
                print("You ran away!")
                break
            else:
                print("You return victorious!")
                break

        elif choice.lower() == "fight":
            while player_hp > 0 and enemy_hp > 0:
                hit = input("Roll to hit? ")
                if hit == "":
                    if random.randint(1, 20) > enemy_ac:
                        damage = random.randint(1, enemy_dmg)
                        enemy_hp -= damage
                        print(f"You hit the {enemy} for {damage} damage!")
                    else:
                        print("You missed!")
                else:
                    print("Invalid input!")
                    continue

                if enemy_hp <= 0:
                    print(f"You defeated the {enemy}!")
                    points += 10 * difficulty
                    break

                enemy_hit = random.randint(1, 20)
                player_hp -= enemy_hit
                print(f"The {enemy} hit you for {enemy_hit} damage!")

            if player_hp <= 0:
                print(f"You lost! Your score was {points}.")
                break

if __name__ == "__main__":
    points = 0
    main()
