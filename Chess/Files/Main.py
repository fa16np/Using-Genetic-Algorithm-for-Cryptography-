#-----TODO
#Connect GUI also
#Then act this as a tunnel between Board, AI and GUI


#Make perfect working player to player
from time import sleep, time

import Board
import sys
import Pieces
import Team
import AI as ai
import GUI as ui



b=Board.Board()
b.initializePieces()
ta,tb = "", ""

# try:
#
#     ta= raw_input("Give a name to Team A\n")
#
# except NameError: pass
#
# try:
#
#     tb= raw_input("Give a name to Team B\n")
#
# except NameError: pass
#
#
#
# print(ta,tb)
# b.setTeamA(str(ta))
# print b.teamA.getName()
# b.setTeamB(str(tb))


#check if there is a piece actually or not on both places
b.movePiece(1,2,2,2)



# b.flipBoard()
b.printBoard()

sleep(50000)

# print(b.getTeam(1).getName())
# print(b.getTeam(0).getName())
