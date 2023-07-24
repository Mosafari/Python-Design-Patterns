"""ChatGPT Definition : 
    The Adapter design pattern in Python is a structural design pattern that
    allows incompatible interfaces of two or more classes to work together. 
    It acts as a bridge between these classes by converting the interface of 
    one class into an interface that the client code expects. It helps in reusing
    existing classes with different interfaces without modifying their source code.

    Key Concepts:

    1.Target: This is the interface that the client code expects to interact with. 
    It defines the operations that the client code can use to achieve its functionality.

    2.Adaptee: This is the existing class with an incompatible interface that we want 
    to use in the client code. It contains the functionality that the client code needs 
    but with a different interface.

    3.Adapter: This is the class that implements the Target interface and wraps the Adaptee. 
    It acts as a bridge between the client code and the Adaptee, translating the client's 
    requests into calls that Adaptee can understand.
"""
class Korean:
	"""Korean speaker"""
	def __init__(self):
		self.name = "Korean"

	def speak_korean(self):
		return "An-neyong?"

class British:
	"""English speaker"""
	def __init__(self):
		self.name = "British"	

	#Note the different method name here!
	def speak_english(self):
		return "Hello!"	

class Adapter:
	"""This changes the generic method name to individualized method names"""

	def __init__(self, object, **adapted_method):
		"""Change the name of the method"""
		self._object = object

		#Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
		#For example, speak() will be translated to speak_korean() if the mapping says so
		self.__dict__.update(adapted_method)

	def __getattr__(self, attr):
		"""Simply return the rest of attributes!"""
		return getattr(self._object, attr)
		
#List to store speaker objects
objects = []

#Create a Korean object
korean = Korean()

#Create a British object
british = British()

#Append the objects to the objects list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))


for obj in objects:
	print("{} says '{}'\n".format(obj.name, obj.speak()))


"""ChayGPT Example:
    Let's consider a simple example of a temperature converter application
    that converts temperatures between Celsius and Fahrenheit. We have an 
    existing CelsiusTemperature class with a different interface than the 
    client code expects. We create an adapter class to make the CelsiusTemperature
    class compatible with the client's expected interface.
"""

# Target interface
class TemperatureConverter:
    def convert(self, value):
        pass

# Adaptee with an incompatible interface
class CelsiusTemperature:
    def get_temperature(self):
        return 0

# Adapter
class CelsiusToFahrenheitAdapter(TemperatureConverter):
    def __init__(self, celsius_temperature):
        self._celsius_temperature = celsius_temperature

    def convert(self, celsius_value):
        # Call the Adaptee's method to get Celsius temperature
        celsius_temp = self._celsius_temperature.get_temperature()
        # Convert Celsius to Fahrenheit and return
        return (celsius_value * 9/5) + 32

# Client code
if __name__ == "__main__":
    # Creating an instance of Adaptee (CelsiusTemperature)
    celsius_temp = CelsiusTemperature()
    # Creating an instance of Adapter and passing the Adaptee instance to it
    converter = CelsiusToFahrenheitAdapter(celsius_temp)

    # Client code expects to work with the Target interface
    celsius_value = 25
    fahrenheit_value = converter.convert(celsius_value)
    print(f"{celsius_value} Celsius is equal to {fahrenheit_value} Fahrenheit")
    
"""In this example, TemperatureConverter is the target interface that the client code expects
    to use for temperature conversion. CelsiusTemperature is the Adaptee with an incompatible interface,
    providing the Celsius temperature. We create the CelsiusToFahrenheitAdapter class, which implements 
    the TemperatureConverter interface and wraps the CelsiusTemperature instance. The convert() method in
    the adapter translates the client's request for Fahrenheit conversion into the corresponding Celsius 
    temperature from the Adaptee and then converts it to Fahrenheit. The client code works with the 
    TemperatureConverter interface, allowing seamless temperature conversion using the existing 
    CelsiusTemperature class without modifying its original interface."""