from display import deathScreen, eraser1
from maps import map1, map2, map3
import random
import time
import os

hp = random.randint(500, 1000)
damage = random.randint(90, 100)
defense = random.randint(5, 15)
hppotion = (3)
randomEnemyCounter = 0

def enemyFight():
    enhp = random.randint(250, 500)
    criticalHit = 0
    global hp
    global hppotion
    global damage
    global defense

    while hp > 0:
        if hp >= 0:
            print(f"YOUR STATS:")
            print(f"DAMAGE: {damage}")
            print(f"SHIELD: {defense}")
            print(f"HP: {hp}")
            print(f"---------------")
            print(f"ENEMY HP: {enhp}")
            print()
            print("CHOOSE YOUR MOVE")
            print("ATTACK")
            print(f"HEAL ({hppotion} LEFT)")
            print("ESCAPE")
            print()
            choice = input("MOVE:")
            print()
            time.sleep(0.5)

            if choice == "ATTACK" or choice == "Attack" or choice == "damage" or choice == "attack": 
                dmg = random.randint(damage, damage+125)
                enhp -= dmg
                if enhp <= 0:
                    enhp = 0
                    if dmg >= damage+90:
                        print("HIT!")
                        criticalHit += 1
                    print(dmg, "DAMAGE DEALTH!")
                    print(enhp, "ENEMY HP LEFT!")
                    print()
                    break
                else:
                    if dmg >= damage+90:
                        print("HIT!")
                    print(dmg, "DAMAGE DEALTH!")
                    print(enhp, "ENEMY HP LEFT!")
                    print()
                time.sleep(0.5)

                enemydmg = random.randint(100, 175)
                if defense >= 100:
                    enemydmg -= defense-40
                else:
                    enemydmg -= defense
                hp -= enemydmg
                if enhp >= 0:
                    if hp <= 0:
                        hp = 0
                        print("YOU HAVE BEEN HIT WITH", enemydmg, "DAMAGE!")
                        if enemydmg >= 150:
                            print("YOU ARE HURT!")
                        print(hp, "HP REMAINING!")
                        print()
                        break
                    else:
                        print("YOU HAVE BEEN HIT WITH", enemydmg, "DAMAGE!")
                        if enemydmg >= 150:
                            print("YOU ARE HURT!")
                        print(hp, "HP REMAINING!")
                        print()
                time.sleep(0.5)
                end = input("PRESS ENTER")
                time.sleep(0.1)
                eraser1(16)
                if dmg >= damage+90:
                    eraser1(1)
                if enemydmg >= 150:
                    eraser1(1)
            
            elif choice == "HEAL" or choice == "Heal" or choice == "heal":
                if hppotion > 0:
                    heal = random.randint(75, 100)
                    hp += heal
                    if hp >= 1000:
                        hp = 1000
                        print("RECOVERED", heal, "HP!")
                        print("HP IS FULL!")
                        print()
                    else:
                        print("RECOVERED", heal, "HP!")
                        print(hp, "HP REMAINING")
                        print()
                    hppotion -= 1
                    end = input("PRESS ENTER")
                    time.sleep(0.1)
                    eraser1(13)           
                else:
                    print("OUT OF HEALING POTIONS!")
                    print()
                    end = input("PRESS ENTER")
                    time.sleep(0.1)
                    eraser1(12)
                
            elif choice == "ESC" or choice == "Esc" or choice == "esc" or choice == "ESCAPE" or choice == "Escape" or choice == "escape":
                print("ESCAPED!")
                hp -= 500
                damage -= 15
                defense -= 15
                hppotion -= 2
                if hp <= 0:
                    hp = 0
                if hppotion <= 0:
                    hppotion = 0
                if damage <= 0:
                    damage = 0
                if defense <= 0:
                    defense = 0
                break
            else:  
                eraser1(9)

    if hp == 0:
        deathScreen()
    elif enhp == 0:
        print("ENEMY KILLED!")
        additionalAttack = random.randint(1, 15)
        damage += additionalAttack
        additionalDefense = random.randint(1, 10)
        defense += additionalDefense
        if defense >= 150:
            defense = 150
            additionalDefense = 0
        additionalhp = random.randint(50, 100)
        hp += additionalhp
        if hp >= 1000:
            hp = 1000
            additionalhp = 0
        additionalhppotion = random.randint(1, 2)
        hppotion += additionalhppotion
        if hppotion >= 10:
            hppotion = 10
            additionalhppotion = 0
        print()
    end = input("PRESS ENTER")

