from typing import Type
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.use_cases.product_finder import ProductFinder as ProductFinderInterface


class ProductFinderController(ControllerInterface):
    def __init__(self, use_case: Type[ProductFinderInterface]) -> None:
        self.__use_case = use_case

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        id = http_request.path_params["id"]
        response = self.__use_case.find_by_id(id)

        return HttpResponse(
            status_code=200,
            body={
                "data": {
                    "type": "Products",
                    "count": 1,
                    "attributes": response["data"],
                }
            }
        )
