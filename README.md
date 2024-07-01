# Object-Oriented-Programming
Object-oriented programming developed as a way to organize code for data structures. 

The data managed in the structure is kept in an **object**. The object is also called an **instance** of a class of objects.
Object classes define specific **methods** that implement operations on the object instances.
The methods are common to all objects in the class and operate on the data specific to each instance.

Python defines classes of objects with the _class_ statement.
The _def_ statements define methods and assignment statements define class attributes.
The first parameter of each defined method should be _self_. The self parameter holds the object instance, allowing methods to call other instance methods and reference instance attributes.

To define the constructor for object instances, there should be a def __init__() statement inside the class definition. Like the other methods, __init__() should accept self as its first parameter. The __init__() method takes the empty instance and performs any needed initialization like creating instance variables and setting their values (and doesn’t need to return self like constructors do in other languages).

_Reference: "Data Structures & Algorithms in Python"_
by John Canning, Alan Broder and Robert Lafore



