from . import Dot


class DotCollection:
    # Insert dot
    def __init__(self, *args):  # default (), user-defined (nDots, dim)
        self.arrOfDot = []
        self.nDots = 0
        self.solvingTime = 0
        self.nStep = 0
        self.closestIndexes = [0, 0]
        self.closestPoints = []
        self.shortest_distance = 0
        if (len(args) == 2):
            print("Collection created")
            self.nDots = args[0]
            for i in range(self.nDots):
                self.arrOfDot.append(Dot.Dot(args[1]))
    
    # mengcopy nilai
    def copy(self, listOfDot):
        print("Copy Collection created")
        listOfDot.nDots = self.nDots
        for i in self.arrOfDot:
            listOfDot.arrOfDot.append(i)

    def addDot(self, d):
        self.arrOfDot.append(d)
        self.nDots += 1

    # Setter
    def setClosestIndexes(self, idx1, idx2):
        self.closestIndexes[0] = idx1
        self.closestIndexes[1] = idx2

    def setNStep(self, steps):
        self.nStep = steps

    def setSolvingTime(self, time):
        self.solvingTime = time

    def setShortestDistance(self, shortest_distance):
        self.shortest_distance = shortest_distance

    # Getter
    def getClosestIndexes(self):
        return self.closestIndexes

    def getNStep(self):
        return self.nStep

    def getSolvingTime(self):
        return self.solvingTime

    def getArrOfDot(self):
        return self.arrOfDot
    
    def getNDots(self) :
        return self.nDots

    def getShortestDistance(self):
        return self.shortest_distance

    def printArr(self):
        for dot in self.arrOfDot:
            print(dot.getCoordinate())

    def getClosestPoints(self):
        return (self.arrOfDot[self.closestIndexes[0]], self.arrOfDot[self.closestIndexes[1]])
