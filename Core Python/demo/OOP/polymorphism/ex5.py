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
        
    def Totaltemp(self):
        print(f'Total temperature:{self.temp}')
    
    def display(self):
        print(f'Temp:{self.temp}\tHumidity:{self.humidity}\tLocation:{self.location}')
        
#Weather class ends here.....................

class Rainy(Weather):
    def __init__(self, temp, humidity, location, rainfall, cold):
        super().__init__(temp, humidity, location)
        self.rainfall = rainfall
        self.cold = cold
    def getRainfall(self):
        return self.rainfall
    def setRainfall(self, newid):
        self.rainfall = newid
    def Totaltemp(self):
        print(f'Total temperature:{self.temp-self.cold}')
    def display(self):
        print(f'Rainfall:{self.rainfall}')
        return super().display()
    
#Rainfall class ends here.................

class Winter(Weather):
    def __init__(self, temp, humidity, location, fog, cold):
        super().__init__(temp, humidity, location)
        self.fog = fog
        self.cold = cold
    def getFog(self):
        return self.fog
    def setFog(self, newid):
        self.fog = newid
    def Totaltemp(self):
        print(f'Total temperature:{self.temp-self.cold}')
    def display(self):
        print(f'Fog:{self.fog}')
        return super().display()
    
#Winter class ends here......................

w1 = Weather(23, 31, 'Pune')
r1 = Rainy(30, 30, 'Nashik', 123, 12)
wi1 = Winter(20, 19, 'Dhule', 30, 18)

w1.Totaltemp()
r1.Totaltemp()
wi1.Totaltemp()