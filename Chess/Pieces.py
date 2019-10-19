import Team
#-------------Pieces------------------
class Bishop:
    name = "Bishop"

    def __init__(self, team):
        self.team = team

    def getName(self):
        return self.name

    def getTeam(self):
        return self.team
#-------------------------------------

class King:

    name = "King"

    def __init__(self, team):
        self.team = team

    def getName(self):
        return self.team

    def getTeam(self):
        return self.team
#-------------------------------------

class Knight:
    initialPos = [0,1]

    def __init__(self, team):
        self.team = team

    def getName(self):
        return self.team

    def getTeam(self):
        return self.team
#-------------------------------------

class Pawn:
    name = "Pawn"

    def __init__(self, team):
        self.team = team

    def getName(self):
        return self.team

    def getTeam(self):
        return self.team
#-------------------------------------

class Queen:
    name = "Queen"

    def __init__(self, team):
        self.team = team

    def getName(self):
        return self.team

    def getTeam(self):
        return self.team
#-------------------------------------

class Rook:
    name = "Rook"

    def __init__(self, team):
        self.team = team

    def getName(self):
        return self.team

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
            print()
        elif name == "Kn":
            self.res  = Knight(team=team)
        elif name == "K":
            self.res  = King(team=team)
        elif name == "Q":
            self.res  = Queen(team=team)

