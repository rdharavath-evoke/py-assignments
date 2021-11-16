#Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
# It describes the idea of wrapping data and the methods that work on data within one unit. 
# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
# To prevent accidental change, an object’s variable can only be changed by an object’s method. 
# Those types of variables are known as private variable. 

# Creating a base class
class Base:
	def __init__(self):
		
		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):
		
		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling protected member of base class: ")
		print(self._a)

obj1 = Derived()
		
obj2 = Base()

# Calling protected member
# Outside class will result in
# AttributeError
print(obj2)
