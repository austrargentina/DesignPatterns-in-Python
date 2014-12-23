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

    def create(self, numWords):
        LegacyRoman.create(self, numWords/1000) #1000 Wörter pro Seite

    def publish(self, booktype):
        if booktype is "Horror":
            LegacyRoman.publish(self, "Hardcover")
        elif booktype is "Thriller":
            LegacyRoman.publish(self, "Softcover")

class LegacyRoman(object):

    def create(self, numPages):
        """
        Test
        :param numPages:
        :return:
        """
        print("Ein Buch mit %d Seiten wurde erstellt" %numPages)

    def publish(self, coverArt):
        print("Das Buch wurde mit einem %s gepublished" %coverArt)

x = Roman();
x.create(10000)
x.publish("Horror")

x.create(10000000)
x.publish("Thriller")