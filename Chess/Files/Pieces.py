
import Team
#-------------Pieces------------------
class Bishop:

    def __init__(self, team):
        self.team = team
        self.name = "Bishop"

    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +" -"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class King:

    def __init__(self, team):
        self.team = team
        self.name = " King "


    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +" -"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class Knight:

    def __init__(self, team):
        self.team = team
        self.name = "Knight"


    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +" -"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class Pawn:

    def __init__(self, team):
        self.team = team
        self.name = " Pawn "


    def getName(self):


        temp = self.team.getName()[0] + self.team.getName()[-1] +" -"+ self.name

        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class Queen:

    def __init__(self, team):
        self.team = team
        self.name = " Queen"


    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +" -"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class Rook:
    def __init__(self, team):
        self.team = team
        self.name = " Rook "

    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +" -"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-----------------------------------
#---------Piece-Factory-------------

class PeiceMkr:

    res = None

    def createPiece(self,name, team):
        if name == "B":
            self.res = Bishop(team=team)
        elif name == "R":
            self.res = Rook(team=team)
        elif name == "P":
            self.res  = Pawn(team=team)
        elif name == "Kn":
            self.res  = Knight(team=team)
        elif name == "K":
            self.res  = King(team=team)
        elif name == "Q":
            self.res  = Queen(team=team)

        return self.res

