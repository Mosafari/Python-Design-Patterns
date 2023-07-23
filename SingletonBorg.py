"""ChatGPT explanation:
    The design pattern used in the given code snippet is a
    combination of the Borg Pattern and the Singleton Pattern.

    1. Borg Pattern:
    The Borg Pattern is used in the `Borg` class, which makes the 
    class attributes global across all instances of the class. It 
    achieves this by sharing the same attribute dictionary 
    `_shared_data` among all instances. When a new instance of the
    `Borg` class is created, its `__dict__` is set to the shared 
    attribute dictionary `_shared_data`, so any modification to 
    the attributes in one instance will affect all other instances.
    This pattern allows multiple instances to share state while still
    having separate instances of the class.

    2. Singleton Pattern:
    The `Singleton` class inherits from the `Borg` class, which means 
    it shares the same attribute dictionary among all instances, just 
    like the Borg pattern. However, it adds the concept of a singleton 
    object, which means that only one instance of the `Singleton` class 
    can exist throughout the application. It achieves this by using the 
    Borg pattern's shared attributes to store the data specific to the 
    singleton object.

    In the given code, the `Singleton` class acts as a singleton object 
    with a shared attribute dictionary `_shared_data`, and each instance 
    of `Singleton` updates this dictionary when initialized with keyword 
    arguments. The `__str__` method is used to print the shared attribute 
    dictionary, showing the data stored in it.

    This combined pattern ensures that multiple instances of `Singleton` 
    can exist, and they will share a common state through the `_shared_data` 
    attribute dictionary. However, the essence of the Singleton pattern is 
    that the application should create and work with only one instance of `Singleton`,
    and any subsequent attempts to create new instances will refer to the same instance 
    already created."""

class Borg:
    """Borg pattern making the class attributes global"""
    _shared_data = {} # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data # Make it an attribute dictionary

        
class Singleton(Borg): #Inherits from the Borg class
    """This class now shares all its attributes among its various instances"""
    #This essenstially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs) # Update the attribute dictionary by inserting a new key-value pair 

    def __str__(self):
        return str(self._shared_data) # Returns the attribute dictionary for printing

#Let's create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
# Print the object
print(x) 

#Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym.
y = Singleton(SNMP="Simple Network Management Protocol")
# Print the object
print(y)
