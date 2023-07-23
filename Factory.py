"""ChatGPT Definition : 
The Factory Design Pattern is a creational design pattern
    that provides an interface for creating objects in a 
    super class but allows the subclasses to alter the 
    type of objects that will be created. It is used to
    create objects without specifying the exact class of 
    the object that will be created, allowing the client 
    code to interact with the created objects through a 
    common interface."""
    
class Dog :
    """Simple Dog class"""
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        return "Woof!"
    
    def get_pet(pet="dog"):
        """The Factory method"""
        
        pets = dict(dog=Dog("Hope"))
        return pets[pet]
    
class Cat :
    """Simple Cat class"""
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        return "Meow!"
    
def get_pet(pet="dog"):
    """The Factory method"""
    
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())