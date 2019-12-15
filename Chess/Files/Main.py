#-----TODO




#Make perfect working player to player
#Put whole game inside a loop
#Fix board printing (13 spaces per piece name inside bars)
#Lok psf rec for more

#send board sample to TA for confirmation
#Ask mitch about other things also in same email <-----------------

from time import sleep, time

import Board
import sys
import os
import Pieces
import Team
import AI as ai
import GUI as ui


def teamInput(ai):
    ta = None
    tb = None

    while True:
        try:

            ta = str(raw_input("Give a name to Player A\n"))
            break
        except:
            print "Not a valid name format"

    if ai:
        print "\nAI would be player B"
        tb = "AI"
    else:
        while True:
            try:

                tb = str(raw_input("Give a name to Player B \n"))
                break
            except:
                print "Not a valid name format"



    return ta,tb

def indexInput(txt):
    i=None
    j=None
    while i > 8 or i < 1 or j < 1 or j > 8:
        try:
            i, j = map(int, raw_input(
                "Enter indices 'i' [1-8] and 'j' [1-8] " + txt + " (seperated by a space)\n").split())

            if i > 8 or i < 1 or j < 1 or j > 8: print str(i) + "," + str(j) + " Not in valid range of 1-8"
        except:
            print "Not Integers!! Please try again!"

    return i,j


def checkWin():
    pass


b=Board.Board()
b.initializePieces()
print "---------------------------------------------------------------"

AP = 0
try:
    AP = int(raw_input("Enter number associated with a mode to play in that mode:\n0 - human-VS-human\n1 - AI-VS-human\n "
                       +"(Entering anything else will lead to player-VS-player)\n"))

except:
    print "\n---------------------------------------------------------------\nNot a valid entry but you can play human-VS-human"



if AP == 0:

    print "\n---------------------------------------------------------------\n------------------Welcome to player-VS-player mode------------------\n"
    ta,tb = teamInput(AP)

    b.setTeamA(str(ta))
    b.setTeamB(str(tb))


    while True:
        b.printBoard()

        i=None
        j=None
        i2=None
        j2=None

        moved = False
        while not moved:

            i,j = indexInput("of the piece you want to move!")
            if b.isEmptyBox(i-1, j-1):
                print "There is not piece there, Null pointer!!!\n"
                continue

            i2,j2 = indexInput("of the box you want to move to!")
            if i == i2 and j == j2:
                print "Cant move a piece where it already is!\n"
                continue

            break

        b.movePiece(i-1,j-1,i2-1,j2-1)

        b.printBoard()

        sleep(3)
        os.system("clear")
        b.flipBoard()

        win = checkWin()
        won = "Someone"
        if win:
            print "-----------------------------------------------------------"
            print won + " has just won the game"
            break


        print "-----------Board Rotated! (you are at the bottom side now)-------------------"
        b.printBoard()
        sleep(3)
        os.system("clear")

elif AP == 1:

    print "\n---------------------------------------------------------------\n------------------Welcome to AI-VS-player mode------------------\n"
    ta,tb = teamInput(AP)

    b.setTeamA(str(ta))
    b.setTeamB(str(tb))



    while True:
        b.printBoard()

        i = None
        j = None
        i2 = None
        j2 = None

        moved = False
        while not moved:
            i, j = indexInput("of the piece you want to move!")
            i2, j2 = indexInput("of the box you want to move to!")

            moved = b.movePiece(i - 1, j - 1, i2 - 1, j2 - 1)

        b.printBoard()

        sleep(3)
        os.system("clear")
        b.flipBoard()

        win = checkWin()
        won = "Someone"
        if win:
            print "-----------------------------------------------------------"
            print won + " has just won the game"
            break

        print "-----------Board Rotated! (you are at the bottom side now)-------------------"
        b.printBoard()
        sleep(3)
        os.system("clear")



