from typing import Callable, Type, Dict
from flask import request as FlaskRequest
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


def request_adapter(request: FlaskRequest, callback: Callable, token_information: Dict = None) -> Type[HttpResponse]:
    body = None
    if request.data:
        body = request.json

    http_request = HttpRequest(
        header=request.headers,
        body=body,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path,
        token_information=token_information
    )

    http_response = callback(http_request)
    return http_response
