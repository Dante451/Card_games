"""
War card game
Dante Daciuk
13/3/24
"""
import random 
from time import sleep
import os

value = 0
computer_value = 0

master_deck = [" 2 of ♠", " 2 of ♥", " 2 of ⯁", " 2 of ♣️",
" 3 of ♠", " 3 of ♥", " 3 of ⯁", " 3 of ♣️",
" 4 of ♠", " 4 of ♥", " 4 of ⯁", " 4 of ♣️",
" 5 of ♠", " 5 of ♥", " 5 of ⯁", " 5 of ♣️",
" 6 of ♠", " 6 of ♥", " 6 of ⯁", " 6 of ♣️",
" 7 of ♠", " 7 of ♥", " 7 of ⯁", " 7 of ♣️",
" 8 of ♠", " 8 of ♥", " 8 of ⯁", " 8 of ♣️",
" 9 of ♠", " 9 of ♥", " 9 of ⯁", " 9 of ♣️",
"10 of ♠", "10 of ♥", "10 of ⯁", "10 of ♣️",
" J of ♠", " J of ♥", " J of ⯁", " J of ♣️",
" Q of ♠", " Q of ♥", " Q of ⯁", " Q of ♣️",
" K of ♠", " K of ♥", " K of ⯁", " K of ♣️",
" A of ♠", " A of ♥", " A of ⯁", " A of ♣️"]

player_deck = []
player_won_deck = []
computer_deck = []
computer_won_deck = []

def war_intro():
    print(" __________")
    print("|          |")
    print("|   WAR    |")
    print("|          |")
    print("|  A GAME  |")
    print("| BY DANTE |")
    print("|__________|")

def reset_screen():
    sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

def shuffle():
    for x in range(1, 27):
        move_card = random.choice(master_deck)
        player_deck.append(move_card)
        master_deck.remove(move_card)
        x + 1
    for y in range(1, 27):
        move_card = random.choice(master_deck)
        computer_deck.append(move_card)
        master_deck.remove(move_card)
        y + 1

def value_check(value):
    if "2" in player_deck[0]:
        value = 1
    elif "3" in player_deck[0]:
        value = 2
    elif "4" in player_deck[0]:
        value = 3
    elif "5" in player_deck[0]:
        value = 4
    elif "6" in player_deck[0]:
        value = 5
    elif "7" in player_deck[0]:
        value = 6
    elif "8" in player_deck[0]:
        value = 7
    elif "9" in player_deck[0]:
        value = 8
    elif "10" in player_deck[0]:
        value = 9
    elif "J" in player_deck[0]:
        value = 10
    elif "Q" in player_deck[0]:
        value = 11
    elif "K" in player_deck[0]:
        value = 12
    elif "A" in player_deck[0]:
        value = 13
    return value

def computer_value_check(computer_value):
    if "2" in computer_deck[0]:
        computer_value = 1
    elif "3" in computer_deck[0]:
        computer_value = 2
    elif "4" in computer_deck[0]:
        computer_value = 3
    elif "5" in computer_deck[0]:
        computer_value = 4
    elif "6" in computer_deck[0]:
        computer_value = 5
    elif "7" in computer_deck[0]:
        computer_value = 6
    elif "8" in computer_deck[0]:
        computer_value = 7
    elif "9" in computer_deck[0]:
        computer_value = 8
    elif "10" in computer_deck[0]:
        computer_value = 9
    elif "J" in computer_deck[0]:
        computer_value = 10
    elif "Q" in computer_deck[0]:
        computer_value = 11
    elif "K" in computer_deck[0]:
        computer_value = 12
    elif "A" in computer_deck[0]:
        computer_value = 13
    return computer_value

shuffle()

print("This is the player deck: ")
print(player_deck)
print("This is the computer deck: ")
print(computer_deck)
print("This is the master deck: ")
print(master_deck)

print(value_check(player_deck))
print(computer_value_check(computer_deck))
#add an if/elif/else for the two lists.
#possibly combine effects with an or statement??