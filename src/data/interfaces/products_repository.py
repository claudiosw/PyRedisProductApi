from abc import ABC, abstractmethod
from src.domain.models.products import Products


class ProductsRepositoryInterface(ABC):

    @abstractmethod
    def get_product_by_id(self, id: int) -> Products:
        pass

    @abstractmethod
    def register_product(self, id: int, name: str, value: float, product_type: str):
        pass
