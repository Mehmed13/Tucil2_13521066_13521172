from . import Dot

class DotCollection :
    arrOfDot = []
    nDots = 0
    solvingTime = 0
    nStep = 0
    closestIndexes = [-1,-1]

    # Insert dot
    def __init__ (self, nDots, dim) :
        print("Collection created")
        self.nDots = nDots
        for i in range (0,nDots) :
            self.arrOfDot.append(Dot.Dot(dim))

    def addDot(self, d) :
        self.arrOfDot.append(d)
    
    # Setter
    def setClosestIndexes(self, idx1, idx2) :
        self.closestIndexes[0] = idx1
        self.closestIndexes[1] = idx2
    def setNStep(self, steps) :
        self.nStep = steps
    def setSolvingTime(self, time) :
        self.solvingTime = time

    # Getter
    def getClosestIndexes(self):
        return self.closestIndexes
    def getNStep(self) :
        return self.nStep
    def getSolvingTime(self) :
        return self.solvingTime
    def getArrOfDot(self) :
        return self.arrOfDot
    
    def printArr(self) :
        for dot in self.arrOfDot :
            print(dot.getCoordinate())
