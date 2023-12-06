import os
import time

def playscreen():
    os.system('cls')
    print()
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
    print("-------------------------------------------------------- PLAY -----------------------------------------------------------------")
    print("-------------------------------------------------------- HELP -----------------------------------------------------------------")
    print("------------------------------------------------------- CREDITS -----------------------------------------------------------------")
    print("-------------------------------------------------------- QUIT -----------------------------------------------------------------")
    print()
    titleChoice = input("> ")
    if titleChoice == "PLAY" or titleChoice == "Play" or titleChoice == "play":
        os.system('cls')
    elif titleChoice == "HELP" or titleChoice == "Help" or titleChoice == "help":
        os.system('cls')
        print('''
        ██░ ██ ▓█████  ██▓     ██▓███  
        ▓██░ ██▒▓█   ▀ ▓██▒    ▓██░  ██▒
        ▒██▀▀██░▒███   ▒██░    ▓██░ ██▓▒
        ░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██▄█▓▒ ▒
        ░▓█▒░██▓░▒████▒░██████▒▒██▒ ░  ░
         ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░▒▓▒░ ░  ░
         ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░▒ ░     
         ░  ░░ ░   ░     ░ ░   ░░       
         ░  ░  ░   ░  ░    ░  ░         ''')
        print('''________________________________________________
          ''')
        print('!Use/Type "W", "S", "A", "D" to move!')
        print('!use "inspect" to inspect something!')
        print('!May you have a splendid journey!') 
        print()
        end = input("PRESS ENTER")
        playscreen()

    elif titleChoice == "CREDITS" or titleChoice == "Credits" or titleChoice == "credits":
        os.system('cls')
        print(""" ▄████▄   ██▀███  ▓█████ ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███    ██████ 
▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▒██    ▒ 
▒▓█    ▄ ▓██ ░▄█ ▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒░ ▓██▄   
▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄    ▒   ██▒
▒ ▓███▀ ░░██▓ ▒██▒░▒████▒▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒▒██████▒▒
░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
  ░  ▒     ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒  ░ ░
░          ░░   ░    ░    ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ ░  ░  ░  
░ ░         ░        ░  ░     ░  ░            ░ ░     ░           ░  
░                                                                    """)
        print('-------------------------------TOM LUMIBAO-------------------------------')
        print('-------------------------------KURT LOPEZ--------------------------------')
        print('-------------------------------CARL FILARCA------------------------------') 
        end = input("PRESS ENTER")
        playscreen()
    elif titleChoice == "QUIT" or titleChoice == "Quit" or titleChoice == "quit":
        quit()
    else:
        print("INVALID!")
        time.sleep(1)
        playscreen()
        
def deathScreen():
    print("YOU HAVE BEEN SLAINED")
    print()
    print("RESTART")
    print("EXIT GAME")
    print()
    deathChoice = input("> ")
    if deathChoice == "RESTART" or deathChoice == "Restart" or deathChoice == "restart":
        playscreen()
    elif deathChoice == "EXIT GAME" or deathChoice == "QUIT" or deathChoice == "QUIT GAME":
        quit()
    else:
        eraser1(8)
        deathScreen()

def userInput():
    global user
    user = input("> ").capitalize()
    if user.isalnum() == True:
        eraser1(1)
        return user
    else:
        print("INVALID!")
        time.sleep(1)
        eraser1(2)
        userInput()

def eraser1(numberOfLines: int):
    cursorUpOne = '\x1b[1A'
    erase = '\x1b[2K'
    for _ in range(numberOfLines):
        print(cursorUpOne + erase, end='')