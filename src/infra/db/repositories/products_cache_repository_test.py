from src.infra.db.settings import cache_connection_handler
from .products_cache_repository import ProductsCacheRepository


cache_connection_handler.connect_to_cache()


def test_cache_get_product_by_id():
    products_cache_repository = ProductsCacheRepository()
    fake_registry = {
        "id": 0,
        "name": "myProductName",
        "value": 5.19,
        "product_type": "cleaning"
    }

    cache_connection = cache_connection_handler.get_connection()
    cache_connection.hset(str(fake_registry["id"]), key='name', value=fake_registry["name"])
    cache_connection.hset(str(fake_registry["id"]), key='value', value=str(fake_registry["value"]))
    cache_connection.hset(str(fake_registry["id"]), key='product_type', value=fake_registry["product_type"])

    result = products_cache_repository.get_product_by_id(fake_registry["id"])
    cache_connection.delete(str(fake_registry["id"]))

    assert result['name'] == fake_registry["name"]
    assert result['value'] == str(fake_registry["value"])
    assert result['product_type'] == fake_registry["product_type"]


def test_cache_register_product():
    products_cache_repository = ProductsCacheRepository()
    fake_registry = {
        "id": 0,
        "name": "myProductName",
        "value": 5.19,
        "product_type": "cleaning"
    }

    cache_connection = cache_connection_handler.get_connection()

    result = products_cache_repository.register_product(
        fake_registry["id"],
        fake_registry["name"],
        fake_registry["value"],
        fake_registry["product_type"]
    )
    cache_connection.delete(str(fake_registry["id"]))

    assert result.name == fake_registry["name"]
    assert result.value == str(fake_registry["value"])
    assert result.product_type == fake_registry["product_type"]
