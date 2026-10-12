class Transport:
    def __init__(self, number, capacity, route, fare):
        self.number = number
        self.capacity = capacity
        self.route = route
        self.fare = fare
        
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
        
    def Calfare(self):
        print(f'Total fare:{self.fare}')
    
    def display(self):
        print(f'VehicleNumber:{self.number}\tCapacity:{self.capacity}\tRoute:{self.route}')
        
#Transport class ends here...................

class Roadtransport(Transport):
    def __init__(self, number, capacity, route, vehicle, fare, km):
        super().__init__(number, capacity, route, fare)
        self.vehicle = vehicle
        self.km = km
    def getVehicle(self):
        return self.vehicle
    def setVehicle(self,newid):
        self.vehicle = newid
    def Calfare(self):
        print(f'Total fare:{self.fare*self.km}')
    def display(self):
        print(f'Vehicle:{self.vehicle}')
        return super().display()
    
# Roadtransport class ends here..............

class Airtransport(Transport):
    def __init__(self, number, capacity, route, type, fare, tax):
        super().__init__(number, capacity, route, fare)
        self.type = type
        self.tax = tax
    def getType(self):
        return self.type
    def setType(self, newid):
        self.type = newid
    def Calfare(self):
        print(f'Total fare:{self.fare+self.tax}')
    def display(self):
        print(f'Type:{self.type}')
        return super().display()
    
t1 = Transport(12, 200, 'punetomumbai', 100)
r1 = Roadtransport(1234, 4, 'punetomumbai', 'Car', 200, 5)
a1 = Airtransport(23, 2, 'nsktopune', 'Helicopter', 4000, 500)

t1.Calfare()
r1.Calfare()
a1.Calfare()