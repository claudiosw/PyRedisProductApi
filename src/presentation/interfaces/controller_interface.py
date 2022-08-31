from abc import ABC, abstractmethod
from typing import Type
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class ControllerInterface(ABC):

    @abstractmethod
    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        pass
