class Automobiles:
    def __init__(self,wheeler,windows,colour):
        self.wheeler=wheeler
        self.windows=windows
        self.colour=colour
    def display(self):
        print(self.wheeler,self.windows,self.colour)
mycar= Automobiles(4,4,"black")
mycar.display()

class Bus(Automobiles):
    def __init__(self,wheeler,windows,colour,company):
        Automobiles.__init__(self,wheeler,windows,colour)
        self.company=company
    def details(self):
        print(self.wheeler,self.windows,self.colour,self.company)
SchoolBus= Bus(4,True,"yellow","ABC")
SchoolBus.details()

#how to calculate the fair??