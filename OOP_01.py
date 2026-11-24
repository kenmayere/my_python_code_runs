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

print('Hello')