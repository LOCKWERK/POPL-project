import time
import random 
import sys

#hea;th is static, across all this no 
player_health = 100
npc_health = 100

print("Welcome to the dungeon game!, every choice you make decides your life, so choose wisely.")
def start_game():
    time.sleep(3)
    print("\nYou find yourself at a dungeon. You can go 'left' or 'right'.")
    
    # Start the main game loop
    while True:
        try:
            choice = input("Which way do you choose? (left/right/quit): ").lower()
            
            if choice == "left":
                dark_hallway()# this will proceed to the dark hallway scene
                break
            elif choice == "right":
                light_hallway()# this will proceed to the light hallway scene
                break
            elif choice == "quit":
                quit()
                break
            else:
                raise ValueError("Invalid choice! Please type 'left', 'right', or 'quit'.")
        except ValueError as ve:
            print(ve)
        finally:
            time.sleep(2)  # Add a short pause before the next input for a smoother experience

#hallway scenarios
def light_hallway():
    time.sleep(2)
    print("\nYou are in a hallway full of light. At the end of the hallway, there is a door with a face clad with gold")
    
    while True:
        try:
            print("The door: Welcome adventurer! for you to enter the room and claimm the treasures inside, you must answer a ridlle of mine. You only have chance")
            choice = input("Do you want to answer the riddle?'yes' or 'no': ").lower()
            time.sleep(2)
            if choice == "yes":
                print("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?")
                answer = input("\nYour answer: ").lower()
                time.sleep(2)
                if answer == "echo":
                    print("The door: Your answer is correct.")
                    treasure_scenario() 
                else:
                    print("The door: Your answer is wrong.")
                    print("\nA trap door opened underneath and you found yourself in the boss room")
                    ogre_scenario()
            elif choice == "no":
                return start_game()#if the user chooses no it will go back to the start of the game
            else:
                raise ValueError("Invalid choice! Please choose 'yes' or 'no'.")    
        except ValueError as ve:
            print(ve)
        finally:
            time.sleep(2) 

def dark_hallway():
    time.sleep(2)
    print("\nYou are in a dimly lighted hallway, the hallway feels cold and eerie. The walls are damp, and faint growls echo in the distance.")

    while True:
        try:
            choice = input("Do you choose the enter? 'yes' or 'no': ").lower()
            time.sleep(2)
            if choice == "yes":
                encounter_spider_web()
                break
            elif choice == "no":
                print("\nYou are now back at the entrance")
                return start_game()
            else:
                raise ValueError("Invalid choice! Please choose 'yes' or 'no'.")    
        except ValueError as ve:
            print(ve)
        finally:
            time.sleep(2)  

#functions for different scenarios
def encounter_spider_web():
    print("\nAs you move deeper into the hallway, you walk straight into a giant sticky spider web!")
    time.sleep(2)
    while True:
        try:
            choice = input("Do you try to 'cut' through the web or 'burn' it with a torch?: ").lower()
            time.sleep(2)
            if choice == "cut":
                print("\nYou cut through the web with your weapon, but giant spiders descend from the ceiling!")
                print("\nThe spiders attacked you.")
                while True:  # Loop for re-rolling in case of a draw
                    player_dice = player_roll()
                    spider_dice = npc_roll()
                    
                    if player_dice > spider_dice:
                        print("\nYou have defeated the spiders and continued deeper in the dungeon.")
                        ogre_scenario()
                        break
                    elif player_dice < spider_dice:
                        print("\nThe spiders overwhelm you with their venom bites...")
                        brutal_ending()     
                        break
                    else:
                        print("\nIt's a draw! Rolling again...")
                        time.sleep(1) 
                break
            elif choice == "burn":
                print("\nYou burn the web with your torch and escape unharmed, but the smoke alerts nearby creatures!")
                ghoul_scenario()
                break
            else:
                raise ValueError("Invalid choice! Please choose 'cut' or 'burn'.")
        except ValueError as ve:
            print(ve)
        finally:
            time.sleep(2)

