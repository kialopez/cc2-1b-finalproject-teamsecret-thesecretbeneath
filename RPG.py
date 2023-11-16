# rpg group 1
import cmd
import os
import textwrap
import sys
import time
import random

screen_width = 100

# player #
class Player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 100
        self.mp = 100
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False
myPlayer = Player()

# title screen #
def title_screen_selection():
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("please enter a valid command.")
        option = input("> ")
        if option.lower() == "play":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()

def title_screen():
    os.system = ('cls')
    print('*********************************')
    print('* Welcome To The Secret Beneath *')
    print('*********************************')
    print('             - Play -            ')
    print('             - Help -            ')
    print('             - Quit -            ')
    print('    Copyright 2023 Team Secret   ')
    title_screen_selection()

def help_menu():
    print('*********************************')
    print('* Welcome To The Secret Beneath *')
    print('*********************************')
    print('!Use up, down, left right to move!')
    print('!type commands to Do them!')
    print('!use "inspect" to inspect something!')
    print('!May you have a splendid journey!')
    title_screen_selection()

# Map #
Zonename = ''
Description = 'description'
Examination = 'examine'
Solved = False
Up = 'up', 'north'
Down = 'down', 'south'
Left = 'left', 'west'
Right = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False,
                 }

ZoneMap = {
    'a1': {
        Zonename: "Labrinth Entrance",
        Description: 'The start of Every journey Takes place at very hall',
        Examination: 'Two Large statues at the side of the entrance ominously tower over you',
        Solved: False,
        Up: '',
        Down: '',
        Left: '',
        Right: 'a2',
    },
    'a2': {
        Zonename: "Empty Room",
        Description: 'An eerie empty room...',
        Examination: 'For a labyrinth, you would expect something more chaotic, but it\'s seemingly empty',
        Solved: False,
        Up: '',
        Down: 'b2',
        Left: 'a1',
        Right: 'a3',
    },
    'a3': {
        Zonename: "Treasure!",
        Description: 'A room filled with treasures and artifacts greet you with a sole chest in the middle',
        Examination: 'Not like the last room, this room shines the light of LOOT!, but you still can\'t shake the eerie feeling',
        Solved: False,
        Up: '',
        Down: '',
        Left: 'a2',
        Right: '',
    },
    'a4': {
        Zonename: "Strong Hold",
        Description: 'An old village, ghastly village with no one in sight',
        Examination: 'As you look around, you find adventurers like yourself',
        Solved: False,
        Up: '',
        Down: 'b4',
        Left: '',
        Right: ''
    },
    'b1': {
        Zonename: "Cross",
        Description: 'A cross stands straight in the middle of the dark room, seemingly glowing',
        Examination: 'All of your instincts tell you to RUN...',
        Solved: False,
        Up: '',
        Down: 'c1',
        Left: '',
        Right: '',
    },
    'b2': {
        Zonename: "Contemplation",
        Description: 'Lush green plains greet you, with the warmth of the bright sun',
        Examination: 'You see people at last; they are gathering at the center',
        Solved: False,
        Up: 'a2',
        Down: 'c2',
        Left: '',
        Right: 'b3',
    },
}

# interactivity #
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + ZoneMap[myPlayer.location][Description] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("\n" + "===============================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_action = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'look']
    while action.lower() not in acceptable_action:
        print("Unknown action. Try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = ZoneMap[myPlayer.location][Up]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = ZoneMap[myPlayer.location][Left]
        movement_handler(destination)
    elif dest in ['east', 'right']:
        destination = ZoneMap[myPlayer.location][Right]
        movement_handler(destination)
    elif dest in ['south', 'down']:
        destination = ZoneMap[myPlayer.location][Down]
        movement_handler(destination)

def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if ZoneMap[myPlayer.location][Solved]:
        print("You have cleared the area")
    else:
        print("There are things still hidden")

# Game function #
def main_game_loop():
    prompt()
    # here handle if puzzles have been solved, enemies defeated, explored everything.

def setup_game():
    # Job Handling ...
    question1 = "Hello, what is your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    question2 = "What are you?\nA warrior, priest, or mage?"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are a " + player_job + " Splendid!\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are a " + player_job + " Splendid!\n")
    # player stats #
    if myPlayer.job == 'warrior':
        myPlayer.hp = 120
        myPlayer.mp = 40
    elif myPlayer.job == 'mage':
        myPlayer.hp = 60
        myPlayer.mp = 100
    elif myPlayer.job == 'priest':
        myPlayer.hp = 80
        myPlayer.mp = 80

    # introduction #
    question3 = "Welcome! " + player_name + " the " + player_job + "." + "Are you ready to begin your adventure?\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = "Welcome to the Labrynth!\n"
    speech2 = "This is where fame and fortune await the brave\n"
    speech3 = "The labrynth which takes the lives of the foolish\n"
    speech4 = "Which one are you, I wonder?\n"
    speech5 = "Don't die...\n"

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    os.system('cls')
    print("######################")
    print("# Let's start adventuring! #")
    print("######################")
    main_game_loop()       
 
title_screen()