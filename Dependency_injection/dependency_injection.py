class Monitor:
    pass

class Computadora:
    def __init__(self):
       self.monitor= Monitor()# <-- dependency
    
class Config:
    def __init__(self, database, user, password, host, port):
        self.database = database
        self.username = username
        self.password = password

        self.host= host
        self.port = port


class DataBaseConnect:
    def __init__(self, config: Config):
       self.config= Config

development = Config('pywombat', 'root', 'password', 'localhost', 2207)

production = Config('pywombat', 'superadmin', 'password', '157.245.120.121', 2207)

testing= Config('pywombat', 'test', 'password', '157.245.120.121', 2207)        

connect = DataBaseConnect(development)
connect = DataBaseConnect(production)
connect = DataBaseConnect(testing)        
