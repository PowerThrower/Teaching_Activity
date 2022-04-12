import random
import string
import math


class Computer():
    def __init__(self):
        self.isHacked = False
        self.isOn = True
        self.adjacentComp = []
        self.password = str(int(math.pow(random.randint(1, 5), random.randint(1, 10))))

    def hacked(self, ignoredValue):
        self.isHacked = True

    def off(self, ignoredValue):
        self.isOn = False

    def adjSet(self, comp1, comp2):
        self.adjacentComp = (comp1, comp2)

    def hack(self, ignoredValue):
        if (self.isOn):
            # a) Evidently, x = 0 doesn't work.  Design a better password breaker below!
            x = 0
        pass
        
class YourComputer(Computer):
    # Add your own password (or password generator) here!
    pass

# The following is for setting up the program, no need to edit it.
class Network:
    def __init__(self, List):
        self.List = List
        for i in range(9):
            computer = Computer()
            List.append(computer)
        computer = YourComputer()
        List.append(computer)
        
        for i in range(9):
            randOff = random.randint(0,10)
            if randOff < 2:
                List[i].off(True)

            randComp1 = i
            randComp2 = i
            while (randComp1 == i or randComp2 == i or randComp1 == randComp2):
                randComp1 = random.randint(0,9)
                randComp2 = random.randint(0,9)
                List[i].adjSet(List[randComp1], List[randComp2])
            
        while(True):
            randHack = random.randint(0,9)
            if (List[randHack].isOn):
                List[randHack].hacked(True)
                return

    def infect(self):
        for i in range(9):
            if (self.List[i].isHacked == True):
                self.List[i].adjacentComp[0].hack(True)
                self.List[i].adjacentComp[1].hack(True)
                break

    def print(self):
        for i in range(9):
            if (not self.List[i].isOn):
                print("Computer " + str(i + 1) + "...is off.  Can't be hacked.")
            elif (self.List[i].isHacked):
                print("Computer " + str(i + 1) + "...is hacked!")
            else:
                print("Computer " + str(i + 1) + "...is fine.")

        if (self.List[9].isHacked):
            print("Your computer, in the meantime...has been hacked!")
        else:
            print("Your computer, in the meantime...is still safe!")


def main():
    endRun = False
    network = Network([])
    runXtimes = 0
    while (not endRun):
        network.infect()
        network.print()
        runXtimes += 1
        if (network.List[9].isHacked):
            print("Oh no!  You can't access your own computer anymore!")
            endRun = True
        if (runXtimes == 10):
            print("Impressive!  Your computer avoided being hacked!")
            endRun = True

if __name__ == "__main__":
    main()
