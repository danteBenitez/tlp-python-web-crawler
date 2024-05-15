from crawler import crawl
from log import log_error
import json
import sys

DEFAULT_URL = "https://docs.astro.build/es/getting-started"

def print_help():
    log_error("""
       Uso: python -m crawler [options] [URL]
       URL: La URL de la página web que deseas analizar
            Si no se proporciona una URL, se utilizará la URL por defecto
       Options:
            --help Muestra este mensaje de ayuda
            --verbose Muestra mensajes de depuración
    """)

def main():
    """
        Lógica general para acceder al Web Crawler mediante un CLI.
    """
    verbose = False
    if "--verbose" in sys.argv:
        print("Iniciando el Web Crawler", file=sys.stderr)
        verbose = True
        sys.argv.remove("--verbose")
    elif "--help" in sys.argv:
        print_help()
        sys.argv.remove("--help")
        return

    url = DEFAULT_URL
    if len(sys.argv) > 1:
        url = sys.argv[1]

    results = crawl(url, verbose=verbose)
    with open('results.json', 'w') as file:
        json.dump(results, fp=file)

    print("Resultados guardados en results.json")

if __name__ == "__main__":
    main()