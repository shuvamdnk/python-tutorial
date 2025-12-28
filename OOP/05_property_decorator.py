class Car:
    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed - 10
    
    @speed.setter
    def speed(self, speed):
        if speed <= 200:
            self._speed = speed
        else:
            raise ValueError("Speed Limit is 200")    
        
bmw = Car(100)

print(bmw.speed)
bmw.speed = 180
print(bmw.speed)