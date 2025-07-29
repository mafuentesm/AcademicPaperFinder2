from abstract_strategy import SearchStrategy
import requests
import os
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
# Se importan todas las liberias de Parsing encontradas en 'search_helper.py'

class ScopusSearchStrategy(SearchStrategy):
    def __init__(self):
        self.api_key = os.getenv("SCOPUS_API_KEY")
        self.base_url = "https://api.elsevier.com/content/search/scopus"

    def search_papers(self, query: str, is_open_access: bool = False, number_of_abstracts: int = 25) -> Optional[List[Dict]]:
        headers = {
            "X-ELS-APIKey": self.api_key,
            "Accept": "application/json"
        }
        # Incorporate the open access and publication year filter into the query if required
        open_access_filter = "AND (OPENACCESS(1))" if is_open_access else ""
        year_filter = "AND PUBYEAR > 2014"
        full_query = f"{query} {open_access_filter} {year_filter}"

        params = {
            "query": full_query,
            "count": number_of_abstracts,  # Number of results to return
            "field": "dc:title,dc:creator,dc:description,prism:publicationName,prism:doi,prism:url,prism:coverDate"  # Including prism:coverDate for year
        }
        papers = []

        try:
            response = requests.get(self.base_url, headers=headers, params=params)
            if response.status_code == 200:
                response_json = response.json()
                for entry in response_json.get("search-results", {}).get("entry", []):
                    # Extracting the year from the cover date
                    cover_date = entry.get("prism:coverDate", "")
                    year = cover_date.split('-')[0] if cover_date else "No year available"
                    paper_info = {
                        "id": entry.get("prism:doi"),
                        "title": entry.get("dc:title"),
                        "authors": entry.get("dc:creator"),
                        "url": f"https://doi.org/{entry.get('prism:doi')}",
                        "abstract": entry.get("dc:description"),
                        "year": year
                    }
                    papers.append(paper_info)
            else:
                print(f"Error fetching data from Scopus API: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred while fetching data from Scopus API: {e}")
            return None

        return papers