from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING
from .product import Product

if TYPE_CHECKING:
    from .grocery_store import GroceryStore


@dataclass
class GroceryProduct(Product):
    selling_price: float
    weight: float
    expiry_date: int
    threshold: int
    available_stock: int
    discount: float
    store: Optional['GroceryStore'] = None

    def to_json(self):
        base_json = super().to_json()
        base_json.update({
            "selling_price": self.selling_price,
            "weight": self.weight,
            "expiry_date": self.expiry_date,
            "threshold": self.threshold,
            "available_stock": self.available_stock,
            "discount": self.discount,
            "store": self.store.to_json() if self.store else None,
            "product_type": "grocery"
        })
        return base_json 