from src.presentation.http_types.http_response import HttpResponse
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from .error_controller import handle_errors


def test_handle_errors_generic():
    error_message = 'Trying some generic error here'
    some_error = Exception(error_message)

    response = handle_errors(some_error)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 500
    assert response.body["errors"][0]["detail"] == error_message


def test_handle_errors_unprocessable_entity_error():
    error_message = 'Trying some HttpUnprocessableEntityError error here'
    some_error = HttpUnprocessableEntityError(error_message)

    response = handle_errors(some_error)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 422
    assert response.body["errors"][0]["detail"] == error_message
