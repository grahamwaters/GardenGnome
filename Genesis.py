'''
Goals and Objectives

1. Learn the basics of ML through the exploration of basic Entity actions.
2. Explore how ML (Reinforcement learning) is applied to virtual entities in virtual spaces like OpenAI Gym and MineRL
3. Learn how to benchmark a model's loss % on a graph while it is learning.

https://colab.research.google.com/drive/1v4zBm_2Qczo02Vz1fUXnkjo_KMs-Mkn9?usp=sharing

Notes
def __init__(self,agent_name='robert', mouth):
  self.mouth = mouth

means that user can specify what the agent says by providing "mouth" as string. Applies to the first time the agent is instantiated.

Agent away from Home
Agent away from Agent
Agent on Agent Violence
Working from Agent
Agent is where the Heart is
Love makes a house a Agent
MisAgentr
Les MisAgentrables
Gnoman's Land
The Gnomad
Gnomadic Life
There's no place like Agent
Leaving Agent

'''
import basic_garden
import basic_agent
from basic_garden import *
from basic_agent import *

if __name__ == '__main__':


  Robert_the_Agent = Agent("Robert", "Hi I am a happy agent!") # include # of parameters in the objects construction
  Game_Area = ObservationSpace("Garden")
  print(Robert_the_Agent.getName()) #not good
  print(Robert_the_Agent.getArm())
  Robert_the_Agent.talk()


  newx, newy = Robert_the_Agent.move()
  Game_Area.setGame_Area_Position(newx,newy)
  Game_Area.printGame()
