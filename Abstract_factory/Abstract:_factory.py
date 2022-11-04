import abc
class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_item_a(self):
        pass

    @abc.abstractmethod
    def create_item_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_item_a(self):
        return ConcreteitemA1()

    def create_item_b(self):
        return ConcreteitemB1()

class ConcreteFactory2(AbstractFactory):
    def create_item_a(self):
        return ConcreteitemA2()

    def create_item_b(self):
        return ConcreteitemB2()
    
class AbstractitemA(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface_a(self):
        pass

class ConcreteitemA1(AbstractitemA):
    def interface_a(self):
        pass

class ConcreteitemA2(AbstractitemA):
    def interface_a(self):
        pass

class AbstractitemB(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface_b(self):
        pass

class ConcreteitemB1(AbstractitemB):
    def interface_b(self):
        pass

class ConcreteitemB2(AbstractitemB):
    def interface_b(self):
        pass

def main():
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        item_a= factory.create_item_a()
        item_b = factory.create_item_b()
        item_a.interface_a()
        item_b.interface_b()

if __name__ == "__main__":
    main()
