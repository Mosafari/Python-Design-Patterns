"""ChatGPT Definition : 
    The Composite design pattern is a structural design pattern that allows you
    to compose objects into tree-like structures to represent part-whole hierarchies.
    It lets clients treat individual objects and compositions of objects uniformly.

    In this pattern, there are two main components:

    1.Component: This is the base interface or abstract class that declares common operations
    for both simple and complex objects in the composition. It defines operations that are 
    applicable to individual objects and their compositions.

    2.Composite: This is a class that represents the complex objects in the composition. It 
    implements the Component interface and contains a collection of child components. The 
    Composite class provides methods to add, remove, and access child components.

    3.Leaf: This is a class that represents the simple objects in the composition. It also 
    implements the Component interface but does not have children.

    The key idea of the Composite pattern is that the client code can interact with both 
    individual objects and compositions uniformly. It can treat a leaf (simple object) and 
    a composite (complex object) interchangeably through the common Component interface."""
    
class Component(object):
	"""Abstract class"""

	def __init__(self, *args, **kwargs):
		pass

	def component_function(self):
		pass

class Child(Component): #Inherits from the abstract class, Component
	"""Concrete class"""

	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		#This is where we store the name of your child item!
		self.name = args[0]

	def component_function(self):
		#Print the name of your child item here!
		print("{}".format(self.name))

class Composite(Component): #Inherits from the abstract class, Component
	"""Concrete class and maintains the tree recursive structure"""

	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		#This is where we store the name of the composite object
		self.name = args[0]

		#This is where we keep our child items
		self.children = []

	def append_child(self, child):
		"""Method to add a new child item"""
		self.children.append(child)

	def remove_child(self, child):
		"""Method to remove a child item"""
		self.children.remove(child)

	def component_function(self):

		#Print the name of the composite object
		print("{}".format(self.name))

		#Iterate through the child objects and invoke their component function printing their names
		for i in self.children:
			i.component_function()

#Build a composite submenu 1
sub1 = Composite("submenu1")

#Create a new child sub_submenu 11
sub11 = Child("sub_submenu 11")
#Create a new Child sub_submenu 12
sub12 = Child("sub_submenu 12")

#Add the sub_submenu 11 to submenu 1
sub1.append_child(sub11)
#Add the sub_submenu 12 to submenu 1
sub1.append_child(sub12)

#Build a top-level composite menu
top = Composite("top_menu")

#Build a submenu 2 that is not a composite
sub2 = Child("submenu2")

#Add the composite submenu 1 to the top-level composite menu
top.append_child(sub1)

#Add the plain submenu 2 to the top-level composite menu
top.append_child(sub2)

#Let's test if our Composite pattern works!
top.component_function()

"""ChatGPT Example:
    Here's a simple example of the Composite design pattern in Python:"""

from abc import ABC, abstractmethod

# Component (abstract class or interface)
class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

# Leaf (simple object)
class Circle(Graphic):
    def draw(self):
        print("Drawing a circle")

# Leaf (simple object)
class Square(Graphic):
    def draw(self):
        print("Drawing a square")

# Composite (complex object)
class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def draw(self):
        for graphic in self.graphics:
            graphic.draw()

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)

# Client code
circle = Circle()
square = Square()

composite = CompositeGraphic()
composite.add(circle)
composite.add(square)

composite.draw()
"""
    In this example, we have a base Graphic interface (Component), two simple objects Circle and Square
    (Leaf), and a complex object CompositeGraphic (Composite) that can hold multiple Graphic objects. 
    The client code treats both the simple objects and the composite object uniformly through the Graphic 
    interface. When we call the draw() method on the composite object, it will call the draw() method of 
    each child object it contains.

    The Composite pattern is useful when you have a part-whole hierarchy, and you want to treat individual 
    objects and compositions uniformly, making it easier to work with complex structures."""