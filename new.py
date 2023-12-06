# rpg group 1
import cmd
import os
import textwrap
import sys
import time
import random

from generator import make_maze
from setting import setup_game
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
setup_game()
