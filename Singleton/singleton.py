class Conecction:
    __instance= None

    def __new__(cls):
        if cls.__instance is None:
            print('Conectado')
            cls.__instance = \
                super(Conecction,cls).__new__(cls) 
        return cls.__instance



if __name__ == '__main__':
    conecction1 = Conecction()
    conecction2 = Conecction()
    admin1=Conecction()
    admin2= Conecction()
    print(conecction1 is conecction2)
    print(admin1 is admin2)
    print (conecction1 is admin1)