import math
import random

class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def locdist(self, p2):
        return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)

    def __str__(self):
        return str(self.x) + ", "+ str(self.y)

    def __eq__(self, p2):
        if self.x == p2.x and self.y == p2.y:
            return True
        return False

class salesmap():
    def __init__(self):
        self.loc = []
        self.size = 0
        self.bound = 500

    def addloc(self, p):
        self.loc.append(p)
        self.size += 1

    def retloc(self,i):
        return self.loc[i]

    def randomset(self, num):
        for x in range(num):
            self.loc.append(point(random.randint(0,self.bound), random.randint(0,self.bound)))

        self.size += num

class salespath():
    def __init__(self, map):
        self.dist = 0
        self.fit = 0
        self.path = []
        self.map = map

    def generatepath(self):
        self.path = self.map.loc
        self.randompath()

    def randompath(self):
        for p in range(len(self.path)):
            swap = random.randint(p,len(self.path)-1)
            temp = self.path[swap]
            self.path[swap] = self.path[p]
            self.path[p] = temp

    def getloc(self, i):
        return self.path[i]

    def setloc(self, loc, i):
        self.path[i] = loc
        self.dist = 0
        self.fit = 0

    def findfit(self):
        if self.fit == 0:
            self.fit = 1 / self.getpathL()
        return self.fit

    def getpathL(self):
        if self.dist == 0:
            temp = 0

            for x in range(1,len(self.path)):
                temp += self.path[x].locdist(self.path[x-1])

        self.dist = temp
        return temp

    def contains(self, loc):
        for x in self.path:
            if x == loc:
                return True

        return False




