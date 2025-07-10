import astropy.units as u

class Vehicle:

    def __init__(self,
                 weight: u.Quantity[u.kg],
                 length: u.Quantity[u.m],
                 width : u.Quantity[u.m]
                 ):
        self.weight = weight
        self.length = length
        self.width = width

    @property
    def area(self)-> u.Quantity[u.m**2]:
        return self.width * self.length


class Car(Vehicle):

    def __init__(self,
                 weight: u.Quantity[u.kg],
                 length: u.Quantity[u.m],
                 width : u.Quantity[u.m]
                 ):