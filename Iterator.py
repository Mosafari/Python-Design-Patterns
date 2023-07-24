"""ChatGPT Definition :
    The Iterator design pattern is a behavioral design pattern that provides
    a way to access elements of a collection sequentially without exposing 
    the underlying representation of the collection. It allows you to traverse
    a collection (such as a list, array, or tree) in a standardized manner, 
    regardless of its internal structure. In Python, the Iterator pattern is 
    implemented using the built-in iter() function and the __iter__() and __next__() methods.

    Here's a basic explanation of the components of the Iterator design pattern in Python:

    Iterable (Aggregate):

    This represents the collection or container that can be iterated over.
    It defines the __iter__() method, which returns an iterator object.
    Iterator:

    This is the object responsible for traversing the elements of the Iterable.
    It defines the __next__() method, which returns the next element in the collection
    and raises the StopIteration exception when there are no more elements to iterate over.

    The typical steps to use the Iterator pattern in Python are as follows:

    Create an Iterable (collection) class that implements the __iter__() 
    method and returns an Iterator object.

    Create an Iterator class that implements the __next__() method to provide 
    iteration logic over the elements of the Iterable.

    Use the Iterable's __iter__() method to get an Iterator object and use 
    the __next__() method to access elements of the collection sequentially."""
    
def count_to(count):
	"""Our iterator implementation"""
	
	#Our list
	numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

	#Our built-in iterator
	#Creates a tuple such as (1, "eins")
	iterator = zip(range(count), numbers_in_german)
	
	#Iterate through our iterable list
	#Extract the German numbers
	#Put them in a generator called number
	for position, number in iterator:
		
		#Returns a 'generator' containing numbers in German
		yield number 

#Let's test the generator returned by our iterator
for num in count_to(3):
	print("{}".format(num))

for num in count_to(4):
	print("{}".format(num))
	
""" ChatGPT Example:
    Here's a simple example in Python:"""

class Numbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            self.start += 1
            return self.start - 1

# Create an Iterable object
numbers = Numbers(1, 5)

# Get an Iterator object using iter()
iterator = iter(numbers)

# Access elements using next()
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  # Output: 4
print(next(iterator))  # Output: 5
# Further calls to next() will raise StopIteration

# or with for loop : (to avoid StopIteration)
numbers2 = Numbers(1,6)
for i in numbers2:
    print(i)
    

""" The Iterator pattern is helpful when you want to decouple the traversal logic
    from the collection, making it easy to change or extend the iteration behavior without
    modifying the collection's implementation."""