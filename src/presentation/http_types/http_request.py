# pylint: disable=too-many-arguments
from typing import Dict


class HttpRequest:

    def __init__(
        self,
        header: Dict = None,
        body: Dict = None,
        query_params: Dict = None,
        path_params: Dict = None,
        url: str = None,
        token_information: Dict = None
    ):
        self.header = header
        self.body = body
        self.query_params = query_params
        self.url = url
        self.path_params = path_params
        self.token_information = token_information

    def __repr__(self):
        return (
            f"HttpRequest (header={self.header}, body={self.body}, query={self.query_params})"
        )
