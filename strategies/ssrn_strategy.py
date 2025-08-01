from typing import List, Dict, Optional
import requests
from bs4 import BeautifulSoup

class SSRNSearchStrategy():
    def __init__(self):
        self.base_url = "https://www.ssrn.com/index.cfm/en/"

    def search_papers(self, query: str, number_of_abstracts: int = 25) -> Optional[List[Dict]]:
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }

        # SSRN search parameters
        params = {
            "query": query,
        }
        
        papers = []

        try:
            response = requests.get(self.base_url, headers=headers, params=params)
            
            if response.status_code == 200:
                response_html = BeautifulSoup(response.content, 'html.parser')
                descriptions = response_html.find_all('div', class_='description')

                if descriptions:
                    for description in descriptions:
                        title = description.find('h3').find('a', class_='title optClickTitle')

                        authors = description.find('div', class_='authors-list').get_text() # Listo
                        url = description.find('a')['href']

                        raw_year = description.find('div', class_='note note-list').get_text()
                        year = raw_year[7:] #Listo

                        paper_info = {
                            "title": title,
                            "authors": authors,
                            "url": url,
                            "abstract": "NONE",
                            "year": year
                        }
                        papers.append(paper_info)
                        count += 1
            else:
                print(f"Error fetching data from SSRN: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"An error occurred while fetching data from SSRN: {e}")
            return None

        return papers if papers else None

if __name__ == "__main__":
    strategy = SSRNSearchStrategy()
    query = "financial markets"

    papers = strategy.search_papers(query=query, number_of_abstracts=5)

    if papers:
        print(f"{len(papers)} papers found:\n")
        for paper in papers:
            print(f"Title: {paper['title']}")
            print(f"Authors: {paper['authors']}")
            print(f"Year: {paper['year']}")
            print(f"URL: {paper['url']}")
            if paper['abstract']:
                print(f"Abstract: {paper['abstract'][:200]}...")
            print("-" * 50)
    else:
        print("No papers found.")