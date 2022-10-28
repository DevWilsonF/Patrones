# class Conecction(object):
#     __instance= None
#     def __new__(cls):
#         if Conecction.__instance is None:
#             print('Conectado')
#             Conecction.__instance = object.__new__(cls)
#         return Conecction.__instance
from multiprocessing import connection
import re


def singleton(cls):
    instance= dict()
    def add (*args,**kargs):
        if cls not in instance:
            instance[cls]= cls(*args,**kargs)
        return instance[cls]
    return add
@singleton
class Conecction(object):
    def __init__(self,username):
        self.username=username

if __name__ == '__main__':
    conecction1 = Conecction("auser1")
    conecction2 = Conecction("user2")
    admin1=Conecction()
    admin2= Conecction()
    print(conecction1 is conecction2)
    print(admin1 is admin2)
    print (conecction1 is admin1)