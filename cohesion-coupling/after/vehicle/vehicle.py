from vehicle_info import VehicleInfo

class Vehicle:
    _id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, _id: str, license_plate: str, info: VehicleInfo):
        self._id = _id
        self.license_plate = license_plate
        self.info = info

    def __str__(self):
        print(self.info) # Printing the vehicle info
        return f"License plate: {self.license_plate}\n"