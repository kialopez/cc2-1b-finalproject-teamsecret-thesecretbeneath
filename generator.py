from maps import maze1, maze2, maze3, maze4, maze5
import os
import random
from clear import clearOutput, deathScreen
import time

def playMaze():
    WALL = '#'
    EMPTY = ' '
    START = 'S'
    EXIT = 'E'
    PLAYER = '@'
    BLOCK = chr(9608)

    def displayMaze(maze):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) == (playerx, playery):
                    print(PLAYER, end='')
                elif (x, y) == (exitx, exity):
                    print('X', end='')
                elif maze[(x, y)] == WALL:
                    print(BLOCK, end='')
                else:
                    print(maze[(x, y)], end='')
            print()

    mazeFile = random.choice([maze1, maze2, maze3, maze4, maze5])
    maze = {}
    lines = mazeFile
    playerx = None
    playery = None
    exitx = None
    exity = None
    y = 0
    play = True
    for line in lines:
        WIDTH = len(line.rstrip())
        for x, character in enumerate(line.rstrip()):
            assert character in (WALL, EMPTY, START, EXIT), 'Invalid character at column {}, line {}'.format(x + 1, y + 1)
            if character in (WALL, EMPTY):
                maze[(x, y)] = character
            elif character == START:
                playerx, playery = x, y
                maze[(x, y)] = EMPTY
            elif character == EXIT:
                exitx, exity = x, y
                maze[(x, y)] = EMPTY
        y += 1
    HEIGHT = y

    assert playerx != None and playery != None, 'No start in maze file.'
    assert exitx != None and exity != None, 'No exit in maze file.'

    while play == True: 
        print("The Quest of Mojo")
        print()
        displayMaze(maze)
        print()
        print("Get to the X to get to Carnivale's Throne.")
        print()
        while True:
            print('                  W')
            print('Enter direction: ASD')
            move = input('> ').upper()

            if move not in ['W', 'A', 'S', 'D']:
                print('Invalid direction. Enter one of W, A, S, or D.')
                clearOutput(4)
                continue

            if move == 'W' and maze[(playerx, playery - 1)] == EMPTY:
                break
            elif move == 'S' and maze[(playerx, playery + 1)] == EMPTY:
                break
            elif move == 'A' and maze[(playerx - 1, playery)] == EMPTY:
                break
            elif move == 'D' and maze[(playerx + 1, playery)] == EMPTY:
                break

            print('You cannot move in that direction.')
            clearOutput(4)
        if move == 'W':
            while True:
                playery -= 1
                if (playerx, playery) == (exitx, exity):
                    break
                if maze[(playerx, playery - 1)] == WALL:
                    break  
                if (maze[(playerx - 1, playery)] == EMPTY
                    or maze[(playerx + 1, playery)] == EMPTY):
                    break
            randomEnemy()  
            os.system('cls')
        elif move == 'S':
            while True:
                playery += 1
                if (playerx, playery) == (exitx, exity):
                    break
                if maze[(playerx, playery + 1)] == WALL:
                    break  
                if (maze[(playerx - 1, playery)] == EMPTY
                    or maze[(playerx + 1, playery)] == EMPTY):
                    break  
            randomEnemy()
            os.system('cls')
        elif move == 'A':
            while True:
                playerx -= 1
                if (playerx, playery) == (exitx, exity):
                    break
                if maze[(playerx - 1, playery)] == WALL:
                    break 
                if (maze[(playerx, playery - 1)] == EMPTY
                    or maze[(playerx, playery + 1)] == EMPTY):
                    break 
            randomEnemy()
            os.system('cls')
        elif move == 'D':
            while True:
                playerx += 1
                if (playerx, playery) == (exitx, exity):
                    break
                if maze[(playerx + 1, playery)] == WALL:
                    break 
                if (maze[(playerx, playery - 1)] == EMPTY
                    or maze[(playerx, playery + 1)] == EMPTY):
                    break
            randomEnemy()
            os.system('cls')

        if (playerx, playery) == (exitx, exity):
            os.system('cls')
            print("The Quest of Mojo")
            print()
            play = False

