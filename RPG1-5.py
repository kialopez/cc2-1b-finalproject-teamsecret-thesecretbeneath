# rpg group 1
import cmd
import os
import textwrap
import sys
import time
import random

from generator import make_maze

screen_width = 100

# player #
class player:
    def __init__(self):
         self.name = ''
         self.job = ''
         self.hp = 0
         self.mp = 0
         self.status_effects =[]
         self.location = 'a1'
         self.game_over = False
myPlayer = player()

#TITLE SCREEN
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        os.system('cls')
        setup_game()# place holder until written
    elif option.lower() == ("help"):
        os.system('cls')
        help_menu()
    elif option.lower() == ("credit"):
        os.system('cls')
        credit_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid comand")
        option = input("> ")
        if option.lower() == ("play"):
            os.system('cls')
            setup_game()# placeholder until written
        elif option.lower() == ("help"):
            os.system('cls')
            help_menu()
        elif option.lower() == ("credit"):
            os.system('cls')
            credit_menu()
        elif option.lower() == ("quit"):
            sys.exit()
    
        
def title_screen():
    print('_________________________________________________________________________________________________________________________________________')
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
    print('''_________________________________________________________________________________________________________________________________________
          ''')
    print('                                                                   - Play -                                                                ')
    print('                                                                   - Help -                                                                ')
    print('                                                                   - Quit -                                                                ')
    print('                                                                  - Credit -                                                               ')
    print('                                                          Copyright 2023 Team Secret                                                       ')
    print('_________________________________________________________________________________________________________________________________________')
    title_screen_selections()
    
