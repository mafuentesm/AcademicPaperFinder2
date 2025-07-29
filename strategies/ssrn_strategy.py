from abstract_strategy import SearchStrategy
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional

# Se importan todas las liberias de Parsing encontradas en 'search_helper.py'

class SSRNSearchStrategy(SearchStrategy):
    def __init__(self):
        self.base_url = "https://papers.ssrn.com/sol3/results.cfm"

    def search_papers(self, query: str, is_open_access: bool = False, number_of_abstracts: int = 25) -> Optional[List[Dict]]:
        headers = {
            #Header
        }

        full_query = f"{query}"

        params = dict
        
        papers = []

        try:
            response = requests.get(self.base_url, headers=headers, params=params)
            if response.status_code == 200:
                response_json = response.json()
                pass
        except:
            pass

    pass