__author__ = 'Isabella'

class OnlyOne:
    class __OnlyOne:

        """
        Der Konstruktor von der inneren Klasse __OnlyOne
        """
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None

    """
    Der Konstruktor der OnlyOne Klasse. Es wird geschaut ob OnlyOne eine Instanz hat,
    ha sie noch keine wird eine neue Instanz erzeugt.
    """
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    """
    Diese Methode gibt ein Attribut zurück.
    """
    def __getattr__(self, name):
        return getattr(self.instance, name)

x = OnlyOne('sausage')
print(x)
y = OnlyOne('eggs')
print(y)
z = OnlyOne('spam')
print(z)
print(x)
print(y)
