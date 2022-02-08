'''
Goals and Objectives

1. Learn the basics of ML through the exploration of basic Entity actions.
2. Explore how ML (Reinforcement learning) is applied to virtual entities in virtual spaces like OpenAI Gym and MineRL
3. Learn how to benchmark a model's loss % on a graph while it is learning.

https://colab.research.google.com/drive/1v4zBm_2Qczo02Vz1fUXnkjo_KMs-Mkn9?usp=sharing

Notes
def __init__(self,gnome_name='robert', mouth):
  self.mouth = mouth

means that user can specify what the gnome says by providing "mouth" as string. Applies to the first time the gnome is instantiated.

Gnome away from Home
Gnome away from Gnome
Gnome on Gnome Violence
Working from Gnome
Gnome is where the Heart is
Love makes a house a Gnome
MisGnomer
Les MisGnomerables
Gnoman's Land
The Gnomad
Gnomadic Life
There's no place like Gnome
Leaving Gnome

'''
import basic_garden
import basic_gnome
from basic_garden import *
from basic_gnome import *

if __name__ == '__main__':


  Robert_the_Gnome = Gnome("Robert", "Hi I am a happy gnome!") # include # of parameters in the objects construction
  Game_Area = ObservationSpace("Garden")
  print(Robert_the_Gnome.getName()) #not good
  print(Robert_the_Gnome.getArm())
  Robert_the_Gnome.talk()


  newx, newy = Robert_the_Gnome.move()
  Game_Area.setGame_Area_Position(newx,newy)
  Game_Area.printGame()
