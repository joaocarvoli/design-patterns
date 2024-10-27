from taxes import tax_reference
from after.vehicle import VehicleModel

class TaxCalculator:
    @staticmethod
    def compute_tax(model: VehicleModel, catalogue_price: float) -> float:
        if model not in tax_reference:
            raise ValueError("The model has no tax reference")
        tax_percentage = tax_reference[model]
        return tax_percentage * catalogue_price