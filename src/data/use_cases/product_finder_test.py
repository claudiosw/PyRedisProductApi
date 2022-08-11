from src.infra.db.tests.products_repository import ProductsRepositorySpy
from src.errors.http_not_found import HttpNotFoundError
from .product_finder import ProductFinder


def test_find_by_id_on_cache():
    repo = ProductsRepositorySpy()
    cache_repo = ProductsRepositorySpy()
    product_finder = ProductFinder(repo, cache_repo)

    mock_id = 0

    response = product_finder.find_by_id(mock_id)

    assert cache_repo.get_product_by_id_attributes["id"] == mock_id

    assert "data" in response
    assert "name" in response["data"]
    assert "value" in response["data"]
    assert "product_type" in response["data"]
    assert response["data"]["status"] == 1


def test_find_by_id_on_db():
    class ProductRepoNone(ProductsRepositorySpy):
        def get_product_by_id(self, id):
            return None

    repo = ProductsRepositorySpy()
    cache_repo = ProductRepoNone()
    product_finder = ProductFinder(repo, cache_repo)

    mock_id = 0

    response = product_finder.find_by_id(mock_id)

    assert repo.get_product_by_id_attributes["id"] == mock_id

    assert "data" in response
    assert "name" in response["data"]
    assert "value" in response["data"]
    assert "product_type" in response["data"]


def test_find_by_id_no_registry():
    class ProductRepoWithError(ProductsRepositorySpy):
        def get_product_by_id(self, id):
            return None

    repo = ProductRepoWithError()
    repo_cache = ProductRepoWithError()
    product_finder = ProductFinder(repo, repo_cache)

    mock_id = 0

    try:
        product_finder.find_by_id(mock_id)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpNotFoundError)
        assert str(exception) == "Product Not found"
