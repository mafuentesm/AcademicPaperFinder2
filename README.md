# Academic Paper Finder

El siguiente repositorio es una extensión basada en el código publicado en el siguiente artículo:
https://medium.com/@zakaria.hamane1/how-to-automate-academic-paper-searches-with-python-part-i-65bd1c837f4c

A definición del autor original del repositorio:
"This script provides an interface to search for academic papers from multiple sources including IEEE Xplore, arXiv, PubMed, CrossRef, and more. It uses a sequential combined search strategy to go through the strategies one by one until the requested number of paper abstracts are found."

En esta versión, se busca agregar estrategias asociadas a fuentes nuevas, siendo el objetivo final:
- Google Scholar
- Scopus ✅
- Web of Science
- PubMed ✅
- SSRN
- JSTOR

## Setup

1. Clonar el repositorio en la máquina local
2. Instalar los Python packages necesarios, localizados en `requirements.txt`:
```
pip install -r requirements.txt
```

3. Set up your environment variables by copying the `.env` template to your project root and filling in your API keys and email for PubMed.
```
cp env_files/local.env .env
```

Edit `.env` with your actual credentials.

## Usage

El `SearchHelper` puede ser ejecutado desde `main.py`. Este último está compuesto por dos arguementos clave: la solicitud hacia la
página, o `query`; y la cantidad de abstracts por obtener. Se deja un código de ejemplo:

Ejemplo:
```python
from search_helper import SearchHelper

helper = SearchHelper()
helper.set_sequential_combined_strategy(["ieee", "arxiv"])
papers = helper.execute("Artificial Intelligence", 10)
for paper in papers:
 print(paper)
```

## Environment Variables
- S2_API_KEY_1: Your Semantic Scholar API key.
- CORE_API_KEY: Your CORE API key.
- SPRINGER_API_KEY: Your Springer API key.
- SS_EMAIL: Your email for Entrez PubMed API.
- SCOPUS_API_KEY: Your Scopus API key.
