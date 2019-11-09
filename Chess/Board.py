

#------TODO

#To string methods for all the classes
#flip baord method and fix working
#Start Controller method of input and output
    #increase and use board methods
#insert comments


############### START PASSING BOARD ##############

import sys
import Pieces
import Team

#Square object to form a complete board
class Square:
    color = None
    piece = None
    pr=Pieces.PeiceMkr()
    def __init__(self):
        self.color = None

    def setColor(self, nm):
        self.color = nm

    def getColor(self):
        return self.color

    def getName(self):
        temp=self.piece.res.getName()
        return temp

    def mkrPiece(self, p, team):
        self.piece = self.pr.createPiece(p,team)

    def setPiece(self,pi):
        self.piece = None
        self.piece = pi

    def getPiece(self):
        return self.piece


#Board object to act as a chess board
class Board:

    #Singleton-Pattern

    instance = None

    def __init__(self):
        if Board.instance == None:
            Board.instance=self

    @staticmethod
    def getInstance():
        if Board.instance == None:
            Board()
        return Board.instance




    #Actual Board


    #initializing primitives
    teamA = Team.Team()
    teamB = Team.Team()
    teamA.setName("PlayerA")
    teamB.setName("PlayerB")

    turnCount= 0 #---------------------------------------------------------------------------------

    #using square object to create a chess board
    brd = [[Square() for j in range(8)] for i in range(8)]

    #for loop to set colour of squares in the board
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0: brd[i][j].setColor("White")
            elif (i+j)%2 == 1: brd[i][j].setColor("Black")


    print("Board Initialized!")



    #Methods
    def getBoard(self):
        return self.brd

    def printBoard(self):
        if self.turnCount == 0:
            print("                                            ",str(self.teamA.getName()))
        elif self.turnCount == 1:
            print("                                            ",str(self.teamB.getName()))
        print("                                           --------------");

        print(" ")

        print("        1                2            3            4            5           6            7           8");
        print("   ---------------------------------------------------------------------------------------------------------")

        for i in range(8):
            sys.stdout.write(str(i+1))
            sys.stdout.write("  |")
            for j in range(8):
                sys.stdout.write(" ")

                if self.brd[i][j].getPiece() != None:
                    sys.stdout.write(self.brd[i][j].getPiece().getName())#to strng for board printing
                    sys.stdout.write(" |")
                else:
                    kg = "           |" if  self.brd[i][j].getColor() == "White"  else "           |"
                    sys.stdout.write(kg),
            print(" ")
            print(
                "   ---------------------------------------------------------------------------------------------------------")

        print(" ")
        print("                                          --------------");
        if self.turnCount == 0:
            print("                                            ",str(self.teamB.getName()))
        elif self.turnCount == 1:
            print("                                            ",str(self.teamA.getName()))


    #CHECK AND VERIFY
    def initializePieces(self):

        #Pwn
        for i in range(8):
            self.brd[1][i].mkrPiece("P", self.teamA)
            self.brd[6][i].mkrPiece("P", self.teamB)

        #Rook
        self.brd[0][0].mkrPiece("R", self.teamA)
        self.brd[0][7].mkrPiece("R", self.teamA)
        self.brd[7][0].mkrPiece("R", self.teamB)
        self.brd[7][7].mkrPiece("R", self.teamB)


        #Bishop
        self.brd[0][2].mkrPiece("B", self.teamA)
        self.brd[0][5].mkrPiece("B", self.teamA)
        self.brd[7][2].mkrPiece("B", self.teamB)
        self.brd[7][5].mkrPiece("B", self.teamB)

        #Knight
        self.brd[0][1].mkrPiece("Kn", self.teamA)
        self.brd[0][6].mkrPiece("Kn", self.teamA)
        self.brd[7][1].mkrPiece("Kn", self.teamB)
        self.brd[7][6].mkrPiece("Kn", self.teamB)

        # Rook
        self.brd[0][3].mkrPiece("Q", self.teamA)
        self.brd[7][3].mkrPiece("Q", self.teamB)

        #King
        self.brd[0][4].mkrPiece("K", self.teamA)
        self.brd[7][4].mkrPiece("K", self.teamB)


    def setTeamA(self,namea):
        self.teamA.setName(name=namea)

    def setTeamB(self,nameb):
        self.teamB.setName(name=nameb)

    def getTeam(self,ab):
        return self.teamA if ab==1 else self.teamB


    #From Point A to Point B - CHK and VERIFY
    def movePiece(self, iA,jA,iB,jB):
        p = self.brd[iB-1][jB-1].getPiece()
        self.brd[iB-1][jB-1].setPiece(self.brd[iA - 1][jA - 1].getPiece())
        self.brd[iA-1][jA-1].setPiece(None)
        return p

    def isEmptyBox(self,i,j):
        return self.brd[i][j].getPiece() == None

    def flipBoard(self):
        self.brd.reverse()
        self.turnCount = 1

    def restart(self):
        self.brd.clear()
        self.brd = [[Square() for j in range(8)] for i in range(8)]
        self.turnCount=0 #-------------------------------------------------------------------
        self.initializePieces()
        print("EVERYTHING RESTARTED!")



