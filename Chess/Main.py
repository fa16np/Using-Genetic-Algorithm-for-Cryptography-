import Board


b=Board.Board()
# b.initializePieces()
b.setTeamA(input("Give a name to Team A"))
b.setTeamB(input("Give a name to Team B"))
# b.printBoard()
print(b.getTeam(1).getName())
print(b.getTeam(0).getName())