def help_menu():
    print('________________________________________________')
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
    print('!Use/Type "up", "down", "left", "right" to move!')
    print('!use "inspect" to inspect something!')
    print('!May you have a splendid journey!')
    print('''________________________________________________
          ''')
    print('                    - Play -                    ')
    print('                    - Help -                    ')
    print('                    - Quit -                    ')
    print('                   - Credit -                   ')
    print('________________________________________________')
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
    print('_________________________________________________________________________')
    print('                                - Play -                                 ')
    print('                                - Help -                                 ')
    print('                                - Quit -                                 ')
    print('                               - Credit -                                ')
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
MAZE = """"""
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
        MAZE : """
       ,-----.
       |Start|
       |  X  |
       `--+--'
          |
          |
          V
         +-+               +-+           +-+          +-+         
         | |->             | |->       <-| |->      <-| |       
         +-+               +-+           +-+          +-+       
                            |                                  
                            V                          A       
                                                       |
         +-+               +-+           +-+          +-+            
         | |->             | |->       <-| |->        | |            
         +-+               +-+           +-+          +-+            
                                          |           
          A                 A             V                     
          |                 |                                         
         +-+               +-+           +-+          +-+ 
         | |->           <-| |->         | |->        | | 
         +-+               +-+           +-+          +-+ 
          |                                            |
          V                                            V                                                                                             
,----.   +-+                                          +-+                 
|Exit| <-| |                                        <-| |          
`----'   +-+                                          +-+""",
        DESCRIPTION: 'Place holder for description',
        EXAMINATION: 'Place holder for examination',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'a2',
        LEFT: 'a1',
        RIGHT:'a1',
    },
    'a2': {
        ZONENAME: "Empty Room",
        MAZE : """,-----.
       |Start|
       |     |
       `--+--'
          |
          |
          V
         +-+               +-+           +-+          +-+         
         |X|->             | |->       <-| |->      <-| |       
         +-+               +-+           +-+          +-+       
                            |                                  
                            V                          A       
                                                       |
         +-+               +-+           +-+          +-+            
         | |->             | |->       <-| |->        | |            
         +-+               +-+           +-+          +-+            
                                          |           
          A                 A             V                     
          |                 |                                         
         +-+               +-+           +-+          +-+ 
         | |->           <-| |->         | |->        | | 
         +-+               +-+           +-+          +-+ 
          |                                            |
          V                                            V                                                                                             
,----.   +-+                                          +-+                 
|Exit| <-| |                                        <-| |          
`----'   +-+                                          +-+""",
        DESCRIPTION: 'Place holder for description',
        EXAMINATION: 'Place holder for examination',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'a2',
        LEFT: 'a2',
        RIGHT:'a3',
    },
    'a3': {
        ZONENAME: "Treasure!",
        MAZE : """,-----.
       |Start|
       |     |
       `--+--'
          |
          |
          V
         +-+               +-+           +-+          +-+         
         | |->             |X|->       <-| |->      <-| |       
         +-+               +-+           +-+          +-+       
                            |                                  
                            V                          A       
                                                       |
         +-+               +-+           +-+          +-+            
         | |->             | |->       <-| |->        | |            
         +-+               +-+           +-+          +-+            
                                          |           
          A                 A             V                     
          |                 |                                         
         +-+               +-+           +-+          +-+ 
         | |->           <-| |->         | |->        | | 
         +-+               +-+           +-+          +-+ 
          |                                            |
          V                                            V                                                                                             
,----.   +-+                                          +-+                 
|Exit| <-| |                                        <-| |          
`----'   +-+                                          +-+""",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'b3',
        LEFT: 'a3',
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
    print('\n' + ('' * (4 + len(myPlayer.location))))
    print(' ' + myPlayer.location.upper() + ' ')
    print(' ' + zonemap[myPlayer.location] [ZONENAME] + ' ')
    print(' ' + zonemap[myPlayer.location] [DESCRIPTION] + ' ')
    print(' ' + zonemap[myPlayer.location] [EXAMINATION] + ' ')
    print('\n' + ('' * (4 + len(myPlayer.location))))
    
def prompt():
    print("\n" + "========================")
    print("what would you like to do---'move', 'quit', 'inspect'")
    action = input("> ")
    acceptable_actions = ['move', 'quit', 'inspect']
    while action.lower() not in acceptable_actions:
        print("Unknow action, Try again.\n")
        action = input("> ")
    if action.lower == 'quit':
        sys.exit()
    elif action.lower() in ['move']:
        player_move(action.lower())
    elif action.lower() in ['inspect']:
        player_examine(action.lower())
        
def player_move(myAction):
    ask = "Where would you like to move to?\n"
    print("Type up, down, left, right. or north, west, east, south")
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        os.system('cls')
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        os.system('cls')
        movement_handler(destination)
    elif dest in ['east', 'right']:
        destination = zonemap[myPlayer.location][RIGHT]
        os.system('cls')
        movement_handler(destination)
    elif dest in ['south', 'down']:
        destination = zonemap[myPlayer.location][DOWN]
        os.system('cls')
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
        if myPlayer.location == "a1":
            print('\n' + ('' * (4 + len(myPlayer.location))))
            print(' ' + myPlayer.location.upper() + ' ')
            print(' ' + zonemap[myPlayer.location] [ZONENAME] + ' ')
            print(' ' + zonemap[myPlayer.location] [DESCRIPTION] + ' ')
            print(' ' + zonemap[myPlayer.location] [EXAMINATION] + ' ')
            print('\n' + ('' * (4 + len(myPlayer.location))))
            prompt()
        else:
            prompt()
    #here handle if puzzle solve, boss defeated, or explore everything etc.

    
def setup_game():
    #Name collection
    question1 = "hello, what is your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    player_name = input("> ")
    if len(player_name) < 1:
        print("Enter a valid name!")
        setup_game()
    else:    
        myPlayer.name = player_name
        os.system('cls')
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
        time.sleep(0.02)
    player_job = input("> ")
    myPlayer.job = player_job
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower in valid_jobs:
        myPlayer.job = player_job
        print("You are a " + player_job + " i see...\n")
    while player_job.lower() not in valid_jobs:
        print("Enter A valid Class!")
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
        time.sleep(0.02)
    myPlayer.name = player_name
    os.system('cls')

    speech0 = "You wake up from your nap at the back of the caravan being pulled by two horses."
    speech1 = " As you look around you see a pile of gear made out of steel and leather.\n"
    speech2 = "The gear has seen combat with wear and tear all over.\n"
    speech3 = "Then you remember it is yours.\n"
    speech4 = "The caravan suddenly stoped and you hear an old man shouting 'Wake up! Wake up! Now pay me and get out!'\n"
    speech5 = "As you step out of the caravan, your eyes widen as you see a huge tower stand before you, made out of brown stone-like material and covered with overgrown vines.\n"
    speech6 = "You stand at the foot of the tower in awe.\n"
    speech7 = "Two giant statues guard the entrance of the tower made out of granite and a red crystal for the eyes, they look like warriors that have seen many horrors and conquered them.\n"
    speech8 = "You remember your goal, and why you came here, for it is said if you get to the very top you will be granted a wish.\n"
    speech9 = "Your resolve stands firm as you enter the tower.\n"
    for character in speech0:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    os.system('cls')
        
    print("============================================================")
    print("""
          
  ██████ ▄▄▄█████▓ ▄▄▄       ██▀███  ▄▄▄█████▓ ▐██▌
▒██    ▒ ▓  ██▒ ▓▒▒████▄    ▓██ ▒ ██▒▓  ██▒ ▓▒ ▐██▌
░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▓██ ░▄█ ▒▒ ▓██░ ▒░ ▐██▌
  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒██▀▀█▄  ░ ▓██▓ ░  ▓██▒
▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░██▓ ▒██▒  ▒██▒ ░  ▒▄▄ 
▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ▒▓ ░▒▓░  ▒ ░░    ░▀▀▒
░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░▒ ░ ▒░    ░     ░  ░
░  ░  ░    ░        ░   ▒     ░░   ░   ░          ░
      ░                 ░  ░   ░               ░   """)
    print("============================================================")
    print("You are at 'X'")
    
    make_maze()
    main_game_loop()

        
        
    
    


title_screen()