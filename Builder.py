"""ChatGPT Definition : 
    The Builder design pattern in Python is a creational pattern
    that separates the construction of a complex object from its
    representation. It allows you to create different representations
    of an object step-by-step by using the same construction process.

    Key components of the Builder pattern:

    1.Product: Represents the complex object to be created.

    2.Builder: An abstract interface that defines the steps required to 
    build the product. It typically includes methods for creating parts
    of the product.

    3.ConcreteBuilder: Implements the Builder interface and provides specific
    implementations for building the product.

    4.Director: Controls the construction process using the Builder object.
    It hides the complexity of the product's creation from the client.

    5.Client: Initiates the construction of the product using the Director.
    """

class Director():
    """Director"""
    def __init__(self, builder):
        self._builder = builder 
        
    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()
        
    def get_car(self):
        return self._builder.car
        
        
 
class Builder():
    """Abstract Builder"""
    def __init__(self):
        self.car = None 
        
    def create_new_car(self):
        self.car = Car()
        


class SkyLarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts """
    
    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):    
        self.car.engine = "Turbo engine"

class Car():
    """Product"""
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None
        
    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)

builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)