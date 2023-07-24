"""ChatGPT Definition :
    The Visitor design pattern is a behavioral design pattern that allows you
    to add new behaviors to a group of related classes without modifying their
    implementation. It achieves this by separating the algorithms (visitor) from
    the object structure (elements). The pattern is useful when you have a complex
    object structure with a fixed set of classes, and you want to add new operations
    or behaviors to these classes without modifying their code.

    Key Components of the Visitor Pattern:

    Visitor: The Visitor class defines the new operation or behavior that can be applied
    to the elements of the object structure. It declares visit methods for each element
    type. Each visit method corresponds to a specific operation for a particular element
    type.

    Element: The Element interface represents the elements of the object structure. 
    It defines an accept method that takes a visitor as an argument. The accept method
    is responsible for dispatching the call to the appropriate visit method of the visitor.

    ConcreteElement: The ConcreteElement classes are the specific elements of the object
    structure. They implement the Element interface and define their own behavior for 
    the accept method.

    ObjectStructure: The ObjectStructure represents the collection of elements that 
    the visitor can visit. It provides a way to iterate through the elements and call 
    their accept method."""

class House(object): #The class being visited 
	def accept(self, visitor):
		"""Interface to accept a visitor"""
		visitor.visit(self) #Triggers the visiting operation!

	def work_on_hvac(self, hvac_specialist):
		print(self, "worked on by", hvac_specialist) #Note that we now have a reference to the HVAC specialist object in the house object!

	def work_on_electricity(self, electrician):
		print(self, "worked on by", electrician) #Note that we now have a reference to the electrician object in the house object!

	def __str__(self):
		"""Simply return the class name when the House object is printed"""
		return self.__class__.__name__


class Visitor(object):
	"""Abstract visitor"""
	def __str__(self):
		"""Simply return the class name when the Visitor object is printed"""
		return self.__class__.__name__


class HvacSpecialist(Visitor): #Inherits from the parent class, Visitor
	"""Concrete visitor: HVAC specialist"""
	def visit(self, house):
		house.work_on_hvac(self) #Note that the visitor now has a reference to the house object


class Electrician(Visitor): #Inherits from the parent class, Visitor
	"""Concrete visitor: electrician"""
	def visit(self, house):
		house.work_on_electricity(self) #Note that the visitor now has a reference to the house object

#Create an HVAC specialist
hv = HvacSpecialist()
#Create an electrician
e = Electrician()

#Create a house
home = House()

#Let the house accept the HVAC specialist and work on the house by invoking the visit() method
home.accept(hv)

#Let the house accept the electrician and work on the house by invoking the visit() method
home.accept(e)
