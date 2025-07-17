import astropy.units as u
from numbers import Integral,Real

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
    
    @property
    def density(self) -> u.Quantity[u.kg / u.m**2]:
        return self.weight / self.area


class Car(Vehicle):

    def __init__(self,
                 weight: u.Quantity[u.kg],
                 length: u.Quantity[u.m],
                 width : u.Quantity[u.m],
                 engine_size: u.Quantity[u.liter] = 1.0 * u.liter
                 ):
        super().__init__(weight, length, width)
        self.engine_size = engine_size

    
    
class Bike(Vehicle):

    def __init__(self,
                 weight: u.Quantity[u.kg],
                 length: u.Quantity[u.m],
                 width : u.Quantity[u.m],
                 number_of_gears: float = 10
                 ):
        super().__init__(weight, length, width)
        self._number_of_gears = 10

        self.number_of_gears = number_of_gears

    @property
    def number_of_gears(self) -> int:
        return self._number_of_gears    
    
    @number_of_gears.setter
    def number_of_gears(self, value: int):
        if not (isinstance(value,Integral) and value >= 1):
            raise ValueError("Number of gears must be an int and at least 1.")
        self._number_of_gears = value

