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
            