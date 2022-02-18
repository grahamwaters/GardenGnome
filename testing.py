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
def __init__(self,agent_name='robert', mouth):
  self.mouth = mouth

means that user can specify what the agent says by providing "mouth" as string. Applies to the first time the agent is instantiated.



'''
import plotly.graph_objects as go
import numpy as np

import matplotlib.pyplot as plt # CAVEAT: may change if OpenAI Gym is used for example.
import numpy as np #import
x_position = [] # initialize both position arrays for the path of the agent
y_position = []
class Agent:

    #Atributes: arms, legs, location, health, mood, head, mouth, eyes

    mouth = "Hey... I'm Greg..."
    health = 100
    mood = 0
    Interest = 0 # starts with no interest at all in features within his/her action space
    strength = 50 # ranges from 1 to 100 and will change based on interactions with environment.
    agent_name = "Greg"
    xlocation = 2 # call gamearea len(gamearea)//2 gives the central point if it is an odd number of cols or rows
    ylocation = 2
    DistanceFromHome = 0

    #Constructor
    def __init__(self,agent_name, mouth):
        self.agent_name = agent_name
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
    def getXlocationAgent(self):
        return self.xlocation# init

    def getYlocationAgent(self):
        return self.ylocation

    def getInterest(self):
        return self.Interest
    def setInterest(self, newInterest):
        self.interest = newInterest

    #setting x,y coordinate
    def setXlocationAgent(self,newXloc):
        self.xlocation = newXloc # init
    def setYlocationAgent(self,newYloc):
        self.ylocation = newYloc

    #distance from its home shelter in the space
    def getDistanceFromHome(self):
        return self.DistanceFromHome
    def setDistanceFromHome(self, newDistanceFromHome):
        self.DistanceFromHome = newDistanceFromHome

    #name
    def getName(self):
        return self.agent_name
    def setName(self,newName):
        self.agent_name = newName

    #Methods:
    '''
    talk - asking agent to talk or say something.
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
        print(self.getMouth())

    def moveUp(self): #w a s d
        try:
          return (self.getXlocationAgent(), self.getYlocationAgent()-1)
        except Exception:
          print("cannot perform action")

    def moveDown(self): #w a s d
        try:
          return (self.getXlocationAgent(), self.getYlocationAgent()+1)
        except Exception:
          print("cannot perform action")
    def moveLeft(self): #w a s d
        try:
          return (self.getXlocationAgent()-1, self.getYlocationAgent())
        except Exception:
          print("cannot perform action")
    def moveRight(self): # w a s d
        try:
          return (self.getXlocationAgent()+1, self.getYlocationAgent())
        except Exception:
          print("cannot perform action")


    def move(self,Game_Area):
      '''
      Summary: Goal is to move the agent through the game area. This area is represented by a matrix of 1's and 0's denoting the boolean state: contains the location of the agent or does not contain the location of the agent.

      Args:
          Game_Area (matrix): The observation space.

      Returns:
          currentX: the current X position of the agent.
          currentY: the current Y position of the agent.
      '''
      # x origin is [2,2]
      currentX = 0 # initialise
      currentY = 0 # initialise

      print("Where do you want to move? ") # this is a waypoint
      moveTo = 'w'# init default
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
          self.setXlocationAgent(x)
          self.setYlocationAgent(y)
          currentX = self.getXlocationAgent()
          currentY = self.getYlocationAgent()

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

  #Constructor
  def __init__(self,Game_Name,Agent,n):
      """
      INITIALIZER
      Args:
          Game_Name ([string]): the game name will be supplied by user for now until further changed into survival of the fattest or something witty like that.
      """
      self.Game_Name = Game_Name
      Agent.xlocation = n//2 # find middle
      Agent.ylocation = n//2 # place in middle of the matrix

  Game_Area = [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]

  n = 21
  Game_Area = np.zeros((n,n))

  Game_Name = "Hide and Seek"

  #Gets and Sets
  def getGame_Area(self):
    return self.Game_Area
  def setGame_Area(self, newGame_Area):
    self.Game_Area = newGame_Area

  # agent location (new)
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

  def build_walk(self,new_x,new_y): # generator
    '''generates a trail from x,y coordinates showing a path taken by an agent.

    Args:
        new_x ([int]): [delta x]
        new_y ([int]): [delta y]

    Yields:
        [tuple of coordinates]: [shows entire pathway up to the current steps]
    '''

    #builds a trail
    x_position.append(int(new_x))
    y_position.append(int(new_y))

    yield (x_position,y_position)

  def random_walk(self,x_steps,y_steps,n):
      #l = 1000
      #x_steps = np.random.choice([-1, 1], size=l) + 0.2 * np.random.randn(l) # l steps
      #y_steps = np.random.choice([-1, 1], size=l) + 0.2 * np.random.randn(l) # l steps
      x_position = np.cumsum(x_steps) # integrate the position by summing steps values
      y_position = np.cumsum(y_steps) # integrate the position by summing steps values

      fig = go.Figure(data=go.Scatter(
          x=x_position,
          y=y_position,
          mode='markers',
          name='Random Walk',
          marker=dict(
              color=np.arange(len(x_steps)),
              size=8,
              colorscale='Greens',
              showscale=True
          )
      ))
      if len(x_steps)==n-1: # If we have reached the end of the x_teps list...
        fig.show() # then show the figure.
class Visual_Tests:
      #Constructor
  Visual_Name = 'Random Walk'
  def __init__(self,Visual_Name):
      """
      INITIALIZER
      Args:
          Visual_Name ([string]): the visual name that will be used.
      """
      self.Visual_Name = Visual_Name







if __name__ == '__main__':

  Robert_the_Agent = Agent("Robert", "Hi I am a happy agent!") # include # of parameters in the objects construction
  Game_size = 21 # how big is the game size?
  Game_Area = ObservationSpace("Garden",Robert_the_Agent,Game_size) # create the environment for the game
  # now make the agent walk through it with the provided methods.

  # GLOSS: Game area now can be traversed by the agent
  stop_walking = False
  while stop_walking == False:
    #* agent is walking and choosing paths
    x_position,y_position = next(Game_Area.build_walk(x_position,y_position,Game_Area.n))

  Game_Area.random_walk()


  print(Robert_the_Agent.getName()) #not good
  print(Robert_the_Agent.getArm())
  Robert_the_Agent.talk()


  Robert_the_Agent.move(Game_Area)


  '''
  random walk? and provide a waypoint.


  '''
