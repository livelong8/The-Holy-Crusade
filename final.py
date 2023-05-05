import random

points = 0

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
    enemy_hp = 0
    enemy_names = ["Goblin", "Skeleton", "Orc", "Ogre"]

    while player_hp > 0:
        enemy = random.choice(enemy_names)
        enemy_hp = 10 * random.randint(1, difficulty) + 10 * difficulty
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
                    if random.randint(1, 20) > 10:
                        damage = 10 + 5 * difficulty
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
    main()
