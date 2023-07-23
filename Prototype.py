"""ChatGPT Definition : 
    The Prototype design pattern in Python is a creational pattern that
    allows you to create new objects by copying or cloning existing objects
    known as prototypes. This pattern promotes object creation by cloning 
    rather than using traditional constructors.

    Key components of the Prototype pattern:

    1.Prototype: An abstract class or interface that declares the clone() method.
    It serves as the base for all concrete prototype classes.

    2.ConcretePrototype: Implementations of the Prototype interface.
    These classes define their own cloning logic.

   3. Client: Initiates the cloning process by requesting the prototype
    to create a new instance."""
    
import copy

class Prototype:
    """  Prototype """
    def __init__(self):
        self._objects = {}
        
    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj
        
    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]
        
    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj
        
class Car:
    """ ConcretePrototype """
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"
        
    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)
   
""" Client """     
c = Car()
prototype = Prototype()
prototype.register_object('skylark',c)

c1 = prototype.clone('skylark')

print(c1)
