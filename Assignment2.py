
from A2classes import *
import random

mutationR = 5
tournaments = 5

def evolve(routes):
    temp = [len(routes.path)]

    temp.append(getbestpath(routes))

    for x in range(1, routes.num):
        temp1 = selectTournament(routes)
        temp2 = selectTournament(routes)

        temp3 = crossover(temp1,temp2)
        temp.append(temp3)

    for x in range(1,routes.num):
        temp[x].path = mutate(temp[x].path)

    return temp


def crossover(r1, r2):
    temp = [len(r1.path)]

    start = random.randint(len(r1.path))
    end = random.randint(len(r1.path))

    if start > end:
        swap = end
        end = start
        start = swap

    for x in range(len(r1.path)):
        if x > start and x < end:
            temp[x] = r1.path[x]

    for x in r2.path:
        if temp.contains(x):
            for c in range(len(r1.num)):
                if not temp[c]:
                    temp[c] = x
                    break
    child = salespath(temp)
    child.path = temp
    return child

def mutate(path):
    for p in range(len(path)):
        if random.randint(100) < mutationR:
            temp = random.randint(len(path))

            swap = path[p]
            path[p] = path[temp]
            path[temp] = swap

def selectTournament(routes):
    temp = []

    for x in range(tournaments):
        temp.append(routes[random.randint(len(routes))])

    return getbestpath(temp)


def getbestpath(routes):
    temp = 0
    best = -1
    for x in range(len(routes[0].path)):
        if temp < routes[x].findfit():
            temp = routes[x].fit
            best = x
    return best



def main():
    test = []
    testmap = salesmap()
    testmap.randomset(20)

    for x in range(20):
        test.append(salespath(testmap))

    print(getbestpath(test))


if __name__ == "__main__":
    main()