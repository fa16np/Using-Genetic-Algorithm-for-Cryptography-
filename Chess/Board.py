
#To string methods for all the classes
#input of team names
#initial positions can be added
import sys
import Pieces
import Team

class Square:
    color = None
    piece = Pieces.PeiceMkr()

    def setColor(self, nm):
        self.color = nm

    def getColor(self):
        return self.color

    def setPiece(self,p,team):
        self.piece.createPiece(p,team)

    def getPiece(self):
        return self.piece.res

class Board:

    #------- Singleton-Pattern -----

    instance = None

    def __init__(self):
        if Board.instance == None:
            Board.instance=self

    @staticmethod
    def getInstance():
        if Board.instance == None:
            Board()
        return Board.instance

    #-----  Actual Board ----------


    #initializing primitives
    teamA = Team.Team()
    teamB = Team.Team()
    teamA.setName("A")
    teamB.setName("B")

    turnCount= 0

    brd = [[Square() for j in range(8)] for i in range(8)]

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
            print("                                     ",str(self.teamA.getName()))
        elif self.turnCount == 1:
            print("                                     ",str(self.teamB.getName()))
        print("                                --------------");

        print(" ")
        print("        1           2           3           4           5           6           7           8");
        for i in range(8):
            sys.stdout.write(str(i+1))
            sys.stdout.write("    ")
            for j in range(8):
                print(self.brd[i][j].getPiece())
                if self.brd[i][j].getPiece() != None:
                    sys.stdout.write(self.brd[i][j].getPiece()) #to strng for board printing
                else:
                    kg = "   0   | " if  self.brd[i][j].getColor() == "White"  else "   1   | "
                    sys.stdout.write(kg),
            print(" ")

        print(" ")
        print("                               --------------");
        if self.turnCount == 0:
            print("                                     ",str(self.teamB.getName()))
        elif self.turnCount == 1:
            print("                                     ",str(self.teamA.getName()))


    #CHECK AND VERIFY
    def initializePieces(self):

        #Pwn
        for i in range(8):
            self.brd[1][i].setPiece("P", self.teamA)
            self.brd[6][i].setPiece("P", self.teamB)

        #Rook
        self.brd[0][0].setPiece("R", self.teamA)
        self.brd[0][7].setPiece("R", self.teamB)
        self.brd[7][0].setPiece("R", self.teamA)
        self.brd[7][7].setPiece("R", self.teamB)

        #Bishop
        self.brd[0][2].setPiece("B", self.teamA)
        self.brd[0][5].setPiece("B", self.teamB)
        self.brd[7][2].setPiece("B", self.teamA)
        self.brd[7][4].setPiece("B", self.teamB)

        #Knight
        self.brd[0][1].setPiece("Kn", self.teamA)
        self.brd[0][6].setPiece("Kn", self.teamB)
        self.brd[7][1].setPiece("Kn", self.teamA)
        self.brd[7][6].setPiece("Kn", self.teamB)

        # Rook
        self.brd[0][3].setPiece("Q", self.teamA)
        self.brd[7][3].setPiece("Q", self.teamB)

        #King
        self.brd[0][4].setPiece("K", self.teamA)
        self.brd[7][4].setPiece("K", self.teamB)

    def setTeamA(self,namea):
        self.teamA.setName(name=namea)

    def setTeamB(self,nameb):
        self.teamB.setName(name=nameb)

    def getTeam(self,ab):
        return self.teamA if ab==1 else self.teamB


    #From Point A to Point B
    def movePiece(self, iA,jA,iB,jB):
        p = self.brd[iB][jB].getPiece()
        self.brd[iB][jB].setPiece(self.brd[iA][jA].getPiece())
        self.brd[iA][jA].setPiece(None)
        return p
#
# bd =  Board()
# bd.initializePieces()
# bd.printBoard()
