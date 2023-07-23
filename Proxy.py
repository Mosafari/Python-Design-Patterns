"""ChatGPT Definition : 
    The Proxy design pattern in Python is a structural design 
    pattern that provides a surrogate or placeholder for another 
    object. It acts as an intermediary or a wrapper, controlling 
    access to the real object and allowing additional functionality 
    to be added without changing the underlying object's code. 
    The primary purpose of using the Proxy pattern is to control 
    access, enhance performance, or implement lazy loading.

    Key Concepts:

    1.Subject: This is the interface that defines the common methods
    or functionalities that both the RealSubject and Proxy implement.
    It acts as the contract that the Proxy must adhere to.

    2.RealSubject: This is the actual object that the Proxy represents
    and controls access to. It contains the real functionality that 
    the Proxy might enhance or modify.

    3.Proxy: This is the class that follows the Subject interface and 
    holds a reference to the RealSubject. It can add additional 
    functionalities or control access to the RealSubject methods."""

import time

class Producer:
	"""Define the 'resource-intensive' object to instantiate!"""
	def produce(self):
		print("Producer is working hard!")

	def meet(self):
		print("Producer has time to meet you now!")

class Proxy:
	""""Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""
	def __init__(self):  
		self.occupied = 'No'
		self.producer = None

	def produce(self):
		"""Check if Producer is available"""
		print("Artist checking if Producer is available ...")

		if self.occupied == 'No':
			#If the producer is available, create a producer object!
			self.producer = Producer()
			time.sleep(2)

			#Make the prodcuer meet the guest!
			self.producer.meet()
			
		else:
			#Otherwise, don't instantiate a producer 
			time.sleep(2)
			print("Producer is busy!")

#Instantiate a Proxy
p = Proxy()

#Make the proxy: Artist produce until Producer is available
p.produce()

#Change the state to 'occupied'
p.occupied = 'Yes'

#Make the Producer produce
p.produce()

"""ChatGPTExample:
    Let's take an example of an image viewer application that 
    loads high-resolution images. To improve the performance, 
    we use a proxy to load the image only when required and 
    cache it for future access.
"""

# Subject (interface)
class ImageViewer:
    def display_image(self):
        pass

# RealSubject
class HighResImageViewer(ImageViewer):
    def __init__(self, image_path):
        self._image_path = image_path
        self._load_image()

    def _load_image(self):
        print(f"Loading high-resolution image from {self._image_path}")

    def display_image(self):
        print(f"Displaying high-resolution image from {self._image_path}")

# Proxy
class ProxyImageViewer(ImageViewer):
    def __init__(self, image_path):
        self._image_path = image_path
        self._real_viewer = None

    def display_image(self):
        if not self._real_viewer:
            self._real_viewer = HighResImageViewer(self._image_path)
        self._real_viewer.display_image()

# Usage
image_path = "image.jpg"

# Using Proxy to display the image (loading happens only when required)
proxy_viewer = ProxyImageViewer(image_path)
proxy_viewer.display_image()  # Output: Loading high-resolution image from image.jpg\nDisplaying high-resolution image from image.jpg

# The second time we display the image, it uses the cached RealSubject
proxy_viewer.display_image()  # Output: Displaying high-resolution image from image.jpg

"""
    In this example, ImageViewer is the subject interface, HighResImageViewer is 
    the real subject that loads the high-resolution image, and ProxyImageViewer is 
    the proxy that acts as a placeholder for the real subject. When the display_image()
    method is called on the ProxyImageViewer, it checks if the real viewer exists. If not,
    it creates the HighResImageViewer (real subject) and then delegates the method call to it.
    Subsequent calls to display_image() reuse the cached real viewer, improving performance by
    loading the image only when needed.
    """