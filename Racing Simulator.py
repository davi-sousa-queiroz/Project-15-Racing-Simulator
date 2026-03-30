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

    def race(self):
        if self.fuel >= 20:
            print("\n================ RACE 🏎️ =================")
            print(f"\nYou take your {self.model} out for a race..")
            self.fuel -= 20
            time.sleep(1.5)
            winner = random.randint(1, 2)
            if winner == 1:
                print("\nYou won the race!")
                self.credits += 10000
                time.sleep(1)
                print("+10,000 Credits! 💰")
            elif winner == 2:
                print("\nYou lost the race..")
                self.credits -= 2000
                time.sleep(1)
                print("-2000 Credits! 🙉")
        else:
            print("\nYour outta fuel champ.")
            time.sleep(1.5)