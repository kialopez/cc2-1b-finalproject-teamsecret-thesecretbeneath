# rpg group 1
import cmd
import os
import textwrap
import sys
import time
import random

screen_width = 100

# player #
class player:
    def __init__(self):
         self.name = ''
         self.job = ''
         self.hp = 0
         self.mp = 0
         self.status_effects =[]
         self.location = 'b2'
         self.game_over = False
myPlayer = player()

#TITLE SCREEN
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()# place holder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("credit"):
        credit_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid comand")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()# placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()
        
def title_screen():
    os.system('clear')
    print('_____________________________________')
    print('* Welcome To The Secret Beneath *')
    print('A TEXT BASED ASCII ADVENTURE RPG GAME')
    print('_____________________________________')
    print('             - Play -            ')
    print('             - Help -            ')
    print('             - Quit -            ')
    print('            - Credit -            ')
    print('    Copyright 2023 Team Secret   ')
    title_screen_selections()
    
def help_menu():
    print('*********************************')
    print('* Welcome To The Secret Beneath *')
    print('*********************************')
    print('!Use/Type "up", "down", "left", "right" to move!')
    print('!use "inspect" to inspect something!')
    print('!May you have a splendid journey!')
    title_screen_selections()

def credit_menu():
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
    title_screen_selections()
    
# Game functionality
def start_game():
    
    
####MAP#####
    """
a1 a2... #player starts at b2
-------------
|  |  |  |  | a4
-------------
|  | x|  |  | b4...
-------------
|  |  |  |  |
-------------
|  |  |  |  |
-------------
"""
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT ='right', 'east'

solved_places = {'a1':False, 'a2':False, 'a3':False, 'a4':False,
                'b1':False, 'b2':False, 'b3':False, 'b4':False,
                'c1':False, 'c2':False, 'c3':False, 'c4':False,
                'd1':False, 'd2':False, 'd3':False, 'd4':False,
                }

zonemap = {
    'a1': {
        ZONENAME: "Damned",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT:'a2',
    },
    'a2': {
        ZONENAME: "Empty Room",
        DESCRIPTION: 'description',
        EXAMINATION: 'dildo',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT:'a3',
    },
    'a3': {
        ZONENAME: "Treasure!",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT:'a4',
    },
    'a4': {
        ZONENAME: "Strong Hold",
        DESCRIPTION:  'description',
        EXAMINATION:  'examine',
        SOLVED:  False,
        UP:  '',
        DOWN:  'b4',
        LEFT:  'a3',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: "Cross",
        DESCRIPTION:  'description',
        EXAMINATION:  'examine',
        SOLVED:  False,
        UP:  'a1',
        DOWN:  'c1',
        LEFT:  '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: "Labrinth Entrance", #player starting point
        DESCRIPTION:  'The start of Every journey Takes place at very hall',
        EXAMINATION:  'Two Large statue at the side of the entrance ominously tower over you',
        SOLVED:  False,
        UP:  'a2',
        DOWN:  'c2',
        LEFT:  'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: "Hell",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT:'b4',
    },
    'b4': {
        ZONENAME: "Contemplation",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT:'',
    },
    'c1': {
        ZONENAME: "Sundering earth",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b1',
        DOWN: 'd1',
        LEFT: '',
        RIGHT:'c2',
    },
    'c2': {
        ZONENAME: "The Sleeping Horror",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT:'c3',
    },
    'c3': {
        ZONENAME: "The Workshop",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT:'c4',
    },
    'c4': {
        ZONENAME: "Son of Ice",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT:'',
    },
    'd1': {
        ZONENAME: "King Maker",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c1',
        DOWN: '',
        LEFT: '',
        RIGHT:'d2',
    },
    'd2': {
        ZONENAME: "Devistation",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c2',
        DOWN: '',
        LEFT: 'd1',
        RIGHT:'d3',
    },
    'd3': {
        ZONENAME: "Ruined Kingdom",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c3',
        DOWN: '',
        LEFT: 'd2',
        RIGHT:'d4',
    },
    'd4': {
        ZONENAME: "The Last battle",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP :'c4',
        DOWN: '',
        LEFT: 'd3',
        RIGHT:'',
    },
    
}

# Game interactivity
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location] [ZONENAME] + ' #')
    print('# ' + zonemap[myPlayer.location] [DESCRIPTION] + ' #')
    print('# ' + zonemap[myPlayer.location] [EXAMINATION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    
def prompt():
    print("\n" + "========================")
    print("what would you like to do")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'look',]
    while action.lower() not in acceptable_actions:
        print("Unknow action, Try again.\n")
        action = input("> ")
    if action.lower == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'look']:
        player_examine(action.lower())
        
def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['east', 'right']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['south', 'down']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
            
def movement_handler(destination):
    print("\n" + "You have moved to " + destination + ".")
    myPlayer.location = destination
    print_location()
    
def player_examine(action):
    if zonemap[myPlayer.location][SOLVED] == True:
        print("You are finished here.. move on...")
    else:
        print("There is still something to explore in here.")

# Game Functionality

def main_game_loop():
    while myPlayer.game_over == False:
        prompt()
    #here handle if puzzle solve, boss defeated, or explore everything etc.
    
def setup_game():
    os.system('clear')
    #Name collection
    question1 = "hello, what is your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name
    #JOB HANDLING
    question2 = "What do you want to be?\n"
    question2added = "(You can play as a warrior, mage, or priest)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_job = input("> ")
    myPlayer.job = player_job
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower in valid_jobs:
        myPlayer.job = player_job
        print("You are a " + player_job + "i see...\n")
    while player_job.lower() not in valid_jobs:
        player_job = input ("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are a " + player_job + "i see...\n")
            
    ##Player stats
    if myPlayer.job == 'warrior':
        myPlayer.hp = 120
        myPlayer.mp = 20
    elif myPlayer.job == 'mage':
        myPlayer.hp = 40
        myPlayer.mp = 120
    elif myPlayer.job == 'priest':
        myPlayer.hp = 60
        myPlayer.mp = 60
        
    
    #Introduction
    question3 = "Welcome! " + player_name + " the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    myPlayer.name = player_name
    
    speech1 = "Welcome To the Labrynth!\n"
    speech2 = "This is where fame and fortune awaits the brave\n"
    speech3 = "The labrynth which takes the lives of the foolish\n"
    speech4 = "which one are you i wonder?\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
        
    os.system('clear')
    print('########################')
    print('#     Let us Start!    #')
    print('########################')
    main_game_loop()

        
        
    
    


title_screen()