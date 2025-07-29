from search_helper import SearchHelper
import json
import sys

def main():
    keywords = [
        "sperm selection", "oocyte selection", "gamete selection", "LLM", "machine learning",
        "embryo quality", "assisted reproduction", "artificial intelligence", "AI", "infertility",
        "TRA", "ART", "embryo selection"
    ]

    reproduction_keywords = ["sperm selection", "oocyte selection", "gamete selection", 
                            "embryo quality", "assisted reproduction", "infertility", 
                            "TRA", "ART", "embryo selection"]

    ai_keywords = ["LLM", "machine learning", "artificial intelligence", "AI"]

    reproduction_query = [f'"{kw}"' for kw in reproduction_keywords]
    ai_query = [f'"{kw}"' for kw in ai_keywords]
    
    query = f"({' OR '.join(reproduction_query)}) AND ({' OR '.join(ai_query)})"

    # Instancia del Helper
    helper = SearchHelper()
    strategy_keys = ["pubmed"] # Prueba con busqueda en foro EntrezPubMed; agregar otros
    helper.set_sequential_combined_strategy(strategy_keys)
    papers = helper.execute(query, 10) # 10 papers por sitio

    with open("search_results.json", 'w', encoding='utf-8') as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    print(f"Resultados guardados en search_results.json")
    print(f"{len(papers)} papers encontrados :)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n Error inesperado: {e}")
        sys.exit(1)