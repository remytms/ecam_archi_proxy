#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""This is a house.

Maintainer: Rémy Taymans <14291@student.ecam.be>
Creation: 31 mar 2017
Last change: 31 mar 2017
"""

class HouseInterface():
    def __init__(self, address):
        raise NotImplementedError("This method should be implemented")
    def enter_by_front_door(self):
        raise NotImplementedError("This method should be implemented")
    def leave_by_front_door(self):
        raise NotImplementedError("This method should be implemented")
    def enter_by_garden_door(self):
        raise NotImplementedError("This method should be implemented")
    def leave_by_garden_door(self):
        raise NotImplementedError("This method should be implemented")

class House(HouseInterface):
    def __init__(self, address):
        self.address = address
        self._people_in_house = 0
        self._people_in_garden = 0
    def enter_by_front_door(self):
        print("Someone enters in the house")
        self._people_in_house += 1
    def leave_by_front_door(self):
        print("Someone leaves the house")
        self._people_in_house -= 1
    def enter_by_garden_door(self):
        print("Someone leaves the garden and goes in the house")
        self._people_in_house += 1
        self._people_in_garden -= 1
    def leave_by_garden_door(self):
        print("Someone leaves the house and enters in the garden")
        self._people_in_house -= 1
        self._people_in_garden += 1
    def __str__(self):
        res = ""
        res += "House: %s\n" % self.address
        res += "    Total people in house: %d\n" % (
            self._people_in_house + self._people_in_garden
        )
        res += "    People in the house: %d\n" % self._people_in_house
        res += "    People in the garden: %d\n" % self._people_in_garden
        return res

class GuardedHouse(HouseInterface):
    def __init__(self, address):
        self.house = House(address)
        self.passwd = "42"
    def ask_password(self):
        passwd = input("Give password to enter: ")
        return passwd == self.passwd
    def enter_by_front_door(self):
        if self.ask_password():
            self.house.enter_by_front_door()
        else:
            print("Wrong password, you cannot enter in the house.")
    def leave_by_front_door(self):
        self.house.leave_by_front_door()
    def enter_by_garden_door(self):
        self.house.enter_by_garden_door()
    def leave_by_garden_door(self):
        self.house.leave_by_garden_door()
    def __str__(self):
        return self.house.__str__()

def main():
    house = GuardedHouse("Rue de la gare 1")
    while True:
        print("1. enter by front door", end="\t")
        print("2. leave by front door", end="\n")
        print("3. enter by garden door", end="\t")
        print("4. leave by garden door", end="\n")
        try:
            choice = int(input("Make your choice: "))
        except ValueError:
            print("Please enter an integer")
        else:
            if choice == 1:
                house.enter_by_front_door()
                print(house)
            elif choice == 2:
                house.leave_by_front_door()
                print(house)
            elif choice == 3:
                house.enter_by_garden_door()
                print(house)
            else:
                house.leave_by_garden_door()
                print(house)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting…")

