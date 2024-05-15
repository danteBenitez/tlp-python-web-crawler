from crawler import crawl
import json

DEFAULT_URL = "https://www.lamañanaonline.com.ar/"

def main():
    """
        Lógica general para acceder al Web Crawler mediante un CLI.
    """
    results = crawl(DEFAULT_URL)
    with open('results.json', 'w') as file:
        json.dump(results, fp=file)
    print("Resultados guardados en results.json")

if __name__ == "__main__":

    main()