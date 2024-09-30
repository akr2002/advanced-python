class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"car info: {self.year} {self.make} {self.model}")

    def start_engine(self):
        print(f"the {self.make} {self.model}'s engine has started.")


my_car = Car("toyota", "corolla", 2020)

my_car.display_info()
my_car.start_engine()
