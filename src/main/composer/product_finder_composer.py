from src.infra.db.repositories.products_repository import ProductsRepository
from src.infra.db.repositories.products_cache_repository import ProductsCacheRepository
from src.data.use_cases.product_finder import ProductFinder
from src.presentation.controllers.product_finder_controller import ProductFinderController


def product_finder_composer():
    repository = ProductsRepository()
    cache_repository = ProductsCacheRepository()
    use_case = ProductFinder(repository, cache_repository)
    controller = ProductFinderController(use_case)

    return controller
