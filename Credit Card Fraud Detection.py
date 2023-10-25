class Car:
    def __init__(self,model,year,milage):
        self.model=model
        self.year=year
        self.milage=milage

    def get_descriptives(self):
        print(f"This car is of model{self.model} made in the year{self.year}")


    def get_milage(self):
        print(f"This car has travelled upto {self.milage} miles.")


class ElectricCar(Car):
    def __init__(self,make,engine,charging_time,driving_range,braking_system):
        self.make=make
        self.engine=engine
        self.charging_time=charging_time
        self.driving_range=driving_range
        self.braking_system=braking_system


    def car_summary(self):
       print( "Make:",self.make)
       print("Engine:",self.engine)
       print("Charging_time:", self.charging_time)
       print("Driving_Range:",self.driving_range)
       print("Braking Sytem:",self.braking_system)


my_car=ElectricCar("Tesla","Induction Motor","7 hours","124-235 miles","Regenerative Braking System")
my_car.car_summary()
