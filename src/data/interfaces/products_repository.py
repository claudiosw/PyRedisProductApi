from decimal import Decimal
from abc import ABC, abstractmethod
from src.domain.models.products import Products
from src.infra.db.entities.product_types import ProductTypes


class ProductsRepositoryInterface(ABC):

    @abstractmethod
    def get_product_by_id(self, id: int) -> Products:
        pass

    @abstractmethod
    def register_product(self, id: int, name: str, value: Decimal, type: ProductTypes):
        pass
