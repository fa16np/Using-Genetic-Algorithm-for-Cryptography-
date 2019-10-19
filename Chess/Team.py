
class Team:
    name = ""

    KilledOnes=[0]

    def setName(self, name):
        self.name = name

    def addKilled(self,killed):
        self.KilledOnes.append(killed)

    def getKilledOnes(self):
        return self.KilledOnes

    def getName(self):
        return self.name

