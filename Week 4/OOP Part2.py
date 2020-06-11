# Writing Classes and Methods
# Writing Classes 

# Create our own class:
class Dog (object):
    # a class must have a body, even if it does nothing, so we will
    # use 'pass' for now...
    pass

# Create instances of our class
d1 = Dog()
d2 = Dog()

# Verify the type of these instances:
print(type(d1))
print(isinstance(d2, Dog))

# Set and get properties (aka 'fields' or 'attributes')
#   of these instances:
d1.name = 'Dot'
d1.age = 4
d2.name = 'Elf'
d2.age = 3

print(d1.name, d1.age)
print(d2.name, d2.age)

# Writing Constructors 
## Constructors let us pre-load our new instances with
##   properties
class Dog(object):
    def __init__(self, name, age):
        # pre-load the dog instance with the given name and age:
        self.name = name
        self.age = age
 
# Create instances of our class, using our new constructor
d1 = Dog('Dot', 4)
d2 = Dog('Elf', 3)

print(d1.name, d1.age) # Dot 4
print(d2.name, d2.age) # Elf 3

# Writing Method
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Now we are using self, as convention requires:
    def sayHi(self):
        print(f'Hi, my name is {self.name} and I am {self.age} years old!')

d1 = Dog('Dot', 4)
d2 = Dog('Elf', 3)

# Notice how we change the function calls into method calls:

d1.sayHi() # Hi, my name is Dot and I am 4 years old!
d2.sayHi() # Hi, my name is Elf and I am 3 years old!

class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This method takes a second parameter -- times
    def bark(self, times):
        print(f'{self.name} says: {"woof!" * times}')

d = Dog('Dot', 6)

d.bark(1) # Dot says: woof!
d.bark(4) # Dot says: woof!woof!woof!woof!

class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.woofCount = 0   # we initialize the property in the constructor!

    def bark(self, times):
        # Then we can set and get the property in this method
        self.woofCount += times
        print(f'{self.name} says: {"woof!" * times} ({self.woofCount} woofs!)')

d = Dog('Dot', 4)

d.bark(1) # Dot says: woof!
d.bark(4) # Dot says: woof!woof!woof!woof!

# Advantages of Classes and Methods
## Encapsulation
### organizes codes
#### a class inclues the data and the method
### promotes intuitive design
#### well-designed classes should be intuitive, so the
####   data and methods in the class match commonsense
####   expectations
### Restrict access
## Polymorphism
### The same method name can run different code based
###   on type, liek so: 
class Dog(object):
    def speak(self):
        print('woof!')

class Cat(object):
    def speak(self):
        print('meow!')

for animal in [ Dog(), Cat() ]:
    animal.speak() # same method name, but one woofs and one meows!