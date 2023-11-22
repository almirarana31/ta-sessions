class House:
    """A simple house class"""

    total_house = 0  # Keep track of the total number of houses

    def __init__(self, floors, doors, windows, color="White", has_garage=False, address=""):
        self.floors = floors
        self.doors = doors
        self.windows = windows
        self.color = color
        self.has_garage = has_garage
        self.address = address

        # Increment
        House.total_house += 1

    def display_info(self):
        """Displays attribute information of a house object."""
        print("House Information: ")
        print(f"    - Address: {self.address}")
        print(f"    - Doors: {self.doors}")
        print(f"    - Floors: {self.floors}")
        print(f"    - Windows: {self.windows}")
        print(f"    - Color: {self.color}")
        print(f"    - Has Garage: {'Yes' if self.has_garage else 'No'}")

    @classmethod
    def display_total_houses(cls):
        print(f"Total number of houses = {cls.total_house}")

    #Paint house function
    def paint_house(self):
        new_color=input("New color: ")
        self.color=new_color
        print(f"Your house in now {self.color}")
    
    #Add garage function
    def add_garage(self):
        if self.has_garage == True:
            print("This house already has a garage")
        else:
            self.has_garage = True
            print("Your house has a garage now")

    #New address function
    def set_address(self):
        new_address=input("New address: ")
        self.address=new_address
        print(f"Your houses address is now {self.address}")

    @staticmethod
    def validate_house(house):
        if not isinstance(house, House):
            return False    # Not a valid house object
        if not all(isinstance(attr, int) and attr > 0 for attr in (house.floors, house.doors, house.windows)):
            return False    # Floors, Doors, Windows should all be positive integers

        return True


# Creating instances (objects) of the House class
house1 = House(floors=2, doors=3, windows=6, color="Blue", has_garage=True, address="123 Main St")
house2 = House(floors=1, doors=2, windows=4, address="123 Main St")
house3 = House(floors=2, doors=3, windows=5)

#Setting new address 
house1.set_address()
house2.set_address()
house3.set_address()

#Adding garage
house1.add_garage()
house2.add_garage()
house3.add_garage()

#Painting house new color
house1.paint_house()
house2.paint_house()
house3.paint_house()

house1.display_info()
print()
house2.display_info()
print()
house3.display_info()
print()
House.display_total_houses()
print()

validation_result = House.validate_house(house2)
print(f"House Validation Result: {'Valid' if validation_result else 'Invalid'}")
