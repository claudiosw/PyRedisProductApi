from typing import Dict


class ProductFinderSpy:
    def __init__(self) -> None:
        self.find_by_id_attributes = {}

    def find_by_id(self, id: int) -> Dict:
        self.find_by_id_attributes["id"] = id
        return {
            "data": {
                "id": 0,
                "name": 'someName',
                "value": 1.25,
                "product_type": 'cleaning'
            }
        }
