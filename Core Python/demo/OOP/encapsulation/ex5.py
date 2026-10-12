class Weather:
    def __init__(self, temp, humidity, location):
        self.temp = temp
        self.humidity = humidity
        self.location = location
        
    def getTemp(self):
        return self.temp
    def setTemp(self, newid):
        self.temp = newid
        
    def getHumidity(self):
        return self.humidity
    def setHumidity(self, newid):
        self.humidity = newid
        
    def getLocation(self):
        return self.location
    def setLocation(self, newid):
        self.location = newid
        
    def display(self):
        print(f'Temp:{self.temp}\tHumidity:{self.humidity}\tLocation:{self.location}')
    
w1 = Weather(10, 19, 'pune')
w2 = Weather(39, 40, 'mumbai')
w1.display()
w2.display()
w1.setLocation('nashik')
w1.display()