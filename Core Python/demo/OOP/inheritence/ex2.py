class Transport:
    def __init__(self, number, capacity, route):
        self.number = number
        self.capacity = capacity
        self.route = route
        
    def getNumber(self):
        return self.number
    def setNumber(self, newid):
        self.number = newid
        
    def getCapacity(self):
        return self.capacity
    def setCapacity(self, newid):
        self.capacity = newid
        
    def getRoute(self):
        return self.route
    def setRoute(self, newid):
        self.route = newid
        
    def display(self):
        print(f'VehicleNumber:{self.number}\tCapacity:{self.capacity}\tRoute:{self.route}')
        
#Transport class ends here...................

class Roadtransport(Transport):
    def __init__(self, number, capacity, route, vehicle):
        super().__init__(number, capacity, route)
        self.vehicle = vehicle
    def getVehicle(self):
        return self.vehicle
    def setVehicle(self,newid):
        self.vehicle = newid
    def display(self):
        print(f'Vehicle:{self.vehicle}')
        return super().display()
    
# Roadtransport class ends here..............

class Airtransport(Transport):
    def __init__(self, number, capacity, route, type):
        super().__init__(number, capacity, route)
        self.type = type
    def getType(self):
        return self.type
    def setType(self, newid):
        self.type = newid
    def display(self):
        print(f'Type:{self.type}')
        return super().display()
    
t1 = Transport(12, 200, 'punetomumbai')
r1 = Roadtransport(1234, 4, 'punetomumbai', 'Car')
a1 = Airtransport(23, 2, 'nsktopune', 'Helicopter')

t1.display()
r1.display()
a1.display()