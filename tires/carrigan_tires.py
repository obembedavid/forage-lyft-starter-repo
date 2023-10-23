from tires.tires import Tires

class CarriganTires(Tires):
    def init(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        for tire in self.tire_wear:
            if tire >= 0:
                return True
            else:
                return False