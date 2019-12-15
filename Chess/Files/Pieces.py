
import Team
#-------------Pieces------------------
class Bishop:

    def __init__(self, team, cr):
        self.team = team
        self.name = "Bishop"+cr

    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +" -"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class King:

    def __init__(self, team, cr):
        self.team = team
        self.name = " King"+cr+" "


    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +" -"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class Knight:

    def __init__(self, team, cr):
        self.team = team
        self.name = "Knight"+cr


    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +" -"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class Pawn:

    def __init__(self, team , cr):
        self.team = team
        self.name = " Pawn"+cr+" "


    def getName(self):


        temp = self.team.getName()[0] + self.team.getName()[-1] +" -"+ self.name

        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class Queen:

    def __init__(self, team, cr):
        self.team = team
        self.name = " Queen"+cr


    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +" -"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class Rook:
    def __init__(self, team, cr):
        self.team = team
        self.name = " Rook"+cr+" "

    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +" -"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-----------------------------------
#---------Piece-Factory-------------

class PeiceMkr:

    res = None

    def createPiece(self,name, team, clr):
        if name == "B":
            self.res = Bishop(team=team, cr=clr)
        elif name == "R":
            self.res = Rook(team=team, cr=clr)
        elif name == "P":
            self.res  = Pawn(team=team, cr=clr)
        elif name == "Kn":
            self.res  = Knight(team=team, cr=clr)
        elif name == "K":
            self.res  = King(team=team, cr=clr)
        elif name == "Q":
            self.res  = Queen(team=team, cr=clr)

        return self.res

