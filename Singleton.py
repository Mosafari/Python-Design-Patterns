"""ChatGPT Definition:
    The Singleton Design Pattern is a creational design 
    pattern that ensures a class has only one instance 
    and provides a global point of access to that instance. 
    It is commonly used when you want to restrict the instantiation 
    of a class to a single object to control shared resources or 
    configuration settings."""
    
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage:
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Output: True (Both s1 and s2 refer to the same instance)
"""ChatGPT explanation:
    In this example, the Singleton class has a class variable _instance, which 
    holds the single instance of the class. The __new__ method is overridden to 
    ensure that the class creates only one instance. If the _instance variable 
    is None, it creates a new instance using the super() method. Otherwise, it 
    returns the existing instance.

    The Singleton class can now be instantiated, but it will always return the 
    same instance. This way, no matter how many times you create an object of 
    the Singleton class, you will always get the same instance, ensuring that 
    only one instance of the class exists throughout the application.

    It's important to note that while the Singleton pattern provides a single 
    global instance, it does not prevent creating other instances through other 
    means (e.g., using reflection or multiprocessing). The implementation shown 
    above is a simple and thread-safe approach, but in multi-threaded scenarios, 
    you may need to implement additional synchronization mechanisms to ensure thread safety.
"""