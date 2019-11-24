
class Team:
    name = ""
    points = 0
    bin = 0
    KilledOnes=[0]

    def setName(self, namef):
        self.name = namef

    def addKilled(self,killed):
        self.KilledOnes.append(killed)

    def getKilledOnes(self):
        return self.KilledOnes

    def getPoints(self):
        return self.points

    def getName(self):
        return self.name

    def toString(self):
        st = "Team: " + self.name + " , Points: " + str(self.points)
        return st
