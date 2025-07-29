from abstract_strategy import SearchStrategy
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional

# Se importan todas las liberias de Parsing encontradas en 'search_helper.py'

class GoogleScholarSearchStrategy(SearchStrategy):
    def __init__(self):
        self.base_url = "https://scholar.google.com/scholar"
        self.api_key = "LLAVE_API_SerpAPI"

    def search_papers(self, query: str, number_of_abstracts: int = 25) -> Optional[List[Dict]]:
        params = {
        "q": query
        }

        papers = []
        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                pass
        except:
            pass
    
    pass