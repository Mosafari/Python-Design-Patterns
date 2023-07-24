"""ChatGPT Definition :
    The Observer design pattern is a behavioral design pattern that allows an 
    object (known as the subject) to notify multiple dependent objects (known as observers)
    automatically when its state changes. It promotes loose coupling between the subject and
    the observers, enabling them to interact without needing to know each other's details.

    In Python, the Observer pattern can be implemented using various techniques, including
    custom implementations and using built-in modules like observable and observer from the tkinter
    library. I'll explain a custom implementation of the Observer pattern in Python:

    Define the Subject (Observable):
    The subject is the object whose state changes are of interest to the observers. It maintains
    a list of its dependent observers and provides methods to add, remove, and notify observers.

    Define the Observer:
    Observers are objects that are interested in receiving updates from the subject. 
    They must implement an update method to respond to the state changes.

    Implement the Custom Observer Pattern:
    Create a custom class for the Subject and another custom class for the Observer.
    In the Subject class, maintain a list of observers, and provide methods to manage
    the list (e.g., add_observer, remove_observer). When the state of the subject changes,
    call the update method of all registered observers to notify them."""


class Subject(object): #Represents what is being 'observed'

	def __init__(self):
		self._observers = [] # This where references to all the observers are being kept
							 # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers

	def attach(self, observer):
		if observer not in self._observers: #If the observer is not already in the observers list
			self._observers.append(observer) # append the observer to the list

	def detach(self, observer): #Simply remove the observer
		try:
			self._observers.remove(observer)
		except ValueError:
			pass

	def notify(self, modifier=None):
		for observer in self._observers: # For all the observers in the list
			if modifier != observer: # Don't notify the observer who is actually updating the temperature 
				observer.update(self) # Alert the observers!

class Core(Subject): #Inherits from the Subject class

	def __init__(self, name=""):
		Subject.__init__(self)
		self._name = name #Set the name of the core
		self._temp = 0 #Initialize the temperature of the core

	@property #Getter that gets the core temperature
	def temp(self):
		return self._temp

	@temp.setter #Setter that sets the core temperature
	def temp(self, temp):
		self._temp = temp
		self.notify() #Notify the observers whenever somebody changes the core temperature

class TempViewer:

	def update(self, subject): #Alert method that is invoked when the notify() method in a concrete subject is invoked
		print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))

#Let's create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

#Let's create our observers
v1 = TempViewer()
v2 = TempViewer()

#Let's attach our observers to the first core
c1.attach(v1)
c1.attach(v2)

#Let's change the temperature of our first core
c1.temp = 80
c1.temp = 90

