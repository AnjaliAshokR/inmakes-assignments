class pgm:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __mul__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return (x,y)
obj1=pgm(5,6)
obj2=pgm(6,5)
print(obj1*obj2)