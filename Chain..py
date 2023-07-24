"""
    The Chain of Responsibility design pattern is a behavioral design pattern that
    allows multiple objects to handle a request without specifying the receiver
    explicitly. Instead of a sender directly calling a specific receiver, the pattern
    creates a chain of objects (usually implemented as a linked list), each having a 
    chance to process the request. If one object cannot handle the request, it passes 
    the request to the next object in the chain until the request is handled or the end 
    of the chain is reached.

    Key components of the Chain of Responsibility design pattern in Python:

    1.Handler (Handler Interface):
    This is the interface or base class that defines the common method(s) for handling the request.
    It contains a reference to the next handler in the chain.
    
    2.Concrete Handlers:
    These are the different implementations of the Handler interface.
    Each concrete handler decides whether it can handle the request or not. If it can, it processes
    the request; otherwise, it passes the request to the next handler in the chain.

    3.Client:
    This is the class that initiates the request and starts the chain.
    The client is unaware of which handler will process the request."""

class Handler: #Abstract handler
	"""Abstract Handler"""
	def __init__(self, successor):
		self._successor = successor # Define who is the next handler

	def handle(self, request):
			handled = self._handle(request) #If handled, stop here

			#Otherwise, keep going
			if not handled:
				self._successor.handle(request)	

	def _handle(self, request):
		raise NotImplementedError('Must provide implementation in subclass!')

class ConcreteHandler1(Handler): # Inherits from the abstract handler
	"""Concrete handler 1"""
	def _handle(self, request):
		if 0 < request <= 10: # Provide a condition for handling
			print("Request {} handled in handler 1".format(request))
			return True # Indicates that the request has been handled

class DefaultHandler(Handler): # Inherits from the abstract handler
	"""Default handler"""

	def _handle(self, request):
		"""If there is no handler available"""
		#No condition checking since this is a default handler
		print("End of chain, no handler for {}".format(request))
		return True # Indicates that the request has been handled

class Client: # Using handlers
	def __init__(self):
		self.handler = ConcreteHandler1(DefaultHandler(None)) # Create handlers and use them in a sequence you want
		                                                      # Note that the default handler has no successor

	def delegate(self, requests): # Send your requests one at a time for handlers to handle
		for request in requests:
				self.handler.handle(request)

# Create a client
c = Client()

# Create requests
requests = [2, 5, 30]

# Send the requests
c.delegate(requests)
