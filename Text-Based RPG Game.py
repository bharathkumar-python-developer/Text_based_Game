import random

def start_game():
    print("Welcome to the RPG Game!")
    player_health = 100
    player_gold = 0
    player_location = "town"

    while True:
        print("\nYou are in the", player_location)
        print("Your health is", player_health)
        print("You have", player_gold, "gold")

        action = input("What do you want to do? (go north/south/east/west, rest, or quit) ")

        if action == "quit":
            break
        elif action == "rest":
            player_health += 10
            print("You rested and gained 10 health.")
        elif action.startswith("go "):
            direction = action[3:]
            if direction == "north":
                player_location = "forest"
            elif direction == "south":
                player_location = "town"
            elif direction == "east":
                player_location = "mountain"
            elif direction == "west":
                player_location = "river"

            if player_location == "forest":
                enemy_health = random.randint(20, 50)
                print("You encountered an enemy!")
                while enemy_health > 0:
                    attack = int(input("Do you want to attack? (1-10) "))
                    enemy_health -= attack
                    print("Enemy health:", enemy_health)
                player_gold += 10
                print("You defeated the enemy and gained 10 gold!")
            elif player_location == "mountain":
                treasure = random.randint(10, 50)
                print("You found treasure!")
                player_gold += treasure
                print("You gained", treasure, "gold!")
            elif player_location == "river":
                player_health -= 10
                print("You were attacked by a fish!")
                print("You lost 10 health.")
        else:
            print("Invalid action.")

start_game()
