import logging
from abc import ABC, abstractmethod
from typing import List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        ...


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        ...

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        ...


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU Spec")


if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    us_car = us_factory.create_car("Ford", "Mustang")
    us_car.start_engine()            

    eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1200")
    eu_motorcycle.start_engine()