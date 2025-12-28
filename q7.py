class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    
    def __init__(self, make, model, year):

        self.make = str(make)
        self.model = str(model)
        self.year = int(year)
    
    def describe_car(self):

        print(f"Year Make Model : {self.year} {self.make} {self.model}")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

print("\n=== Q7: Task 2 Test Scenarios ===\n")

toyota_corolla = Car("Toyota", "Corolla", 2020)
toyota_corolla.describe_car()

print("\n=== Task 2 Completed ===")