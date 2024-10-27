import random
import string
from vehicle_info import VehicleInfo
from vehicle import Vehicle
from vehicle_model import VehicleModel


class VehicleRegistry:
    vehicle_info: dict[str, VehicleInfo] = {}

    def __init__(self):
        # Simulating a data from a database
        self.add_vehicle_info("Tesla Model 3", VehicleModel.ELECTRIC, 60000)
        self.add_vehicle_info("Volkswagen ID3", VehicleModel.ELECTRIC, 35000)
        self.add_vehicle_info("BMW 5", VehicleModel.NO_ELECTRIC, 45000)

    def add_vehicle_info(self, brand: str, model: VehicleModel, catalogue_price: float):
        self.vehicle_info[brand] = VehicleInfo(brand, model, catalogue_price)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand: str) -> Vehicle:
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)

        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])