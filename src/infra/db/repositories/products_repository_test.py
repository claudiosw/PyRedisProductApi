from src.infra.db.settings import db_connection_handler
from .products_repository import ProductsRepository
from src.infra.db.entities.products import ProductTypes


db_connection_handler.connect_to_db()


def test_get_product_by_id():
    products_repository = ProductsRepository()
    fake_registry = {
        "id": 0,
        "name": "myProductName",
        "value": 5.19,
        "product_type": "cleaning"
    }
    mock_product_type = ProductTypes("cleaning")

    engine = db_connection_handler.get_engine()
    engine.execute(
        '''
        INSERT INTO products (id, name, value, product_type)
        VALUES
        ({}, '{}', '{}', '{}')
        '''.format(
            fake_registry["id"],
            fake_registry["name"],
            fake_registry["value"],
            fake_registry["product_type"],
        )
    )

    result = products_repository.get_product_by_id(fake_registry["id"])

    engine.execute("DELETE FROM products WHERE id={}".format(fake_registry["id"]))

    assert result.id == fake_registry["id"]
    assert result.name == fake_registry["name"]
    assert result.value == fake_registry["value"]
    assert result.product_type == mock_product_type


def test_register_product():
    products_repository = ProductsRepository()
    fake_registry = {
        "id": 1,
        "name": "myProductName2",
        "value": "5.19",
        "product_type": "cleaning"
    }

    mock_product_type = ProductTypes("cleaning")
    new_product = products_repository.register_product(
        fake_registry["id"],
        fake_registry["name"],
        fake_registry["value"],
        fake_registry["product_type"],
    )
    engine = db_connection_handler.get_engine()
    query_product = engine.execute(
        "SELECT * FROM products WHERE id={};".format(new_product.id)
    ).fetchone()
    engine.execute("DELETE FROM products WHERE id={}".format(new_product.id))
    assert new_product.id == query_product.id
    assert new_product.name == query_product.name
    assert new_product.value == query_product.value
    assert new_product.product_type == ProductTypes(mock_product_type).value
