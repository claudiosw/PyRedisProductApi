from src.domain.models.products import Products


def create_mock_product():
    return Products(
        id=0,
        name='someNameHere',
        value=9.91,
        product_type="clothing"
    )
