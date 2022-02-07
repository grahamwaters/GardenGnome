
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
    def getHead(self):
        return self.head
    def setHead(self,newHead):
        self.head = newHead

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

    def move(self):
        """
            summary: move the gnome through the observation space with actions
            variables:
                x ([type]): [description]
                y ([type]): [description]
                currentX ([type]): [description]
                currentY ([type]): [description]
            Returns:
                (x,y): an x,y coordinate tuple denoting location of the gnome within the space.
        """
        # x origin is [2,2]
        x = int(input("Steps in X direction: "))
        y = int(input("Steps in Y direction: "))
        currentX = int(self.getXlocationGnome())
        currentY = int(self.getYlocationGnome())
        print(currentX,",",x)
        self.setXlocationGnome(currentX+x)
        self.setYlocationGnome(currentY+y)

        return x,y

    #speed of movement
    def getSpeed(self):
        return self.Speed
    def setSpeed(self, newSpeed):
        self.speed = newSpeed
