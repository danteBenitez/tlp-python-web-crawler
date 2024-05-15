from crawler import crawl
import json
import sys

DEFAULT_URL = "https://docs.astro.build/es/getting-started"

def main():
    """
        Lógica general para acceder al Web Crawler mediante un CLI.
    """
    if "--verbose" in sys.argv:
        print("Iniciando el Web Crawler", file=sys.stderr)
    elif "--help" in sys.argv:
        print("Uso: python -m crawler [URL]", file=sys.stderr)
        print("URL: La URL de la página web que deseas analizar", file=sys.stderr)
        print("--help Muestra este mensaje de ayuda", file=sys.stderr)
        print("--verbose Muestra mensajes de depuración", file=sys.stderr)
        return

    url = DEFAULT_URL
    if len(sys.argv) > 1:
        url = sys.argv[1]

    results = crawl(url)
    with open('results.json', 'w') as file:
        json.dump(results, fp=file)

    print("Resultados guardados en results.json")

if __name__ == "__main__":

    main()