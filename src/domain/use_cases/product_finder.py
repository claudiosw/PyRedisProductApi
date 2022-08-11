from typing import Dict
from abc import ABC, abstractmethod


class ProductFinder(ABC):

    @abstractmethod
    def find_by_id(self, id: int) -> Dict:
        pass
