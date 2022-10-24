class Computer:
    def getspecs(self):
        self.processor=str(input("Enter the processor: "))
        self.os=str(input("Enter the operating system"))
        self.ram=str(input("Enter the RAM capacity"))
        self.storage=str(input("Enter the internal storage capacity"))
        self.speed=str(input("Enter the processor speed"))
        self.monitor=str(input("Enter the monitor specifications"))
    def displayspecs(self):
        print("\n.......Specifications........")
        print("Processor(CPU):",self.processor)
        print("Operating System:",self.os)
        print("RAM:",self.ram)
        print("Internal Storage:",self.storage)
        print("Processor Speed:",self.speed)
        print("Monitor Specifications:",self.monitor)
class Desktop(Computer):
    def getspecs_desktop(self):
        self.ups=str(input("Enter UPS specification(in VA)"))
        self.warranty=str(input("Enter the warranty period"))
    def displayspecs_desktop(self):
        print("UPS:",self.ups)
        print("Warranty:",self.warranty)
class Laptop(Computer):
    def getspecs_laptop(self):
        self.brand=str(input("Enter the laptop brand name"))
        self.weight=str(input("Enter the weight of laptop in Kg"))
    def displayspecs_laptop(self):
        print("Brand:",self.brand)
        print("Laptop Weight",self.weight)
lp = Laptop()
pc=Desktop()
lp.getspecs()
lp.getspecs_laptop()
pc.getspecs()
pc.getspecs_desktop()
lp.displayspecs()
lp.displayspecs_laptop()
pc.displayspecs()
pc.displayspecs_desktop()
