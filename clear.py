import os
import sys

def clearOutput(numberOfLines: int):
    cursorUpOne = '\x1b[1A'
    erase = '\x1b[2K'
    for _ in range(numberOfLines):
        print(cursorUpOne + erase, end='')

def deathScreen():
    print("You died!")
    print()
    print("Game over!")
    print()
    print("1. Restart")
    print("2. Quit")
    print()
    deathChoice = input("> ")
    if deathChoice == "1":
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif deathChoice == "2":
        quit()
    else:
        clearOutput(8)
        deathScreen()