def ghoul_scenario():
    print("\nThe smoke from the web alerts a group of ghouls!")
    time.sleep(2)
    while True:
        try:
            choice = input("Do you want to 'fight' the ghouls or try to 'hide' in a nearby alcove?: ").lower()
            time.sleep(2)
            if choice == "fight":
                print("\nYou engage in battle with the ghouls!")
                player_dice = player_roll()
                ghoul_dice = npc_roll()
                while True:  # Loop for re-rolling in case of a draw
                    player_dice = player_roll()
                    ghoul_dice = npc_roll()
                    
                    if player_dice > ghoul_dice:
                        print("\nYou have defeated the spiders and continued deeper in the dungeon.")
                        ogre_scenario()
                        break
                    elif player_dice < ghoul_dice:
                        print("\nThe spiders overwhelm you with their venom bites...")
                        brutal_ending()     
                        break
                    else:
                        print("\nIt's a draw! Rolling again...")
                        time.sleep(2)  # Optional: Adds a small delay before re-rolling
                break
            elif choice == "hide":
                print("\nYou successfully hide in the alcove until the ghouls pass. You proceed deeper into the dungeon.")
                deadly_trap()
                break
            else:
                raise ValueError("Invalid choice! Please choose 'fight' or 'hide'.")
        except ValueError as ve:
            print(ve)
        finally:
            time.sleep(2)


def deadly_trap():
    print("\nYou come across a narrow hallway with strange markings on the floor.")
    print("As you step forward, a hidden trap activates!")
    trap_roll = roll_dice()
    if trap_roll > 12:
        print("\nYou narrowly avoid the trap and make it through safely.")
        cursed_altar()
    else:
        print("\nYou have activated a trap and are struck by arrows from hidden walls...")
        brutal_ending()
    time.sleep(2)
def cursed_altar():
    print("\nYou find a strange altar glowing with an eerie light.")
    time.sleep(2)
    while True:
        try:
            choice = input("Do you want to 'touch' the altar or 'ignore' it and move on?: ").lower()
            time.sleep(2)
            if choice == "touch":
                print("\nAs you touch the altar, a dark curse envelops you!")
                cursed_treasure()
                break
            elif choice == "ignore":
                print("\nYou wisely avoid the altar and move on.")
                treasure_room()
                break
            else:
                raise ValueError("Invalid choice! Please choose 'touch' or 'ignore'.")
        except ValueError as ve:
            print(ve)
        finally:
            time.sleep(2)      
    
def ogre_scenario():
    global player_health, npc_health
    print("\nYou encountered a fierce Ogre!")
    time.sleep(2)
    while True:
        try:
            choice = input("Do you want to 'fight', 'run', or 'sneak' past the Ogre?: ").lower()
            time.sleep(2)
            if choice == "fight":
                print("You choose to fight the Ogre!")
                fight(player_health, npc_health)
                break
            elif choice == "run":
                print("You successfully escape back to the starting point.")
                return start_game() 
            elif choice == "sneak":
                print("\nYou attempt to sneak past the Ogre!")
                player_result = player_roll()
                ogre_result = npc_roll()

                if player_result > ogre_result:
                    print("\nYou have succesfully sneaked past the ogre!")
                    safe_spot()
                    
                else:
                    print("\nThe Ogre notices you and attacks!")
                    brutal_ending()
                break
            else:
                raise ValueError("Invalid choice! Please choose 'fight', 'run', or 'sneak'.")
        except ValueError as ve:
            print(ve)
        finally:
            time.sleep(2)

def treasure_scenario():
    print("\nYou find a treasure chest!")
    time.sleep(2)
    while True:
        try:
            choice = input("Do you want to 'open' the chest or 'leave' it?: ").lower()
            time.sleep(2)
            if choice == "open":
                print("Inside the chest, you find a paradise that is perfect and you decide to stay. The dungeon traps you with the things you desire most")
                brutal_ending()
                break
            elif choice == "leave":
                print("You decide to leave the treasure chest and head back to the starting point.")
                return start_game() 
            else:
                raise ValueError("Invalid choice! Please choose 'open' or 'leave'.")
        except ValueError as ve:
            print(ve)
        finally:
            time.sleep(2)

