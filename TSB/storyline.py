import os
import sys
import time

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

def setup_game():

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
            
            

    if myPlayer.job == 'warrior':
        myPlayer.hp = 120
        myPlayer.mp = 20
    elif myPlayer.job == 'mage':
        myPlayer.hp = 40
        myPlayer.mp = 120
    elif myPlayer.job == 'priest':
        myPlayer.hp = 60
        myPlayer.mp = 60
        
    

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
