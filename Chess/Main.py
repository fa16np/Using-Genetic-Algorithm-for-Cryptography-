#-----TODO
#Connect GUI also
#Then act this as a tunnel between Board, AI and GUI


import Board
import sys
import Pieces
import Team



b=Board.Board()
b.initializePieces()
ta,tb = "", ""

try:

    ta= input("Give a name to Team A")

except NameError: pass

try:

    tb= input("Give a name to Team B")

except NameError: pass

print(ta,tb)
b.setTeamA(str(ta))
b.setTeamB(str(tb))
b.printBoard()
# b.flipBoard()
# b.printBoard()
# print(b.getTeam(1).getName())
# print(b.getTeam(0).getName())