def goblin_room():
    print("\nYou found yourself in a room full of goblins ")
    time.sleep(2)
    while True:
        try:
            choice = ("Do you choose to 'fight', 'sneak' past them or 'run'? ")

            if choice == "fight":
                print("You choose to fight the Goblins.")
                player_dice = player_roll()
                goblin_dice = npc_roll()

                if player_dice > goblin_dice:
                    print("You killed all the Goblins in the room. ")
                else:
                    print("\nYou were killed by the Goblins.")
                break
            elif choice == "sneak":
                print("\nYou choose to sneak past the Goblins")
                player_dice = player_roll()
                awareness = npc_roll()

                if player_dice > awareness:
                    print("\nThe goblins doesn't notice you and sneaked past them.")
                    treasure_room()

                else:
                    print("\nThe Goblins saw you sneaking and gets ambushed.")
                    brutal_ending()
                break
            elif choice == "run":
                print("\nYou have returned to the entrance")
            else:
                print
        except ValueError as ve:
            print(ve)
        finally:
            time.sleep(2)
def treasure_room():
    print("\nYou enter a grand chamber filled with treasure chests.")
    print("However, you sense danger lurking nearby.")
    time.sleep(2)
    while True:
        try:
            choice = input("Do you want to 'open' a chest or 'leave' the room?: ").lower()
            if choice == "open":
                print("\nYou open a chest and find a powerful weapon!")
                print("With renewed strength, you find an exit leading to safety.")
                safe_spot()
                break
            elif choice == "leave":
                print("\nYou decide to leave the treasure untouched and escape the dungeon.")
                safe_spot()
                break
            else:
                raise ValueError("Invalid choice! Please choose 'open' or 'leave'.")
        except ValueError as ve:
            print(ve)
        finally:
            time.sleep(2)
#fight mechanics

def fight(player_health, npc_health):
    print("\nThe fight begins!")
    
    while player_health > 0 and npc_health > 0:
        print(f"\nYour Health: {player_health} | Ogre's Health: {npc_health}")
        
        # Player rolls
        player_roll_result = player_roll()
        
        # Ogre rolls
        ogre_roll_result = npc_roll()

        # Determine outcome
        if player_roll_result > ogre_roll_result:
            damage = player_roll_result * 5  # Player deals damage
            npc_health -= damage
            print(f"You dealt {damage} damage to the Enemy!")
        elif player_roll_result < ogre_roll_result:
            damage = ogre_roll_result * 5  # Ogre deals damage
            player_health -= damage
            print(f"The Enemy dealt {damage} damage to you!")
        else:
            print("Both rolled the same! No damage dealt this round.")

        # Check for defeat
        if player_health <= 0:
            print("\nYou have been defeated by the enemy")
            brutal_ending()
            return
        if npc_health <= 0:
            print("\nYou have defeated the emeny")
            safe_spot()
            return

    
#dice funcrtions
def roll_dice():
    return random.randint(1, 24)

def player_roll(): #player initates thhe dice roll
    input("\nPress enter to roll dice...")
    roll = roll_dice()
    print(f"Your roll is: {roll}")
    return roll

def npc_roll(): #the enemy automatically rolls the dice
    print("\nThe enemy is rolling the dice...")
    rolled = roll_dice()
    time.sleep(2) #adding a time delay for the ememy for more suspense
    print(f"The enemy rolled a {rolled} !")
    return rolled    

#functions for endings and different ending scenario
def safe_spot():#if the user chooses the sneak option 
    time.sleep(2)
    print("\nThe safe spot is full of treasure and leads to an exit.")
    print("You’ve escaped the dungeon with riches beyond imagination!")
    quit()

def cursed_treasure():
    time.sleep(2)
    print("\nAs you take the treasure, a curse is placed on you!")
    print("You are forever trapped in the dungeon as its new guardian.")
    brutal_ending()

def brutal_ending():
    time.sleep(2)
    print("\nYou have been consumed and failed to conquer the dungeon. the game will now end... Thank  you for playing!")
    sys.exit()

def quit():#this function is the main ending if the user chooses to quit
    time.sleep(2)
    print("\nThank you for playing!")
    sys.exit()

#runs the game
start_game()
