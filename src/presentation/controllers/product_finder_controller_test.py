from src.data.tests.product_finder import ProductFinderSpy
from src.presentation.http_types.http_response import HttpResponse
from .product_finder_controller import ProductFinderController


class HttpRequestMock():
    def __init__(self) -> None:
        self.path_params = {"id": 0}


def test_handler():
    http_request_mock = HttpRequestMock()
    use_case = ProductFinderSpy()
    product_finder_controller = ProductFinderController(use_case)

    response = product_finder_controller.handle(http_request_mock)

    assert use_case.find_by_id_attributes["id"] == http_request_mock.path_params["id"]

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"]["attributes"] is not None
