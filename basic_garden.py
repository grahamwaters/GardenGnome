
class ObservationSpace:

  Game_Area = [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]
  Game_Name = "Tik Tak Toe"

  #Constructor
  def __init__(self,Game_Name):
      """INITIALIZER

      Args:
          Game_Name ([string]): the game name will be supplied by user for now until further changed into survival of the fattest or something witty like that.
      """
      self.Game_Name = Game_Name

  #Get and Set
  def getGame_Area(self):
    return self.Game_Area
  def setGame_Area(self, newGame_Area):
    self.Game_Area = newGame_Area
  # gnome location (new)
  def setGame_Area_Position(self,x, y):
    self.Game_Area[x][y] = 1
  def getGame_Area_Position(self,x, y):
    return self.Game_Area[x][y]

  #TODO method needed: delete previous position,
  def printGame(self):
    for row in self.Game_Area:
      print(row)
