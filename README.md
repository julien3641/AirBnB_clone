# AirBnB_clone

![AirBnB clone logo.](/img/logo_airbnb.png "AirBnB Clone logo.")

##Introduction

![first step](/img/intro1.png "First step")

This project is the first step of a big one witch is to clone the AirBnB full web application.
 * This first step is in python. We will start by implement the parent class called BaseModel.
 * This class do the initialization, serialization and deserialization of the future instances : Instance <-> Dictionary <-> JSON string <-> file
 * During this project, we created some classes that inherit from BaseModel such as : User, State, City, Place, review, state, amenity...
 * Create the first abstracted storage engine of the project: File storage.
 * And to finish create the unittest to validate all the classes and storage processes

##Definitions

First lets have some few definitions to help understand the project :

* __What is a Python package ?__

A Python package is a folder containing modules and maybe other folders that themselves may contain more folders and modules. A package folder usually contains one file named __init__.py that basically tells Python: “Hey, this directory is a package!” The init file may be empty, or it may contain code to be executed upon package initialization.

* __Why use the command interpreter in Python ?__

The Cmd instance or subclass instance is a line-oriented interpreter framework. There is no good reason to instantiate Cmd itself; rather, it’s useful as a superclass of an interpreter class you define yourself in order to inherit Cmd’s methods and encapsulate action methods.

* __How to manage datetime ?__

To manage datetime in python, you have to import the module named datetime. This module allow you to deal with the hours or the dates

* __What is a UUID what can it be used for?__

UUIDs are generally used for identifying information that needs to be unique within a system or a network.

* __What is *args and how to use it ?__

The special syntax "*args" in function definitions in python is used to pass a variable number of arguments to a function.

* __What is **kwargs and how to use it ?__

Kwargs allow you to pass keyword arguments to a function. They are used when you are not sure of the number of keyword arguments that will be passed in the function. Kwargs can be used for unpacking dictionary key, value pairs. This is done using the double asterisk notation ( ** ).

* __How to handle named arguments in a function ?__

Keyword arguments (or named arguments) are values that, when passed into a function, are identifiable by specific parameter names. A keyword argument is preceded by a parameter and the assignment operator, = . Keyword arguments can be likened to dictionaries in that they map a value to a keyword.

##Use the console

The (hbnb) Airbnb Clone can be run both in interactive and non-interactive mode.
To run the console in non-interactive mode, you can use the following command :

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
You can use the interactive mode with the following command :

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

##Main commands


| COMMAND after the (hbnb)                               |                 DESCRIPTION                  |
|--------------------------------------------------------|:--------------------------------------------:|
| quit                                                   |             To quit the console              |
| EOF                                                    |          To quit the console by EOF          |
| help + command                                         |     Display the help for the command ask     |
| create + class                                         |      Creates an object and print the ID      |
| show + class + id                                      |    To show the informations of the object    |
| destroy + class + id                                   |             To remove an object              |
| all + class                                            |     To show all the instances of a class     |
 | update + class + id + attribute name + attribute value | To create or update the attribute of a class |

##BaseModel

The BaseModel class is the parent of all the classes : 

* The _init method_ defines the common attributes for all the class that inrherite from that one. We call that the constructor method.

* The _str method_ is the method that defines the good output format as a string.

* The _save method_ is useful to updates the public instance attribute 'updated_at' with
        the current datetime.

* The _to_dict method_ returns a dictionary containing all the keys and values of the instance.

##Other classes
All the classes listed bellow inherits from BaseModel :

| class       |                                                                   Attributes                                                                   |
|-------------|:----------------------------------------------------------------------------------------------------------------------------------------------:|
| User        |                                                   email + password + first_name + last_name                                                    |
| State       |                                                                      name                                                                      |
| City        |                                                                state_id + name                                                                 |
| Place       | city_id + user_id + name + description<br/>number_rooms + number_bathrooms + max_guest<br/>price_by_night + latitude + longitude + amenity_ids |
| Review      |                                                           place_id + user_id + text                                                            |
| Amenity     |                                                                      name                                                                      |






##Filestorage

This file is composed of methods that are used by the console :
* The _all method_ display the dictionary view of objects.

* The _new method_ sets a new instance with the class name and a new id for the object.

* The _save method_ serialize the object in dictionary format to the JSON file.

* The _reload method_ deserialize the JSON file to object. In other words, bring the data in the file.json and change it to object.

##Console

The HBNBCommand class is created to implement the prompt. The option "do" at the beginning of the method define the action. So do_quit defined the command to quit the prompt, the EOF do the same with the signal.

* The _method do_create_ is to create a new instance and tell the user if there is a missing argument or if the class called doesn't exist. If the argument are passed on the good way, the instance is created and saved.

* The _method do_show_ is to show a sring representation of an instance. This mean that when you type : "show User id" on the good way it will display the information of this user. If a argument is missing it will display an error message.

* The _method do_destroy_ works on the same way as "show" but the objective is to remove an instance.

* The _method do_all_, display in the prompt the string representation of all the instance saved.

* The _method do_update_ have to be exactly "update + class + id + attribute name + attribute value ". This method is useful to update an instance. If the instance already exist, it updates the instance and the time. It the instance doesn't exist it create it.

##Python Unit Tests

We have done some tests for our classes and methods. Tests are made to make sure our code display the result and the outputs expected.

The command to Display the results of the tests in interactive mode is :
```
$ python3 -m unittest discover tests
```
And the command in non-interactive mode is :
```
echo "python3 -m unittest discover tests" | bash
```
