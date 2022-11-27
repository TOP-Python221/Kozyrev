class Carrier:
    def carry_military(self, items):
        pass

    def carry_commercial(self, items):
        pass


class Cargo(Carrier):
    def carry_military(self, items):
        print(f"Самолет перевозит {items}.т военных груза")


class Passenger(Carrier):
    def carry_military(self, passengers):
        print(f"Самолет перевозит {passengers} военных")


class Plane:
    def __init__(self, Carrier):
        self.carrier = Carrier

    def display_description(self):
        pass

    def add_objects(self, new_objects):
        pass


class Commercial(Plane):
    def __init__(self, Carrier, objects):
        super().__init__(Carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_commercial(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects


class Military(Plane):
    def __init__(self, Carrier, objects):
        super().__init__(Carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_military(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects


cargo = Cargo()
passenger = Passenger()

# Bridging Military and Cargo classes
military1 = Military(cargo, 100)
military1.display_description()
military1.add_objects(25)
military1.display_description()
