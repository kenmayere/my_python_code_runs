# --------------------------- Exploring Object Oriented Programming -----------------

''' 
In this script, I will explore some of the basics in OOP, I will explore the following:
    1. Defining classes and creating objects
    2. Instance class methods and attribute functions
    3. Class methods
'''

# ---------- Concepts and Terms ---------
'''
In python, one is not required to to use objects and classes (everthing in python is an object). However, as programs become more complex,
it is had to have them organized. This is where Object Oriented Programming is essential.

----- Why is it important ----
    1. OOP keep code structrured and organized: It groups data and behavior (actions) in one place
    2. Promotes modularization of programs: Changing part of of the program does not affect the entire program or it does with little effect
    3. Isolates different parts from each other

----- Key terms --------------
    1. Class: This is a blueprint or template for creating objects of a particular type
    2. Methods: Regular functions that are part of a class
    3. Attributes: Variables that hold data inside of a class
    4. Object: A specific instance of a class
    5. Inheritance: Means by which a class can inherit capabilities from another
    6. Composition: Means of building complex objects out of their objects

OK! Lets now start to build and explore >>

'''

# --------- Defining classes and creating objects ------
'''
Creating a class, required 'Class' key word followed by the class name conventionally with a n upper first letter.
The class can have parenthesis after the name when it is inheriting capabilities from another class, otherwise, its optional.
Creating an instance of the class (object) involves assigning a class call as calling a function of the class to the object name.
'''
# Creating a class
class Book:
    pass

# __init__ function
'''
The dunder init function is used as an initializer function to initialize the new object with information.
This is different from a constructor function used to build objects.
This is because in pyhton an object is created when an instance is called. For example, creating a class and object to contain title,
author, pages and price.
'''
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

# Creating b1 object
b1 = Book('Introduction to Python', 'Kenford', 280, 25.60)
'''
Why is the first argument 'self', because whenever a method is passed on a python
object, the object automatically gets passed as the first argument
'''

# Instance methods and attribute for a class
# Let me add a function to get a price for any book

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def getprice(self):
        return self.price

b2 = Book('Intro to Python', 'Kenford', 280, 25.84)
# Calling the getprice method
print(b2.getprice())

# Let me further add a discount method, that takes in an amount
# I will just here create the logic of the method and comment it later, will modify the code
 
    # def getdiscount(self, amount):
    #     self._amount = amount

''' Using self._amount as in the code logic above defines a method that can be 
used within the class defining it, not for the public - cannot be inherited.
Since the attribute (amount) was not defined in the __init__ method, I will use the 'hasattr'
function to test for it.
'''
# The modified code will be
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    def getprice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    def getdiscount(self, amount):
        self._discount = amount

b3 = Book('Intro to Python', 'Kenford', 280, 25.84)
print(b3.getprice())
b3.getdiscount(0.25)
print(b3.getprice())

# Checking instance types using an additional class: Newspaper
class Newspaper:
    def __init__(self, name):
        self.name = name

n1 = Newspaper('The Nation')
n2 = Newspaper('The Daily Times')

print(type(b1)) # Result in <class 'Book'>
print(type(n1)) # Result in <class 'Newspaper'>

'''
But a more intutive way is to use 'isistance' which checks if an object 
is of a particula class, it evaluates to a bool. This means I can make comparisions'''
print(isinstance(b3, Book))

# -------- Class attributes and  methods ----------------
'''
Class attributes are shared across all the instances of the class, different with instance attributes
which are only shared in that instance.
In the following example, I will explore the class- and static methods
'''
class Book:
    BOOK_TYPES = ('HARDCOPY', 'PAPERBACK', 'EBOOK')

    @classmethod
    def get_book_type(cls):
        return cls.BOOK_TYPES
    
    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f'{booktype} is not a valid booktype')
        else:
            self.booktype = booktype

b5 = Book('Title5', 'HARDCOPY')
b6 = Book('Title6', 'EBOOK')

'''
In the above code logic, a few things are happening:
    1. I have created BOOK_TYPES class attribute meaning it can be usable
    across all the instance methods.
    2. I have created the class method using the @classmethod decorator. This will take in the
    class as its argument and it is allowine me to access the class attributes
    3. Cool staff using the if-statement as a way of creating an instance method attribute
'''
# Using static methods

# Static methods do not have any arguments. I will modify the code above and explain later on

class Book:
    BOOK_TYPES = ('HARDCOPY', 'PAPERBACK', 'EBOOK')

    @classmethod
    def get_book_type(cls):
        return cls.BOOK_TYPES

    __booklist = None

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError (f'{booktype} is not a valid booktype')
        else:
            self.booktype = booktype

    def get_book_list():
        if Book.__booklist == None:
            Book.__booklist = []
            return Book.__booklist

'''
In the above code, a few things are happening:
    1. I have added a class attribute __booklist. It contains 2 underscores
    meaning it will be private.
    2. The get_book_list method is a static method since it doesnt take in any argument
    3. Interesting how the static method has been used in this class
    '''

# Adding books to the list, remember booklist is an empty list.

thebooks = Book.get_book_list()
b5 = Book('Title5', 'HARDCOPY')
b6 = Book('Title6', 'EBOOK')
thebooks.append(b5)
thebooks.append(b6)


# Just to wrap up, I have isolated the static method just to explore further on how it works
# Ofcourse not very useful
class Movie:
    __movielist = None

    def get_movie_list():
        if Movie.__movielist == None:
            Book.__movielist = []
            return Book.__movielist

movie_list = Movie.get_movie_list()
movie_list.append('Action 1')

movie_list

# ------------------- End of Chapter ---------------------
