"""ChatGPT Definition : 
    The decorator design pattern in Python is a structural design pattern
    that allows you to add new behavior or functionalities to an object 
    dynamically. It involves wrapping an object within another object 
    (decorators) to provide additional functionalities without modifying 
    its structure. Decorators are commonly used in Python using the "@" 
    syntax, making it easy to apply them to functions or methods.

    Key Concepts:

    1.Component: This is the interface that defines the common methods or 
    functionalities that both the concrete component and decorators implement.
    
    2.Concrete Component: This is the original object that you want to 
    enhance with additional functionalities.
    
    3.Decorator: This is the abstract class that follows the component 
    interface and contains a reference to the component object. It 
    acts as the base class for all decorators and maintains a reference 
    to the wrapped component.
    
    4.Concrete Decorators: These are the actual decorators that extend 
    the decorator class and add specific functionalities to the wrapped component."""


from functools import wraps

def make_blink(function):
	"""Defines the decorator"""

	#This makes the decorator transparent in terms of its name and docstring
	@wraps(function)

	#Define the inner function
	def decorator():
		#Grab the return value of the function being decorated
		ret = function() 

		#Add new functionality to the function being decorated
		return "<blink>" + ret + "</blink>"

	return decorator

#Apply the decorator here!
@make_blink
def hello_world():
	"""Original function! """

	return "Hello, World!"

#Check the result of decorating
print(hello_world())

#Check if the function name is still the same name of the function being decorated
print(hello_world.__name__)

#Check if the docstring is still the same as that of the function being decorated
print(hello_world.__doc__)

"""ChatGPT Example:
    Let's take an example of a coffee shop, where we have a basic coffee and decorators
    to add toppings like milk, sugar, and chocolate.
"""

# Component (interface)
class Coffee:
    def cost(self):
        pass

# Concrete Component
class BasicCoffee(Coffee):
    def cost(self):
        return 10

# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 5

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

class ChocolateDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3

# Usage
my_coffee = BasicCoffee()
my_coffee_with_milk_sugar = MilkDecorator(SugarDecorator(my_coffee))
my_coffee_with_all_toppings = ChocolateDecorator(my_coffee_with_milk_sugar)

print("Cost of Basic Coffee:", my_coffee.cost())  # Output: 10
print("Cost with Milk and Sugar:", my_coffee_with_milk_sugar.cost())  # Output: 17 (10 + 5 + 2)
print("Cost with All Toppings:", my_coffee_with_all_toppings.cost())  # Output: 20 (10 + 5 + 2 + 3)
"""
    In this example, Coffee is the component interface, BasicCoffee is the concrete component,
    CoffeeDecorator is the abstract decorator, and MilkDecorator, SugarDecorator, and ChocolateDecorator
    are concrete decorators. Each decorator adds its specific cost to the wrapped component's cost, 
    effectively enhancing the functionality of the basic coffee object."""
