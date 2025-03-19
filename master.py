class Temperature:
    def __init__(self,temperature):
        self._temperature = temperature

    def setTemperature(self, temperature):
        self._temperature = temperature

    def getTemperature(self):
        return self._temperature
        
    def __str__(self):
        return f"Celsius: {self._temperature}"
        
    def __int__(self):
        return 1
        
    def __float__(self):
        return float(self._temperature)
        
    def __add__(self, addValue):
        return Temperature(self._temperature + float(addValue))
        
    temperature = property(getTemperature, setTemperature)

    def __gt__(self, compareValue):
        return float(self) > float(compareValue)
        
    def __lt__(self, compareValue):
        return float(self) < float(compareValue)
        
t0=Temperature(50)
t1=Temperature(100)


print(t0>t1)   #er nimmt grundsätzlich den String