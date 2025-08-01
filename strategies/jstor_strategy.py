from abstract_strategy import SearchStrategy
from typing import List, Dict, Optional
import requests
from bs4 import BeautifulSoup
# Se importan todas las liberias de Parsing encontradas en 'search_helper.py'

class JSTORSearchStrategy(SearchStrategy):
    def __init__(self):
        self.base_url = "https://www.jstor.org/action/doBasicSearch"

    def search_papers(self, query: str, number_of_abstracts: int = 25) -> Optional[List[Dict]]:
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        }
        # Incorporate the open access and publication year filter into the query if required

        params = {
            "query": query,
        }
        
        papers = []

        try:
            response = requests.get(self.base_url, headers=headers, params=params)
            if response.status_code == 200:
                info = BeautifulSoup(response.content, 'html.parser')
                results = info.select("li.search-result")

                for i in range(len(results)):
                    if i >= number_of_abstracts:
                        break

                    result = results[i]

                    title_tag = result.select_one(".title a")
                    title = title_tag.text.strip() if title_tag else "Sin título"
                    url = f"https://www.jstor.org{title_tag['href']}" if title_tag else "Sin URL"

                    authors_tag = result.select_one(".contrib")
                    authors = authors_tag.text.strip() if authors_tag else "Sin autores"

                    date_tag = result.select_one(".publication-date")
                    year = date_tag.text.strip() if date_tag else "Sin año"

                    paper_info = {
                        "title": title,
                        "authors": authors,
                        "url": url,
                        "abstract": None,  # JSTOR no parece incluir abstracts tan faciles de acceder
                        "year": year
                    }
                    papers.append(paper_info)
            else:
                print(f"Error fetching data from JSTOR: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred while fetching data from JSTOR: {e}")
            return None

        return papers
    
if __name__ == "__main__":
    strategy = JSTORSearchStrategy()
    query = "climate change"

    papers = strategy.search_papers(query=query, number_of_abstracts=5)

    if papers:
        print(f"{len(papers)} papers found:\n")
        for paper in papers:
            print(f"Title: {paper['title']}")
            print(f"Authors: {paper['authors']}")
            print(f"Year: {paper['year']}")
            print(f"URL: {paper['url']}")
            print("-" * 40)
    else:
        print("No papers found.")