from typing import List, Dict, Optional, Type
from abc import ABC, abstractmethod

class SearchStrategy(ABC):
    @abstractmethod
    def search_papers(self, query: str, number_of_abstracts: int = 25) -> Optional[List[Dict]]:
        pass
