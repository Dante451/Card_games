"""
War card game
Dante Daciuk
13/3/24
"""
import random 
from time import sleep
import os

print(" __________")
print("|          |")
print("|    WAR   |")
print("|          |")
print("|  A GAME  |")
print("| BY DANTE |")
print("|__________|")

def reset_screen():
    sleep(3)
    os.system("cls" if os.name == "nt" else "clear")

def deal_cards():
    print("Text")

master_deck = [" 1 of ♠", " 1 of ♥", " 1 of ⯁", " 1 of ♣️",
" 2 of ♠", " 2 of ♥", " 2 of ⯁", " 2 of ♣️",
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
computer_deck = []

for x in range(1, 29):
    move_card = random.choice(master_deck)
    player_deck.append(move_card)
    master_deck.remove(move_card)
    x + 1
for y in range(1, 29):
    move_card = random.choice(master_deck)
    computer_deck.append(move_card)
    master_deck.remove(move_card)
    y + 1
    
print("This is the player deck: ")
print(player_deck)
print("This is the computer deck: ")
print(computer_deck)
print("This is the master deck: ")
print(master_deck)