def randomEnemy():
    global randomEnemyCounter
    randomEnemyCounter += random.randint(1, 15)
    if randomEnemyCounter >= 26:
        enemy = random.randint(1, 3)
        if enemy == 1:
            print("You encountered a demon!")
        elif enemy == 2:
            print("You encountered a human trafficker!")
        elif enemy == 3:
            print("You encountered a monster!")
        print()
        enemyFight()
        os.system('cls')
        randomEnemyCounter = random.randint(1, 10)
        print("The Quest of Mojo")
        print()

def enemyFight():
    enemyHealth = random.randint(250, 500)
    criticalHit = 0
    global health
    global healCounter
    global attack
    global defense

    print("------------------------------------------------------------")
    print()
    while health > 0:
        if health >= 0:
            print(f"Attack: {attack} | Defense: {defense} | Health: {health} | Enemy Health: {enemyHealth}")
            print()
            print("What will you do?")
            print("1. Attack")
            print(f"2. Heal ({healCounter} left)")
            print("3. Run")
            print()
            choice = input("Enter choice: ")
            print()
            time.sleep(0.5)

            if choice == "1": 
                dmg = random.randint(attack, attack+125)
                enemyHealth -= dmg
                if enemyHealth <= 0:
                    enemyHealth = 0
                    if dmg >= attack+90:
                        print("Critical hit!")
                        criticalHit += 1
                    print("You dealt", dmg, "damage to the enemy!")
                    print("The enemy has", enemyHealth, "health left!")
                    print()
                    break
                else:
                    if dmg >= attack+90:
                        print("Critical hit!")
                    print("You dealt", dmg, "damage to the enemy!")
                    print("The enemy has", enemyHealth, "health left!")
                    print()
                time.sleep(0.5)

                enemydmg = random.randint(100, 175)
                if defense >= 100:
                    enemydmg -= defense-40
                else:
                    enemydmg -= defense
                health -= enemydmg
                if enemyHealth >= 0:
                    if health <= 0:
                        health = 0
                        print("The enemy dealt", enemydmg, "damage to you!")
                        if enemydmg >= 150:
                            print("The attack was super effective!")
                        print("You have", health, "health left!")
                        print()
                        break
                    else:
                        print("The enemy dealt", enemydmg, "damage to you!")
                        if enemydmg >= 150:
                            print("The attack was super effective!")
                        print("You have", health, "health left!")
                        print()
                time.sleep(0.5)
                end = input("Press enter to continue...")
                time.sleep(0.1)
                clearOutput(16)
                if dmg >= attack+90:
                    clearOutput(1)
                if enemydmg >= 150:
                    clearOutput(1)
            
            elif choice == "2":
                if healCounter > 0:
                    heal = random.randint(75, 100)
                    health += heal
                    if health >= 1500:
                        health = 1500
                        print("You healed", heal, "health!")
                        print("You have max left!")
                        print()
                    else:
                        print("You healed", heal, "health!")
                        print("You have", health, "health left!")
                        print()
                    healCounter -= 1
                    end = input("Press enter to continue...")     
                    time.sleep(0.1)
                    clearOutput(13)           
                else:
                    print("You have no more heals left!")
                    print()
                    end = input("Press enter to continue...")
                    time.sleep(0.1)
                    clearOutput(12)
                
            elif choice == "3":
                print("You ran away!")
                health -= 500
                attack -= 15
                defense -= 15
                healCounter -= 2
                if health <= 0:
                    health = 0
                if healCounter <= 0:
                    healCounter = 0
                if attack <= 0:
                    attack = 0
                if defense <= 0:
                    defense = 0
                break
            else:  
                clearOutput(9)

    if health == 0:
        deathScreen()
    elif enemyHealth == 0:
        print("You won!")
        additionalAttack = random.randint(1, 15)
        attack += additionalAttack
        additionalDefense = random.randint(1, 10)
        defense += additionalDefense
        if defense >= 150:
            defense = 150
            additionalDefense = 0
        additionalHealth = random.randint(50, 100)
        health += additionalHealth
        if health >= 1500:
            health = 1500
            additionalHealth = 0
        additionalHealCounter = random.randint(1, 2)
        healCounter += additionalHealCounter
        if healCounter >= 10:
            healCounter = 10
            additionalHealCounter = 0
        print()
        print(f"You have gained {additionalAttack} attack, {additionalDefense} defense, {additionalHealth} health, and {additionalHealCounter} heal(s)!")
    print()
    end = input("Press enter to exit...")
