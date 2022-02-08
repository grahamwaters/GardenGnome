'''
Goals and Objectives

1. Learn the basics of ML through the exploration of basic Entity actions. (1st)
2. Explore how ML (Reinforcement learning) is applied to virtual entities in virtual spaces like OpenAI Gym and MineRL (3rd)
3. Learn how to benchmark a model's loss % on a graph while it is learning. (2nd)

goal: explore the exciting things in data science and at the same time learn python skills that employers will want me to have on the job.
potentially encorporate the different algorithm types (like knearest neighbor or graph traversal) to real-world problems relevant to a job.

If we can work the items below into the "narrative" (lesson plan) then it would be good.
Algorithms
4. Polymorphism
5. Dunder Methods
6. Data Abstraction
7. Encapsulation
8. Async I/O with Files
9. list comprehension using [x in..]
10. lambda functions
11. class inheritance

https://colab.research.google.com/drive/1v4zBm_2Qczo02Vz1fUXnkjo_KMs-Mkn9?usp=sharing

Notes
def __init__(self,gnome_name='robert', mouth):
  self.mouth = mouth

means that user can specify what the gnome says by providing "mouth" as string. Applies to the first time the gnome is instantiated.



'''
import matplotlib.pyplot as plt

class Gnome:
    #Atributes: arms, legs, location, health, mood, head, mouth, eyes
    arm = 0
    leg = 2
    mouth = "Hey... I'm Greg..."
    health = 100
    mood = 0
    Interest = 0 # starts with no interest at all in features within his/her action space
    eyes = 2 # has two eyes that are able to sense dangers and other things
    head = 1
    strength = 50 # ranges from 1 to 100 and will change based on interactions with environment.
    gnome_name = "Greg"
    xlocation = 2 # call gamearea len(gamearea)//2 gives the central point if it is an odd number of cols or rows
    ylocation = 2
    DistanceFromHome = 0

    #Constructor
    def __init__(self,gnome_name, mouth):
        self.gnome_name = gnome_name
        self.mouth = mouth


    '''
    if we don't declare it then python will do this
    def __init__(self):
        n/a inside

    void talk(){
        # no returns
    }


    '''
    # Gets and Sets

    #arm
    def getArm(self):
        return self.arm
    def setArm(self, newArm):
        self.arm = newArm

    #leg
    def getLeg(self):
        return self.leg
    def setLeg(self,newLeg):
        self.leg = newLeg

    #head
    def getArm(self):
        return self.arm
    def setArm(self, newArm):
        self.arm = newArm

    #mouth for talking
    def getMouth(self):
        return self.mouth
    def setMouth(self, newMouth):
        self.mouth = newMouth

    #eyes
    def getEyes(self):
        return self.eyes
    def setEyes(self, newEyes):
        self.eyes = newEyes



    #secondary conditions
    #strength
    def getStrength(self):
        return self.Strength
    def setStrength(self, newStrength):
        self.strength = newStrength
    #mood
    def getMood(self):
        return self.mood
    def setMood(self, newMood):
        self.mood = newMood
    #speed of movement
    def getStrength(self):
        return self.Strength
    def setStrength(self, newStrength):
        self.strength = newStrength

    #mood
    #x,y location

    #getting x,y coordinate
    def getXlocationGnome(self):
        return self.xlocation# init

    def getYlocationGnome(self):
        return self.ylocation



    def getInterest(self):
        return self.Interest
    def setInterest(self, newInterest):
        self.interest = newInterest

    #setting x,y coordinate
    def setXlocationGnome(self,newXloc):
        self.xlocation = newXloc # init
    def setYlocationGnome(self,newYloc):
        self.ylocation = newYloc

    #distance from its home shelter in the space
    def getDistanceFromHome(self):
        return self.DistanceFromHome
    def setDistanceFromHome(self, newDistanceFromHome):
        self.DistanceFromHome = newDistanceFromHome

    #name
    def getName(self):
        return self.gnome_name
    def setName(self,newName):
        self.gnome_name = newName

    #Methods:
    '''
    talk - asking gnome to talk or say something.
    move
    decide # a binary choice about moving
    eat
    later on add drink
    sleep
        turning on
        turning off
    later on add attack
    later on add defend

    '''

    def talk(self):
        #print(self.mouth) this is an error
        print(self.getMouth())

    def moveUp(self): #w a s d
        try:
          return (self.getXlocationGnome(), self.getYlocationGnome()-1)
        except Exception:
          print("cannot perform action")

    def moveDown(self): #w a s d
        try:
          return (self.getXlocationGnome(), self.getYlocationGnome()+1)
        except Exception:
          print("cannot perform action")
    def moveLeft(self): #w a s d
        try:
          return (self.getXlocationGnome()-1, self.getYlocationGnome())
        except Exception:
          print("cannot perform action")
    def moveRight(self): # w a s d
        try:
          return (self.getXlocationGnome()+1, self.getYlocationGnome())
        except Exception:
          print("cannot perform action")


    def move(self,Game_Area):

      # x origin is [2,2]
      #x = int(input("Steps in X direction: "))
      #y = int(input("Steps in Y direction: "))
      print("Where do you want to move? ") # this is a waypoint
      moveTo = 'w' # init default
      while moveTo in ['w','a','s','d']:
        moveTo = input(":")
        try:
          if(moveTo == 'w'):
            x, y = self.moveUp()
          elif(moveTo == 'a'):
            x,y = self.moveLeft()
          elif(moveTo == 's'):
            x,y = self.moveDown()
          elif(moveTo == 'd'):
            x,y = self.moveRight()
          else:
            print("not a direction")
            x = 'n/a'
            y = 'n/a'
            break
        except Exception:
          print("Exception...")
        finally:
          self.setXlocationGnome(x)
          self.setYlocationGnome(y)
          currentX = self.getXlocationGnome()
          currentY = self.getYlocationGnome()

        # G-Nome

        print(f'[{currentX},{currentY}]')

        Game_Area.setGame_Area_Position(currentX,currentY)
        print(f'moved to --> [{currentX},{currentY}]')

        Game_Area.printGame()



      return currentX,currentY

    #speed of movement
    def getSpeed(self):
        return self.Speed
    def setSpeed(self, newSpeed):
        self.speed = newSpeed

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

  #Gets and Sets
  def getGame_Area(self):
    return self.Game_Area
  def setGame_Area(self, newGame_Area):
    self.Game_Area = newGame_Area

  # gnome location (new)
  def setGame_Area_Position(self,x, y):
    # passing a matrix to this function
    self.Game_Area[x][y] = 1
  def getGame_Area_Position(self,x, y):
    return self.Game_Area[x][y]

  #TODO method needed: delete previous position

  def printGame(self):
    for row in self.Game_Area:
      print(row)

    game_area = self.getGame_Area()
    plt.imshow(game_area, cmap=plt.get_cmap('gray'))
    plt.show()


if __name__ == '__main__':

  Robert_the_Gnome = Gnome("Robert", "Hi I am a happy gnome!") # include # of parameters in the objects construction
  Game_Area = ObservationSpace("Garden")
  print(Robert_the_Gnome.getName()) #not good
  print(Robert_the_Gnome.getArm())
  Robert_the_Gnome.talk()


  Robert_the_Gnome.move(Game_Area)


  '''
  random walk? and provide a waypoint.


  '''