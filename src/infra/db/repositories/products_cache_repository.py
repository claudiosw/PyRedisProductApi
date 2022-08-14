import datetime
from src.domain.models.products import Products
from src.infra.db.settings import cache_connection_handler
from src.infra.db.entities.products import Products as ProductsModel
from src.data.interfaces.products_repository import ProductsRepositoryInterface


class ProductsCacheRepository(ProductsRepositoryInterface):

    @classmethod
    def get_product_by_id(self, id: int) -> Products:

        cache_connection = cache_connection_handler.get_connection()
        product = cache_connection.hgetall(str(id))
        return product

    @classmethod
    def register_product(self, id: int, name: str, value: float, product_type: str):

        cache_connection = cache_connection_handler.get_connection()
        cache_connection.hset(str(id), 'name', name)
        cache_connection.hset(str(id), 'value', str(value))
        cache_connection.hset(str(id), 'product_type', product_type)
        cache_connection.expire(str(id), datetime.timedelta(seconds=180))
        new_product = cache_connection.hgetall(str(id))
        return ProductsModel(
            id=id,
            name=new_product['name'],
            value=new_product['value'],
            product_type=new_product['product_type']
        )
