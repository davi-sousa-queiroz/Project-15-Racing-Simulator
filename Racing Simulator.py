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
        print("\n============= YOUR 🏎️ CAR ===============")
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

    def refuel(self):
        if self.credits < 3000:
            print("\nYou need 3000 Credits to refuel! ⛽️")
        else:
            print(f"\nFilling up your {self.make}..")
            time.sleep(2.5)
            print(f"Your {self.model} has been refueled!")
            time.sleep(1)
            print("-3000 CR.")
            self.credits -= 3000
            time.sleep(1)
            self.fuel = 100

    def upgrades(self):
        while True:
            print("\n1.\tRace suspension 🏎️\n2.\tRace Breaks 🛑\n3.\tRace Spoiler 🪽\n4.\tRace Tires 🛞\n5.\tRace Engine ⚙️💨\n6.\tLeave Garage")
            upgrade = input("\n>> ")
            if upgrade == "1":
                if self.credits >= 3000:
                    print("\nAre you sure you want to purchase race suspension for 3000 CR? (y/n)")
                    choice = input("\n>> ").lower
                    if choice == "y":
                            self.credits -= 3000
                            self.performance += 234
                            print("\nPurchase Successful!")
                            time.sleep(1)
                            print("\n-3000 Credits")
                            print(f"Car Performance: {self.performance}")
                    if choice == "n":
                        continue
                else:
                    print("\nNot enough Credits!")
                    continue
            elif upgrade == "2":
                if self.credits >= 3500:
                    print("\nAre you sure you want to purchase race breaks for 3500 CR? (y/n)")
                    choice = input("\n>> ").lower
                    if choice == "y":
                            self.credits -= 3500
                            self.performance += 313
                            print("\nPurchase Successful!")
                            time.sleep(1)
                            print("\n-3500 Credits")
                            print(f"Car Performance: {self.performance}")
                    if choice == "n":
                        continue
                else:
                    print("\nNot enough Credits!")
                    continue
            elif upgrade == "3":
                if self.credits >= 4000:
                    print("\nAre you sure you want to purchase race spoiler for 4000 CR? (y/n)")
                    choice = input("\n>> ").lower
                    if choice == "y":
                            self.credits -= 4000
                            self.performance += 402
                            print("\nPurchase Successful!")
                            time.sleep(1)
                            print("\n-4000 Credits")
                            print(f"Car Performance: {self.performance}")
                    if choice == "n":
                        continue
                else:
                    print("\nNot enough Credits!")
                    continue
            elif upgrade == "4":
                if self.credits >= 4500:
                    print("\nAre you sure you want to purchase race tires for 4500 CR? (y/n)")
                    choice = input("\n>> ").lower
                    if choice == "y":
                            self.credits -= 4500
                            self.performance += 517
                            print("\nPurchase Successful!")
                            time.sleep(1)
                            print("\n-4500 Credits")
                            print(f"Car Performance: {self.performance}")
                    if choice == "n":
                        continue
                else:
                    print("\nNot enough Credits!")
                    continue
            elif upgrade == "5":
                if self.credits >= 5000:
                    print("\nAre you sure you want to purchase Race Engine for 5000 CR? (y/n)")
                    choice = input("\n>> ").lower
                    if choice == "y":
                            self.credits -= 5000
                            self.performance += 674
                            print("\nPurchase Successful!")
                            time.sleep(1)
                            print("\n-5000 Credits")
                            print(f"Car Performance: {self.performance}")
                    if choice == "n":
                        continue
                else:
                    print("\nNot enough Credits!")
                    continue
            elif upgrade == "6":
                print("\nLeaving Garage..")
                time.sleep(1.5)
                break

    def menu(self):
        print("\n1.\tRace 🏁\n2.\tRefuel ⛽️\n3.\tUpgrades ⬆️\n4.\tView Car 📊\n5.\tQuit")

print("\nWelcome to Racing Simulator! 🏎️")
time.sleep(1.5)
print("\nLet's Build your race car!")
time.sleep(1.5)
print("\nEnter car make: ")
make = input("\n>> ").title()
print("\nEnter car model: ")
model = input("\n>> ").title()
print("\nEnter car year: ")
year = input("\n>> ")

player_car = Car(make, model, year)