# ------TODO


# insert comments




import sys
import Pieces
import Team


# Square object to form a complete board
class Square:
    color = None
    piece = None
    pr = Pieces.PeiceMkr()

    def __init__(self):
        self.color = None

    def setColor(self, nm):
        self.color = nm

    def getColor(self):
        return self.color

    def getName(self):
        temp = ""
        if self.piece != None:
            temp = self.piece.getName()
        return temp

    def mkrPiece(self, p, team, colour):
        self.piece = self.pr.createPiece(p, team, colour)

    def setPiece(self, pi):
        self.piece = None
        self.piece = pi

    def getPiece(self):
        return self.piece
        # print(self.team.getName()[-1])


# Board object to act as a chess board
class Board:
    # Singleton-Pattern

    instance = None

    def __init__(self):
        if Board.instance == None:
            Board.instance = self

    @staticmethod
    def getInstance():
        if Board.instance == None:
            Board()
        return Board.instance

    # Actual Board

    # initializing primitives
    teamA = Team.Team()
    teamA.bin = 0
    teamB = Team.Team()
    teamB.bin = 1
    teamA.setName("PlayerA")
    teamB.setName("PlayerB")

    turnCount = 0  # ---------------------------------------------------------------------------------

    # using square object to create a chess board
    brd = [[Square() for j in range(8)] for i in range(8)]

    # for loop to set colour of squares in the board
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                brd[i][j].setColor("White")
            elif (i + j) % 2 == 1:
                brd[i][j].setColor("Black")

    print("Board Initialized!")

    # Methods
    def getBoard(self):
        return self.brd

    def printBoard(self):
        if self.turnCount == 0:
            print("                                                   " + str(self.teamA.getName()))
        elif self.turnCount == 1:
            print("                                                   " + str(self.teamB.getName()))
        print("                                               -------------");

        print("                                                     j")
        print(" ")

        print("              1            2            3            4            5           6            7           8");
        print(
            "       ---------------------------------------------------------------------------------------------------------")

        for i in range(8):
            if i==4: sys.stdout.write("i   ")
            else: sys.stdout.write("    ")
            sys.stdout.write(str(i + 1))
            sys.stdout.write("  |")
            for j in range(8):
                sys.stdout.write(" ")

                if self.brd[i][j].getPiece() != None:
                    sys.stdout.write(self.brd[i][j].getPiece().getName())  # to strng for board printing
                    sys.stdout.write(" |")
                else:
                    kg = "           |" if self.brd[i][j].getColor() == "White" else "           |"
                    sys.stdout.write(kg),
            print(" ")
            print(
                "       ---------------------------------------------------------------------------------------------------------")

        print(" ")
        print("                                               -------------");
        if self.turnCount == 0:
            print("                                                   " + str(self.teamB.getName()))
        elif self.turnCount == 1:
            print("                                                   " + str(self.teamA.getName()))

    def initializePieces(self):

        # Pwn
        for i in range(8):
            self.brd[1][i].mkrPiece("P", self.teamA,"B")
            self.brd[6][i].mkrPiece("P", self.teamB,"W")

        # Rook
        self.brd[0][0].mkrPiece("R", self.teamA,"B")
        self.brd[0][7].mkrPiece("R", self.teamA,"B")
        self.brd[7][0].mkrPiece("R", self.teamB,"W")
        self.brd[7][7].mkrPiece("R", self.teamB,"W")

        # Bishop
        self.brd[0][2].mkrPiece("B", self.teamA,"B")
        self.brd[0][5].mkrPiece("B", self.teamA,"B")
        self.brd[7][2].mkrPiece("B", self.teamB,"W")
        self.brd[7][5].mkrPiece("B", self.teamB,"W")

        # Knight
        self.brd[0][1].mkrPiece("Kn", self.teamA,"B")
        self.brd[0][6].mkrPiece("Kn", self.teamA,"B")
        self.brd[7][1].mkrPiece("Kn", self.teamB,"W")
        self.brd[7][6].mkrPiece("Kn", self.teamB,"W")

        # Rook
        self.brd[0][3].mkrPiece("Q", self.teamA,"B")
        self.brd[7][3].mkrPiece("Q", self.teamB,"W")

        # King
        self.brd[0][4].mkrPiece("K", self.teamA,"B")
        self.brd[7][4].mkrPiece("K", self.teamB,"W")

    def setTeamA(self, namea):
        self.teamA.setName(namea)
        print("dsffsa", namea)

    def setTeamB(self, nameb):
        self.teamB.setName(nameb)

    def getTeam(self, ab):
        return self.teamA if ab == 1 else self.teamB

    def isEmptyBox(self, i, j):
        return self.brd[i][j].getPiece() == None

    # From Point A to Point B - CHK and VERIFY
    def movePiece(self, Ai, Aj, Bi, Bj):



        # chk current team movement. user can only movie his piece (current playing team)
        #design check system for all indeces of array 'x'

        p = None
        x = self.validateMove(Ai, Aj, Bi, Bj)
        if x[0] and x[1] and not x[2]:
            p = self.brd[Bi][Bj].getPiece()
            self.brd[Bi][Bj].setPiece(self.brd[Ai][Aj].getPiece())
            self.brd[Ai][Aj].setPiece(None)
        return p




    # King validation
    def RetKingValidate(self, c1, c2, a, b, tnamep):
        retState = [bool] * 3
        if c1 and c2:
            if not self.isEmptyBox(a, b):
                if self.brd[a][b].getPiece().getTeam().getName() != tnamep:
                    retState[2] = False
                else:
                    retState[2] = True
                retState[1] = False
            else:
                retState[1] = True
                retState[2] = False
            retState[0] = True
        else:
            retState[0] = False

        return retState

    # Chk the entered indexes and verify the appropriatness ******
    def validateMove(self, ai, aj, bi, bj):

        #0 Is valid
        #1 Is full
        #2 is my team

        fpiece = self.brd[ai][aj].getPiece()

        retState = [bool] * 3

        # current team name
        tmname = self.brd[ai][aj].getPiece().getTeam().getName()

        # begin and futher case for pawn
        if fpiece.getName().find("Pawn") != -1:
            if bi==ai-1:

                retState = self.RetCrossValidate(tmname,bi,bj,ai-1,aj,retState)
                if retState[0]: return retState

            elif bi==ai-2 and ai==6 and self.isEmptyBox(bi-1,bj):

                retState = self.RetCrossValidate(tmname,bi,bj,ai-2,aj,retState)
                if retState[0]: return retState

            elif (bi==ai-1 and bj==aj+1):

                retState = self.RetCrossValidate(tmname, bi, bj, ai-1,aj+1,retState)
                if retState[0]: return retState


            elif (bi==ai-1 and bj==aj-1):

                retState = self.RetCrossValidate(tmname, bi, bj, ai-1, aj+1, retState)
                if retState[0]: return retState





        elif fpiece.getName().find("King") != -1:

            retState = self.RetKingValidate(ai > 0, (bi == ai - 1 and bj == aj), ai - 1, aj, tmname)  # up
            if retState[0]: return retState

            retState = self.RetKingValidate(ai < 7, (bi == ai + 1 and bj == aj), ai + 1, aj, tmname)  # down
            if retState[0]: return retState

            retState = self.RetKingValidate(aj > 0, (bi == ai and bj == aj - 1), ai, aj - 1, tmname)  # left
            if retState[0]: return retState

            retState = self.RetKingValidate(aj < 7, (bi == ai and bj == aj + 1), ai, aj + 1, tmname)  # right
            if retState[0]: return retState

            retState = self.RetKingValidate((ai > 0 and aj < 7), (bi == ai - 1 and bj == aj + 1), ai - 1, aj + 1,
                                            tmname)  # up-right
            if retState[0]: return retState

            retState = self.RetKingValidate((ai > 0 and aj > 0), (bi == ai - 1 and bj == aj - 1), ai - 1, aj - 1,
                                            tmname)  # up-left
            if retState[0]: return retState

            retState = self.RetKingValidate((ai < 7 and aj < 7), (bi == ai + 1 and bj == aj + 1), ai + 1, aj + 1,
                                            tmname)  # up-right
            if retState[0]: return retState

            retState = self.RetKingValidate((ai < 7 and aj > 0), (bi == ai + 1 and bj == aj - 1), ai + 1, aj - 1,
                                            tmname)  # up-left
            if retState[0]: return retState


        # fixOrCheck these-----------
        elif fpiece.getName().find("Bishop") != -1:
            retState = self.chkNchiki(ai, aj, bi, bj, tmname, 1, 0)
            if retState[0]: return retState



        elif fpiece.getName().find("Queen") != -1:
            retState = self.chkNchiki(ai, aj, bi, bj, tmname, 1, 1)
            if retState[0]: return retState


        elif fpiece.getName().find("Rook") != -1:
            retState = self.chkNchiki(ai, aj, bi, bj, tmname, 0, 1)
            if retState[0]: return retState



        elif fpiece.getName().find("Knight") != -1:



            for i in range(2):
                if i%2 == 0: it = ai+2
                elif i%2 == 1: it = ai-2
                for j in range(2):
                    if j % 2 == 0: jt = aj + 1
                    elif j % 2 == 1: jt = aj - 1
                    retState = self.RetCrossValidate(tmname,bi,bj,it,jt,retState)
                    if retState[0] == True: break
                if retState[0] == True: break


            print "------------------"

            if retState[0] == True: return retState

            for i in range(2):
                if i%2 == 0: it = aj+2
                elif i%2 == 1: it = aj-2
                for j in range(2):
                    if j % 2 == 0: jt = ai + 1
                    elif j % 2 == 1: jt = ai - 1
                    retState = self.RetCrossValidate(tmname, bi, bj, it, jt, retState)
                    if retState[0] == True: break
                if retState[0] == True: break

        return retState

    def RetCrossValidate(self, tname, bi, bj, a, b, rS):

        if bi == a and bj == b:
            if not self.isEmptyBox(a, b):
                if self.brd[a][b].getPiece().getTeam().getName() != tname:
                    rS[2] = False
                else:
                    rS[2] = True

                print "i " + str(a) + " : j " + str(b)
                rS[1] = False
            else:
                rS[1] = True
                rS[2] = False

            rS[0] = True
        else:

            rS[0] = False

        return rS

    def chkNchiki(self, ai, aj, bi, bj, tname, cross, plus):

        rS = [bool] * 3

        if cross == 1:
            # upperRight
            i = 0
            j = 0
            while 0 <= ai - i <= 7 and 0 <= aj + j <= 7:
                rS = self.RetCrossValidate(tname,bi,bj, ai - i, aj + j, rS)
                if rS[0]: return rS
                i = i + 1
                j = j + 1



            # upperLeft
            i = 0
            j = 0
            while 0 <= ai - i <= 7 and 0 <= aj - j <= 7:
                rS = self.RetCrossValidate(tname,bi,bj, ai - i, aj - j, rS)
                if rS[0]: return rS
                i = i + 1
                j = j + 1


            # lowerLeft
            i = 0
            j = 0
            while 0 <= ai + i <= 7 and 0 <= aj - j <= 7:
                rS = self.RetCrossValidate(tname,bi,bj, ai + i, aj - j, rS)
                if rS[0]: return rS
                i = i + 1
                j = j + 1


            # lowerRight
            i = 0
            j = 0
            while 0 <= ai + i <= 7 and 0 <= aj - j <= 7:
                rS = self.RetCrossValidate(tname,bi,bj, ai + i, aj - j, rS)
                if rS[0]: return rS
                i = i + 1
                j = j + 1



        if plus == 1:

            # up
            i = 0
            while 0 <= ai - i <= 7 :
                rS = self.RetCrossValidate(tname,bi,bj, ai - i, aj, rS)
                if rS[0]: return rS
                i = i + 1



            # Down
            i = 0
            while 0 <= ai + i <= 7:
                rS = self.RetCrossValidate(tname,bi,bj, ai + i, aj, rS)
                if rS[0]: return rS
                i = i + 1



            # Left
            j = 0
            while 0 <= aj - j <= 7:
                rS = self.RetCrossValidate(tname,bi,bj, ai, aj - j, rS)
                if rS != 0: return rS
                j = j + 1



            # Right
            j = 0
            while 0 <= aj + j <= 7:
                rS = self.RetCrossValidate(tname,bi,bj, ai, aj + j, rS)
                if rS != 0: return rS
                j = j + 1



        return rS




    def checkmate(self, team, brd):
        for i in range(len(self.brd)):
            for j in range(len(self.brd)):
                print self.brd[i][j].getName()




    # (can be used in Ai vs player, that would make validation easy) but can be used in player  vs player
    def flipBoard(self):
        self.brd.reverse()
        self.turnCount = 1


    def restart(self):
        self.brd.clear()
        self.brd = [[Square() for j in range(8)] for i in range(8)]
        self.turnCount = 0  # -------------------------------------------------------------------
        self.initializePieces()
        print("EVERYTHING RESTARTED!")


    def toString(self):
        st = ""
        st = st + "Game State---------------------\n"

        st = st + "Teams: " + self.teamA.getName() + " , " + self.teamB.getName() + "\n"

        st = st + "Score: " + str(self.teamB.getPoints()) + " , " + str(self.teamB.getPoints()) + "\n"

        return st
