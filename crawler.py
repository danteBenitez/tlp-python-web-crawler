import requests
from bs4 import BeautifulSoup
from log import log_error

def get_html_content(url: str) -> BeautifulSoup:
    """
        Obtiene el contenido HTML de una cierta página web y
        lo interpreta.

        :param url URL de la página web
        :type str

        :returns El contenido de la página web como una estructura
        :rtype
    """
    try:
        text = requests.get(url).text
        soup = BeautifulSoup(text, features='html.parser')
        return soup
    except requests.RequestException as err:
        log_error(f"Hubo un error al leer la página con URL {url}", err)
    except Exception as err:
        log_error("Hubo un error desconocido", err)


def crawl(absolute_url: str) -> dict[str, list[str]]:
    """
        Recorre un sitio web, encuentra enlaces y construye un objeto de resultados
        con el contenido de <h1> y <p> como valores, y las URL como claves.
    """
    # Construimos el objeto de resultado
    results = {}
    # Llevamos la cuenta de las URL que debemos visitar
    pages_to_visit = []

    # Obtenemos el contenido de la página principal
    main_content = get_html_content(absolute_url)

    # Encontrar los enlaces
    links = main_content.find_all('a', attrs={
        'href': True,
    })

    for link in links:
        href = link['href']
        # Prevenimos referencias circulares
        if href not in pages_to_visit:
            # Si la URL comienza con #, entonces no debemos seguir el enlace
            if href.startswith('#'):
                continue
            # Si la URL comienza con /, suponemos que debemos agregar la URL de la página
            elif href.startswith('/'):
                pages_to_visit.append(absolute_url + href)
            else:
                pages_to_visit.append(href)

    for url in pages_to_visit:
        # Obtenemos el contenido
        html = get_html_content(url)

        # Creamos la lista de resultados
        results[url] = []

        # Por cada h1 y p encontrado, lo agregamos a la lista
        found = html.find_all(["h1", "p"])
        for content in found:
            results[url].append(str(content))

    return results
