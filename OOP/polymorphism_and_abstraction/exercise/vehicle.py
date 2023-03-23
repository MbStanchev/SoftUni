from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self,  fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIRCON = 0.9

    def drive(self, distance):
        consumption = (self.fuel_consumption + Car.AIRCON) * distance
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIRCON = 1.6

    def drive(self, distance):
        consumption = (self.fuel_consumption + Truck.AIRCON) * distance
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
