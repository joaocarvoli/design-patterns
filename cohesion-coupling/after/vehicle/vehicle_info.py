from vehicle_model import VehicleModel
from after.tax_calculator import TaxCalculator

class VehicleInfo:
    brand: str
    catalogue_price: float
    model: VehicleModel

    def __init__(self, brand: str, model: VehicleModel, catalogue_price: float):
        self.brand = brand
        self.model = model
        self.catalogue_price = catalogue_price

    def __str__(self):
        return (f"Brand: {self.brand}\n"
                f"Price: {self.catalogue_price}\n"
                f"What is the model? {self.model.name}\n"
                f"So the payable tax is: {self.compute_tax()}\n")

    def compute_tax(self) -> float:
        return TaxCalculator.compute_tax(self.model, self.catalogue_price)