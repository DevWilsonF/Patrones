from abc import ABC, abstractmethod
from copy import copy, deepcopy

class Employee(ABC):
    
    def __init__(self):
        self.__description__ = ""
        self.__name__ = ""
        self.__boss__ = None

    def hello(self):
        return f'Job Offer: {self.__name__},\n\
        Description: {str(self.__description__)}.\n\
        Your boss is: {self.__boss__.get_name()}\n'

    def set_boss(self, boss):
        self.__boss__ = boss;

    def get_boss(self):
        return self.__boss__
    
    def change_boss(self, name):
        self.__boss__.set_name(name)

    def set_description(self, description):
        self.__description__ = description;
    
    def get_description(self):
        return self.__description__

    def get_name(self):
        return self.__name__

    def set_name(self, name):
        self.__name__ = name;

    def clone(self):
        return deepcopy(self)
        
        
        class Junior(Employee):
    pass


class Senior(Employee):
    pass

class Expert(Employee):
    pass

class Boss():

    def __init__(self, name):
        self.__name__ = name

    def get_name(self):
        return self.__name__;
    
    def set_name(self, name):
        self.__name__ = name;
