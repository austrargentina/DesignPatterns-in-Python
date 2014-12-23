__author__ = 'Daniel'
from abc import abstractmethod, ABCMeta


class Palatschinke(object, metaclass=ABCMeta):
    """
    Interface Palatschinke
    """
    def getPrice(self):
        """
        Gibt den zu zahlenden Wert zurück
        :return: Preis in €
        """
        pass

    def getName(self):
        """
        Gibt den Namen des Objekts zurueck
        """
        pass

class EisPalatschinke(Palatschinke):
    """
    Erbt von Palatschinke
    """
    def getPrice(self):
        """
        Gibt den zu zahlenden Wert zurück (3€)
        :return: Preis in €
        """
        return 3

    def getName(self):
        """
        Gibt den Namen der Palatschinke zurück
        :return: Name der Palatschinke
        """
        return "Palatschinke mit Eis"

class MarmeladenPalatschinke(Palatschinke):
    """
    Erbt von Palatschinke
    """
    def getPrice(self):
        """
        Gibt den zu zahlenden Wert zurück (3€)
        :return: Preis in €
        """
        return 2

    def getName(self):
        """
        Gibt den Namen der Palatschinke zurück
        :return: Name der Palatschinke
        """
        return "Palatschinke mit Marmelade"

class PalatschinkenFactory(object):
    """
    Ist die Factory, die je nach gewünschter Art eine andere Palatschinke erzeugt
    """
    @staticmethod
    def createPalatschinke(art):
        """
        Erzeugt ein neues Palatschinkenobjekt, je nach gewünschter art
        :param art: Art der gewünschten Palatschinke
        :return:
        """
        palatschinke = None
        if art is "marmelade":
            palatschinke = MarmeladenPalatschinke()
        elif art is "eis":
            palatschinke = EisPalatschinke()
        else:
            print("Eine Palatschinke mit %s homma ned!" %art)

        if palatschinke is not None:
            print("Eine %s, das macht dann €%d!" %(palatschinke.getName(), palatschinke.getPrice()))

PalatschinkenFactory.createPalatschinke("marmelade")
PalatschinkenFactory.createPalatschinke("eis")
PalatschinkenFactory.createPalatschinke("mehl")