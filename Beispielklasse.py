

class Person:
    def __init__(self, name, age): #silliobjekt ist die Person und unten packen wir erst die Attribute hinein
        self.name=name 
        self.age=age
        self.getname()          #das die Funktion immer aufgerufen wird direkt
        print("Object:", self.myname)

    def getname(self):
        print("My Name is:", self.name)


p1= Person("John", 36)
p2= Person("Eve", 20)

