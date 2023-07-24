"""ChatGPT Definition : 
    The Bridge design pattern is a structural design pattern that decouples an abstraction
    from its implementation, allowing them to vary independently. It is used to solve the 
    problem of class explosion (having a large number of class combinations) that can occur 
    when trying to handle multiple variations of a class.

    In the Bridge pattern, there are two main components:

    1.Abstraction: This is the high-level abstraction that defines the interface for the client code.
    It contains a reference to the Implementor interface.

    2.Implementor: This is the low-level implementor interface that defines the interface for concrete
    implementors. It allows different implementations to be used interchangeably by the Abstraction.

    The key idea of the Bridge pattern is to separate the abstract class from its implementation, 
    allowing them to change independently. This promotes flexibility and allows new abstractions and
    implementors to be added without modifying the existing code."""

class DrawingAPIOne(object):
	"""Implementation-specific abstraction: concrete class one"""
	def draw_circle(self, x, y, radius):
		print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawingAPITwo(object):
	"""Implementation-specific abstraction: concrete class two"""
	def draw_circle(self, x, y, radius):
		print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))

class Circle(object):
	"""Implementation-independent abstraction: for example, there could be a rectangle class!"""

	def __init__(self, x, y, radius, drawing_api):
		"""Initialize the necessary attributes"""
		self._x = x
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api

	def draw(self):
		"""Implementation-specific abstraction taken care of by another class: DrawingAPI"""
		self._drawing_api.draw_circle(self._x, self._y, self._radius)

	def scale(self, percent):
		"""Implementation-independent"""
		self._radius *= percent


#Build the first Circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
#Draw a circle
circle1.draw()

#Build the second Circle object using API Two
circle2 = Circle(2, 3, 4, DrawingAPITwo())
#Draw a circle
circle2.draw()

""" ChatGPT Explanation(for cource example):
    The Bridge pattern is used to decouple an abstraction (Circle class) from its 
    implementation (DrawingAPIOne and DrawingAPITwo classes). It allows both abstractions
    and implementations to vary independently.

    In this snippet, we have two sets of classes:

    Abstraction: Circle class
    Implementor: DrawingAPIOne and DrawingAPITwo classes

    The Circle class is the abstraction and provides an interface for the clients
    to interact with the drawing API without being concerned about the specific 
    implementation details. It has a reference to the DrawingAPI interface.

    The DrawingAPIOne and DrawingAPITwo classes are the concrete implementations that
    provide specific drawing functionality. They both implement the draw_circle() 
    method with different implementations.

    The Circle class is initialized with the x, y, radius, and a specific DrawingAPI 
    instance (either DrawingAPIOne or DrawingAPITwo). The draw() method of the Circle 
    class then delegates the drawing task to the appropriate DrawingAPI instance, 
    depending on which implementation was passed during initialization."""