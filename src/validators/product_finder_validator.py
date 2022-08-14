from cerberus import Validator
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


def product_finder_validator(request: any):

    path_parameters_validator = Validator({
        "id": {"type": "string", 'regex': '[0-9]+', "required": True, "empty": False}
    })

    response = path_parameters_validator.validate(request.view_args)

    if response is False:
        raise HttpUnprocessableEntityError(path_parameters_validator.errors)
