"""ChatGPT Definition :
    The Strategy design pattern is a behavioral design pattern that allows you
    to define a family of algorithms (strategies), encapsulate each one of them, 
    and make them interchangeable at runtime. This pattern enables the client to 
    choose the appropriate strategy to use without modifying its context. In Python,
    the Strategy pattern can be implemented using classes and polymorphism.

    Key components of the Strategy design pattern in Python:

    Context:
    This is the class that maintains a reference to the chosen strategy and 
    acts as an interface to the client code.
    It contains a method to set the strategy and a method that delegates 
    the work to the strategy.
                                                                        # in this example context is in the strategy class
    Strategy (Strategy Interface):
    This is the interface or base class that defines the common method(s) 
    that all concrete strategies must implement.

    Concrete Strategies:
    These are the different implementations of the Strategy interface, 
    representing various algorithms or behaviors.
    Each concrete strategy provides its own implementation of the common method(s)."""

import types #Import the types module

class Strategy:
    """The Strategy Pattern class"""
    
    def __init__(self, function=None):
        self.name = "Default Strategy"
        
        #If a reference to a function is provided, replace the execute() method with the given function
        if function:
        	self.execute = types.MethodType(function, self)
            
    def execute(self): #This gets replaced by another version if another strategy is provided.
        """The defaut method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))

#Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))

#Replacement method 2    
def strategy_two(self):
	print("{} is used to execute method 2".format(self.name))
    
#Let's create our default strategy
s0 = Strategy()
#Let's execute our default strategy
s0.execute()

#Let's create the first varition of our default strategy by providing a new behavior
s1 = Strategy(strategy_one)
#Let's set its name
s1.name = "Strategy One"
#Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()