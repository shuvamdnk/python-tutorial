class Car:
    def __init__(self, company, color):
        self.company = company
        self.color = color

    @classmethod
    def car_details(cls, company, color):
        return cls(company, color)


audi = Car.car_details("Audi", 'red')
print(audi.color)           
print(audi.__dict__)
print(audi)