__author__ = 'Daniel'

from abc import ABCMeta, abstractmethod

class IBuch(object,metaclass = ABCMeta):

    @abstractmethod
    def create(self, numWords):
        """
        Erstellt ein neues Buch, anhand Anzahl der geschriebenen Wörter
        :param numWords: Anzahl der geschriebenen Wörter
        :return:
        """
        pass

    def publish(self, booktype):
        """
        Published ein Buch und setzt das Cover anhand des Büchtyps
        :param booktype: Art des Buches (Thriller, Horror)
        :return:
        """
        pass

class Roman(IBuch):
    """
    Klasse Roman, die den Adapter darstellt, da sie das Mittelstück zwischen der 'alten' Klasse
    Legacy Roman und dem neuen Kunden ist
    """

    def create(self, numWords):
        """
        Rechnet die übergebenen Wörter in Seiten um, um so die 'alte' Klasse zu speisen.
        :param numWords: Anzahl der geschriebenen Wörter
        :return:
        """
        LegacyRoman.create(self, numWords/1000) #1000 Wörter pro Seite

    def publish(self, booktype):
        """
        Setzt anhand des Buchtyps das gewünschte Cover, um so die 'alte' Klasse zu speisen.
        :param booktype: Art des Buches (Thriller, Horror)
        :return:
        """
        if booktype is "Horror":
            LegacyRoman.publish(self, "Hardcover")
        elif booktype is "Thriller":
            LegacyRoman.publish(self, "Softcover")

class LegacyRoman(object):
    """
    Adaptierte Klasse LegacyRoman, die nach 'altem' Prinzip funktioniert.
    """

    def create(self, numPages):
        """
        Erzeugt einen Roman, mit einer bestimmten Anzahl an Seiten.
        :param numPages: Anzahl der Seiten
        :return:
        """
        print("Ein Buch mit %d Seiten wurde erstellt" %numPages)

    def publish(self, coverArt):
        """
        Published einen Roman, mit einer bestimmten Coverart.
        :param coverArt:
        :return:
        """
        print("Das Buch wurde mit einem %s gepublished" %coverArt)

x = Roman();
x.create(10000)
x.publish("Horror")

x.create(10000000)
x.publish("Thriller")