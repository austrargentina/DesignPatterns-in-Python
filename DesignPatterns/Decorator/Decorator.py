from abc import abstractmethod

__author__ = 'Isabella'

class PizzaBase():
    """
    Stellt eine Pizza da.
    """
    @abstractmethod
    def getDescription(self):
        pass

class Decorator(PizzaBase):
    """
    Der Decorator erbt von PizzaBase
    """

    pizza = PizzaBase()
    @abstractmethod
    def getDescription(self):
        pass

class Mozzarella(Decorator):
    pizza = ""

    def __init__(self,newpizza):
        self.pizza=self.getDescription(newpizza)

    def getDescription(self,newpizza):
        return  print("New Pizza with "+ newpizza + '+ Mozzarella')

class PizzaBasePizza(PizzaBase):
    """
    Diese Klasse verwendet PizzaBase
    """
    desc = ""

    def __init__(self, desc):
        self.desc = self.getDescription(desc)

    def getDescription(self):
        pass

    print('%s' % Mozzarella("Schinken "))




