# pylint: disable=bare-except
# pylint: disable=comparison-of-constants
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from .product_finder_validator import product_finder_validator


class MockRequest:
    def __init__(self) -> None:
        self.view_args = None


def test_product_finder_validator():
    request = MockRequest()
    request.view_args = {
        "id": "0",
    }

    try:
        product_finder_validator(request)
    except:
        assert False


def test_product_finder_validator_with_error():
    request = MockRequest()
    request.view_args = {}

    try:
        product_finder_validator(request)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
