print("Welcome to the Slot Machine!")
numberOfTimes = input('How many times do you want to play?')
creditsplayed = float(raw_input('How many credits would you like to bet?'))
slotsPossible = ["bar","bar","bar","cherry","crown","crown"]
from random import *
def play():
    slot1=choice(slotsPossible)
    slot2=choice(slotsPossible)
    slot3=choice(slotsPossible)
    win = ""
    if (slot1==slot2==slot3=="cherry"):
        win = "\nYou win $%d, WooHoo" % (creditsplayed * 10)
    if (slot1==slot2==slot3=="crown"):
        win = "\nYou win $%d" % (creditsplayed * 5)
    if (slot1==slot2==slot3=="bar"):
        win = "\nYou win $%d, not too bad." % (creditsplayed * 2)
    return slot1+":"+slot2+":"+slot3+" "+win
for i in range(int(numberOfTimes)):
    print(play())
