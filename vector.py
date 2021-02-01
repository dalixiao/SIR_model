class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector( self.x + other.x , self.y + other.y )

    def __sub__(self,other):
        return Vector( self.x - other.x  , self.y - other.y )

    def __mul__(self,val):
        return Vector(self.x*val, self.y*val)
    @property
    def length(self):
        return float( ((self.x)**2 + (self.y) ** 2) ** (1/2) )

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y


    def unify(self):
        return Vector(  self.x / self.length, self.y / self.length )


    def copy(self):
        return Vector(self.x,self.y)
