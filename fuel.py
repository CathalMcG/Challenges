"""
    A queue of cars is waiting to refuel at a set of 3 pumps. Each pump
    serves one car at a time, and each pump can fuel a car at a rate of
    1 unit of fuel per unit time. You can assume that cars move
    instantaneously.

    Each pump has its remaining fuel count displayed prominently, so
    each car in the queue will wait until there is an available pump
    with enough fuel, then go to the lowest letter such pump. If there
    are no pumps with enough fuel to fill a car, the car blocks the
    queue.

    Write a function which
    Given:
        list A, where each positive integer a in A is a car's fuel requirement
        positive integers X, Y, Z, the amount of fuel in each fuel pump
    Will return:
        The maximum period of wait time
        or
        -1 if the queue is blocked
"""

def solution(A, X, Y, Z):
    cars = [Car(fuelReq) for fuelReq in A]
    plaza = Plaza([X,Y,Z])
    maxWait = 0
    currentWait = 0

    for car in cars:        
        # while there are no available pumps, wait for other
        # cars to pump
        currentWait = 0
        while(not plaza.findSuitablePump(car)):
            # if no pumps have enough fuel, the queue is blocked
            if not plaza.canDispense(car.getFuelRequirement()):
                return -1

            plaza.dispenseAll()
            currentWait += 1
            maxWait = max(maxWait, currentWait)

    return maxWait


class Plaza(object):
    def __init__(self, fuels):
        super(Plaza, self).__init__()
        self.pumps = [Pump(fuel) for fuel in fuels]

    def findSuitablePump(car):
        for pump in pump in self.pumps if pump.isAvailable() and
                                          pump.getRemainingFuel() >= car.getFuelRequirement():
            pump.attachCar(car)
            return True
        return False

    def dispenseAll():
        for pump in self.pumps if pump.isOccupied():
            pump.dispenseFuel()

    def canDispense(self, fuelRequirement):
        for pump in self.pumps if pump.getRemainingFuel() >= fuelRequirement:
            return True
        return False


class Car(object):
    def __init__(self, fuelRequirement):
        super(Car, self).__init__()
        self.fuelRequirement = fuelRequirement

    def getFuelRequirement(self):
        return self.fuelRequirement

    def addFuel(self):
        self.fuelRequirement -= 1

    def tankFull(self):
        return self.fuelRequirement == 0


class Pump(object):
    def __init__(self, fuel):
        super(Pump, self).__init__()
        self.fuel = fuel
        self.car = None

    def attachCar(self, car):
        self.car = car

    def releaseCar(self):
        self.car = None

    def isAvailable(self):
        return self.car == None

    def isOccupied(self):
        return self.car != None

    def getRemainingFuel(self):
        return self.fuel

    def dispenseFuel(self):
        self.car.addFuel()
        self.fuel -= 1
        if self.car.tankFull():
            self.releaseCar()
