import string
from vehicle.vehicle_registry import VehicleRegistry
from vehicle.vehicle import Vehicle

class Application:
    def register_vehicle(self, brand: string) -> Vehicle:
        # create a registry instance
        registry = VehicleRegistry()

        # create a vehicle
        vehicle = registry.create_vehicle(brand)

        return vehicle