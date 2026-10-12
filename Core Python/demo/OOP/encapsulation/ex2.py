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
        
t1 = Transport(1234, 2, 'abc')
t2 = Transport(5678, 4, 'def')
t1.display()
t2.display()