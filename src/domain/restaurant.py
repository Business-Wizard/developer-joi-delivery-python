from dataclasses import dataclass, field
from typing import Set
from .outlet import Outlet
from .food_product import FoodProduct


@dataclass
class Restaurant(Outlet):
    menu: Set[FoodProduct] = field(default_factory=set)
    cuisine_type: str = "International"

    def to_json(self):
        base_json = super().to_json()
        base_json.update({
            "cuisine_type": self.cuisine_type,
            "menu": [product.to_json() for product in self.menu]
        })
        return base_json
