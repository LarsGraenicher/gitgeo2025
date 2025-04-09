# Unsere Person Klasse
class Person:
    def __init__(sillyobject, var_name, var_age):
        sillyobject.name = var_name
        sillyobject.age = var_age
        sillyobject.getname()
        print("sillyobject :", sillyobject)
        
    #def __str__(self):
    #    """Output when printing an instance of a Pet."""
    #    return f"object name {self.name} object age {self.age}"
    
    def myfunc(silly_abc):
        print("silly_abc   :", silly_abc)


    def getname(self):
        print("Hello my name is " + self.name)


# Erstelle zwei Personen mit Namen und Alter (def __init__)
p1 = Person("John", 36)
#p2 = Person("Eve", 20)

#p1.myfunc() # wir geben der Funktion nichts mit
##p2.myfunc()
#p1.getname()
#print("This is my object: ", p1.name)
#print("This is my object: ", p1.getname())
#
