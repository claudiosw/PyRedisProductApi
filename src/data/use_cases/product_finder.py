from typing import Dict
from src.data.interfaces.products_repository import ProductsRepositoryInterface
from src.domain.models.products import Products
from src.domain.use_cases.product_finder import ProductFinder as ProductFinderInterface
from src.errors.http_not_found import HttpNotFoundError


class ProductFinder(ProductFinderInterface):
    def __init__(
        self,
        product_repository: ProductsRepositoryInterface,
        product_cache_repository: ProductsRepositoryInterface
    ) -> None:
        self.__product_repository = product_repository
        self.__product_cache_repository = product_cache_repository
        self.__last_status = None

    def find_by_id(self, id: int) -> Dict:
        product = self.__get_product_by_id_from_cache(id)
        if product:
            self.__last_status = 1
        else:
            product = self.__get_product_by_id_from_db(id)
            if product:
                self.__last_status = 2
                product = self.__register_product_into_cache(
                    product.id,
                    product.name,
                    product.value,
                    product.product_type
                )
            else:
                self.__last_status = 0
                raise HttpNotFoundError('Product Not found')

        return self.__format_response(product)

    def __get_product_by_id_from_cache(self, id):
        return self.__product_cache_repository.get_product_by_id(id)

    def __get_product_by_id_from_db(self, id):
        return self.__product_repository.get_product_by_id(id)

    def __register_product_into_cache(self, id, name, value, product_type):
        return self.__product_cache_repository.register_product(id, name, value, product_type)

    def __format_response(self, product: Products) -> Dict:
        return {
            "data": {
                "id": product.id,
                "name": product.name,
                "value": product.value,
                "product_type": product.product_type,
                "status": self.__last_status
            }
        }
