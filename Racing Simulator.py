import random
import time

class Car:

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.fuel = 100
        self.performance = 50
        self.credits = 0

    def car_info(self):
        print("============= YOUR 🏎️ CAR ===============")
        print(f"{self.make} {self.model} {self.year}"
              f"fuel: {self.fuel} Car Performance: {self.performance}")