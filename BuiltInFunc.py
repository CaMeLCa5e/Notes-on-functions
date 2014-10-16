"""
Standard Library Built-in functions
"""

abs() 
#Returns absolute value

all()
Return True if all elements in iterable are True
def all(iterable)
	for element in interable:
		if not element:
			return False
	return True
	
any()
def any(iterable)
	for element in iterable:
		if element:
			return True
	return False
	
basestring()
#superclass for str and unicode used for testing

bin()
#convert an int to a binary string.  if x =! int need to define __index__() to return an int. 

bool()
#class.  Returns True or False 

bytearray()
Return a new array of bytes.  the bytearray class is a mutable sequence of integers in the range 0<= x <256
It has most of the usual methods of mutable sequences as well as str() methods

callable()
Return True if argument appears callable.  False if not.  

chr()
return a string of one character whose ASCII code is the inteder i. 


classmethod()
receives class as implicit argument. 
class C(object):
	@classmethod
	def f(cls, arg1, arg2, ...)
	
	
cmp()
compare two objects  (takes, a, touple) and return an int according to the outcome.  

compile()
turn code into object. 

complex()
return a complex number made from ([real[,imag]])

delattr()
(del attr) deletes named attr.  

dict()
Dictionary

dir()

divmod()
take two complex numbers and return a pair of their quotient and remainder. 
takes a touple argument 

enumerate()
Return an enumerate object. sequence an iterator or some object that supports iteration.  
seasons = ["Spring", "Summer", "Fall", "Winter"]
list(enumerate(seasons))
list(enumerate(seasons, start=1))

def enumerate(sequence, start = 0):
	n = start
	for elem in sequence:
		yield n, elem 
		n+=1
		
eval()
evaluate or = 
x = 1
print eval("x + 1")

execfile()
similar to exec() but it parses to a file instead of a string. 

file()
same as open()

filter(func, iterable)
Construct a list from elements of iterable for  which function returns true.  returns tuple or string depending on input

float()
get dat '.'


format()
convert value to "formatted" representation.  

format(value, format_spec) == value.__format__(format_spec)

frozenset()
set type- "frozen set module" uses elements taken from the iterable

getattr(obj, name, [,default])  ##why is the ',' inside the []? why wouldn't it be listed-
getattr(obj, name[default])? maybe because this is a str and it is for mutable obj?

globals()
return dict representing current global symbol. 

hasattr()
has attr- returns True or False

hash()
return the value of the object.  ints are always returned.  I feel like the data could get messy with this.  

help()


hex()
Hexidecimal string prefix!! 
hex(255)
hex(-42)
hex(1L)

id()
returned as int() number that is assigned to object. 

input()
input() == eval(raw_input(prompt))

int()
return integer object

isinstance()
return true if object argument is an instance of class argument.  

issubclass()
return True if class is a subclass...  

iter()
return an iterator object. 
with open('mydata.txt') as fp:
	for line in iter(fp.readline, ""):
		process_line(line)
		
len()
length

list()
this is a class- []

locals()
update and return a {}
	
long()
return a long int.  

map(func, iterable)
apply func to all iterables and return a [] of results. 

max()
largest argument within (),[],{}

memoryview()
return object. memory view. 

min()
return smallest value possible

next()
call the next method 

object()

oct()
convert int to octal string

open()

ord()
return int() with unicode

pow()
to the ^ power-  returns power. 

print()

property()
returns class property
class c(object):
	def__init__(self):
		self._x = None
	def getx(x):
		return self._x
	def setx(self, value):
		self._x = value
	def delx(self):
		del self._x
	x = property(getx, setx, delx "The 'x' property")
	
class Parrot(object):
	def __init__(self):
		self._voltage = 10000
		
		@property
		def voltage(self):
			"""get current voltage"""
			return self._voltage
			
class C(object):
	def__init__(self):
		self._x= None
		
		@property
		def x(self):
			"""the 'x' """
			return self._x
		@x.setter
		def x(self, value):
			self._x = value
			
		@x.deleter
		def x(self):
			del self._x
			
			
range()
start + end + step 

raw_input()
takes input from user

reduce()
def reduce(func, iterable, initializer = None):
	it = iter(iterable)
		if initializer is None:
			try:
				initializer = next(it)
			except StopIteration:
				raise TypeError("reduce() of empty sequence")
		accum_value = initializer
		
		for x in it:
			accum_value = function(accum_value, x)
		return accum_value
		
reload()
all code is recompiled. 

try:
	cache
except NameError:
	cache = {}
	
repr()
reversed()
round()
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
tuple()
type()
unichr()
unicode()
vars()
xrange()
zip()
__import__()
apply()
buffer()
coerce()
intern()

