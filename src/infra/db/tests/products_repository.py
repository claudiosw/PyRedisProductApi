from src.domain.models.products import Products
from src.domain.tests.products import create_mock_product


class ProductsRepositorySpy:
    def __init__(self) -> None:
        self.get_product_by_id_attributes = {}
        self.register_product_attributes = {}

    def get_product_by_id(self, id: int) -> Products:
        self.get_product_by_id_attributes["id"] = id
        return create_mock_product()

    def register_product(self, id: int, name: str, value: float, product_type: str) -> Products:
        self.register_product_attributes["id"] = id
        return create_mock_product()
