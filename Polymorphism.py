""" ChatGPT Definition : 
    Polymorphism in Python refers to the ability of different objects to be
    treated as if they have the same interface or behavior, even though they may
    belong to different classes or types. It allows objects of different types to
    be used interchangeably in a way that is transparent to the user.

    Polymorphism is achieved through method overriding and method overloading:

    1. Method Overriding: It occurs when a subclass provides a specific implementation
    for a method that is already defined in its parent class. The subclass method "overrides"
    the behavior of the parent class method while keeping the same method signature. This allows
    the same method call to produce different results based on the type of object being used.
"""

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.speak()  # Output: Dog barks
cat.speak()  # Output: Cat meows

"""
    2. Method Overloading: In Python, method overloading is not directly supported 
    like in some other programming languages. However, Python allows you to define 
    multiple methods with the same name in a class, but with different numbers or 
    types of parameters. The appropriate method is selected based on the number and
    types of arguments provided when the method is called.
"""

class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

math_ops = MathOperations()

# print(math_ops.add(2, 3))        # Error: only the second add method is available
print(math_ops.add(2, 3, 5))     # Output: 10

"""
    Note: Method overloading in Python can be achieved indirectly through the use of 
    default arguments or variable-length arguments (e.g., `*args`, `**kwargs`). In 
    the example above, only the second `add` method is available, as Python only 
    considers the last defined method with the same name."""