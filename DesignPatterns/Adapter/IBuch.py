__author__ = 'Daniel'
from abc import *

class IBuch(object):
    ___metaclass__ = ABCMeta

    @abstractmethod
    def create(self, numWords):
        """
        Erstellt ein neues Buch, anhand Anzahl der geschriebenen Wörter
        :param numWords: Anzahl der geschriebenen Wörter
        :return:
        """
        return

class Roman(IBuch):

    def create(self, numWords):
        print(str(numWords))
        return numWords

x = IBuch()
print(x.create(1))