def randomEnemy():
    global randomEnemyCounter
    randomEnemyCounter += random.randint(1, 15)
    if randomEnemyCounter >= 26:
        enemy = random.randint(1, 2)
        if enemy == 1:
            print("A VAMPIRE APPEARED!")
        elif enemy == 2:
            print("A WEREWOLF APPEARED!")
        print()
        enemyFight()
        os.system('cls')
        randomEnemyCounter = random.randint(1, 10)
        print("""
▄▄▄█████▓ ██░ ██ ▓█████      ██████ ▓█████  ▄████▄   ██▀███  ▓█████▄▄▄█████▓    ▄▄▄▄   ▓█████  ███▄    █ ▓█████ ▄▄▄     ▄▄▄█████▓ ██░ ██ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀▓  ██▒ ▓▒   ▓█████▄ ▓█   ▀  ██ ▀█   █ ▓█   ▀▒████▄   ▓  ██▒ ▓▒▓██░ ██▒
▒ ▓██░ ▒░▒██▀▀██░▒███      ░ ▓██▄   ▒███   ▒▓█    ▄ ▓██ ░▄█ ▒▒███  ▒ ▓██░ ▒░   ▒██▒ ▄██▒███   ▓██  ▀█ ██▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄      ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄░ ▓██▓ ░    ▒██░█▀  ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██████▒▒░▒████▒▒ ▓███▀ ░░██▓ ▒██▒░▒████▒ ▒██▒ ░    ░▓█  ▀█▓░▒████▒▒██░   ▓██░░▒████▒▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒ ░░      ░▒▓███▀▒░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒
    ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░▒  ░ ░ ░ ░  ░  ░  ▒     ░▒ ░ ▒░ ░ ░  ░   ░       ▒░▒   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░ ▒   ▒▒ ░   ░     ▒ ░▒░ ░
  ░       ░  ░░ ░   ░      ░  ░  ░     ░   ░          ░░   ░    ░    ░          ░    ░    ░      ░   ░ ░    ░    ░   ▒    ░       ░  ░░ ░
          ░  ░  ░   ░  ░         ░     ░  ░░ ░         ░        ░  ░            ░         ░  ░         ░    ░  ░     ░  ░         ░  ░  ░
                                           ░                                         ░                                                   """)
        print()

def mazexe():
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

    mazeFile = random.choice([map1, map2, map3])
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
        print("""
▄▄▄█████▓ ██░ ██ ▓█████      ██████ ▓█████  ▄████▄   ██▀███  ▓█████▄▄▄█████▓    ▄▄▄▄   ▓█████  ███▄    █ ▓█████ ▄▄▄     ▄▄▄█████▓ ██░ ██ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀▓  ██▒ ▓▒   ▓█████▄ ▓█   ▀  ██ ▀█   █ ▓█   ▀▒████▄   ▓  ██▒ ▓▒▓██░ ██▒
▒ ▓██░ ▒░▒██▀▀██░▒███      ░ ▓██▄   ▒███   ▒▓█    ▄ ▓██ ░▄█ ▒▒███  ▒ ▓██░ ▒░   ▒██▒ ▄██▒███   ▓██  ▀█ ██▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄      ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄░ ▓██▓ ░    ▒██░█▀  ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██████▒▒░▒████▒▒ ▓███▀ ░░██▓ ▒██▒░▒████▒ ▒██▒ ░    ░▓█  ▀█▓░▒████▒▒██░   ▓██░░▒████▒▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒ ░░      ░▒▓███▀▒░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒
    ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░▒  ░ ░ ░ ░  ░  ░  ▒     ░▒ ░ ▒░ ░ ░  ░   ░       ▒░▒   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░ ▒   ▒▒ ░   ░     ▒ ░▒░ ░
  ░       ░  ░░ ░   ░      ░  ░  ░     ░   ░          ░░   ░    ░    ░          ░    ░    ░      ░   ░ ░    ░    ░   ▒    ░       ░  ░░ ░
          ░  ░  ░   ░  ░         ░     ░  ░░ ░         ░        ░  ░            ░         ░  ░         ░    ░  ░     ░  ░         ░  ░  ░
                                           ░                                         ░                                                   """)
        print()
        displayMaze(maze)
        print()
        while True:
            print('W = UP, A = LEFT, S = DOWN, D = RIGHT')
            move = input('> ').upper()

            if move not in ['W', 'A', 'S', 'D']:
                print('INVALID!')
                eraser1(4)
                continue

            if move == 'W' and maze[(playerx, playery - 1)] == EMPTY:
                break
            elif move == 'S' and maze[(playerx, playery + 1)] == EMPTY:
                break
            elif move == 'A' and maze[(playerx - 1, playery)] == EMPTY:
                break
            elif move == 'D' and maze[(playerx + 1, playery)] == EMPTY:
                break

            print('YOU ARE BLOCKED!')
            eraser1(4)
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
            print("""
▄▄▄█████▓ ██░ ██ ▓█████      ██████ ▓█████  ▄████▄   ██▀███  ▓█████▄▄▄█████▓    ▄▄▄▄   ▓█████  ███▄    █ ▓█████ ▄▄▄     ▄▄▄█████▓ ██░ ██ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀▓  ██▒ ▓▒   ▓█████▄ ▓█   ▀  ██ ▀█   █ ▓█   ▀▒████▄   ▓  ██▒ ▓▒▓██░ ██▒
▒ ▓██░ ▒░▒██▀▀██░▒███      ░ ▓██▄   ▒███   ▒▓█    ▄ ▓██ ░▄█ ▒▒███  ▒ ▓██░ ▒░   ▒██▒ ▄██▒███   ▓██  ▀█ ██▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄      ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄░ ▓██▓ ░    ▒██░█▀  ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██████▒▒░▒████▒▒ ▓███▀ ░░██▓ ▒██▒░▒████▒ ▒██▒ ░    ░▓█  ▀█▓░▒████▒▒██░   ▓██░░▒████▒▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒ ░░      ░▒▓███▀▒░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒
    ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░▒  ░ ░ ░ ░  ░  ░  ▒     ░▒ ░ ▒░ ░ ░  ░   ░       ▒░▒   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░ ▒   ▒▒ ░   ░     ▒ ░▒░ ░
  ░       ░  ░░ ░   ░      ░  ░  ░     ░   ░          ░░   ░    ░    ░          ░    ░    ░      ░   ░ ░    ░    ░   ▒    ░       ░  ░░ ░
          ░  ░  ░   ░  ░         ░     ░  ░░ ░         ░        ░  ░            ░         ░  ░         ░    ░  ░     ░  ░         ░  ░  ░
                                           ░                                         ░                                                   """)
            print()
            play = False
