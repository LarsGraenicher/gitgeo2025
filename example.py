class Vector3:
    def __init__(self,x,y,z):
        self._x=x
        self._y=y
        self._z=z

    def setX(self, x):
        self.x=x

    def getX(self):
        return self._x
    
    def setY(self, y):
        self._y=y

    def getY(self):
        return self._y

    def setZ(self, z):
        self._z=z

    def getZ(self):
        return self._z

    x=property(getX,setX)       #dafür da das man direkt mit x auf die geter und seter zugreifen kann
    y=property(getY,setY)
    z=property(getZ,setZ)

    def __add__(self, addVector):
        return Vector3(self.x+addVector.x, self.y+addVector.y, self.z+addVector.z)
    
    def __iadd__(self, addVector):
        return self.__add__(addVector)
    
    def __mul__(self, multiplicator):
        return Vector3(self.x*multiplicator, self.y+multiplicator, self.z+multiplicator)
    def __invert__(self):
        return self*-1
    

    #rest auf moodle

class Plane:
    def __init__(self, v0,v1):
        self._v0 =v0
        self._v1=v1
    
    def setV0(self, v0):
        self._v0=v0
    
    def getV0(self):
        return self._v0

    def setV1(self, v1):
        self._v1=v1
    
    def getV1(self):
        return self._v1  

    v0=property(getV0,setV0) 
    v1=property(getV1,setV1)


v0=Vector3(1,0,0)
v1=Vector3(0,1,0)

p=Plane(v0, v1)

print(p.v0)