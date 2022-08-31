from typing import Type
from src.presentation.http_types.http_response import HttpResponse
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_not_found import HttpNotFoundError
from src.errors.http_request_error import HttpRequestError


def handle_errors(error: Type[Exception]) -> Type[HttpResponse]:
    if isinstance(error, (HttpUnprocessableEntityError, HttpNotFoundError, HttpRequestError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
