# **Web Crawling** con Python


## Definición de Web Crawler:
Un web crawler, también conocido como araña web o rastreador web, es un programa
informático diseñado para explorar automáticamente la World Wide Web de manera metódica y
sistemática. Utiliza algoritmos para navegar por las páginas web, recopilar información y seguir enlaces a otras páginas.

## Para qué sirve un Web Crawler:
Los web crawlers tienen una variedad de aplicaciones, algunas de las cuales incluyen:

- **Recuperación de Información**:
Los motores de búsqueda utilizan web crawlers para indexar páginas web y recopilar
información sobre el contenido de estas páginas. Esto permite a los usuarios realizar búsquedas
efectivas y encontrar información relevante en la web.

- **Monitoreo y Análisis de Contenido**:
Las empresas pueden utilizar web crawlers para monitorear la web en busca de contenido
relevante sobre su marca, productos o competidores. Esto les permite realizar análisis de
mercado y tomar decisiones informadas.

- **Obtención de Datos**:
Los web crawlers pueden ser utilizados para extraer datos específicos de sitios web, como
precios de productos, información de contacto o noticias. Esta información puede ser utilizada
para diversos fines, como análisis de datos, investigación de mercado o creación de bases de
datos.

## Criterios

- **Funcionalidad**
El web crawler debe ser capaz de recorrer el sitio web de manera efectiva y extraer
todas las etiquetas &lt;a&gt; con sus enlaces correspondientes. Debe acceder a cada enlace encontrado y obtener el contenido completo de la página enlazada. La información extraída debe ser almacenada correctamente en un archivo JSON siguiendo el formato especificado.
- **Manejo de Errores**
El programa debe manejar adecuadamente situaciones de error, como páginas no
encontradas, errores de conexión, o problemas de formato de HTML.
- **Legibilidad y Organización del Código**
El código debe estar bien organizado y estructurado, con nombres descriptivos de
variables y funciones.
- **Presentación del Trabajo Práctico**:
La presentación del trabajo práctico debe realizarse en un repositorio de GitHub, el cual
debe ser público para su posterior revisión y evaluación.

## Objetivo:
El objetivo de este trabajo pr&aacute;ctico es implementar un web crawler en Python que pueda
recorrer un sitio web, extraer todas las etiquetas &lt;a&gt; con sus respectivos enlaces y acceder a cada p&aacute;gina enlazada. Por cada enlace encontrado, se deben obtener todas las etiquetas &lt;h1&gt; y
&lt;p&gt; y almacenarlo en un array en un archivo JSON y si no se encuentran dichos elementos
guardar el array como vac&iacute;o. Por ejemplo, si el crawler encuentra un enlace
https://example.com/pagina1 en una p&aacute;gina y accede a ese enlace, debe obtener el contenido
de la p&aacute;gina https://example.com/pagina1 y buscar todos los elementos &lt;h1&gt;&lt;/h1&gt; y
&lt;p&gt;&lt;/p&gt;, luego almacenarlo en un array en un archivo JSON bajo la clave
&quot;https://example.com/pagina1&quot; con el array de los elementos solicitados de la p&aacute;gina como
valor correspondiente y si no se encuentran dichos elementos guardar el array vac&iacute;o. Ejemplo:

```json
{
    "https://example.com/pagina1": ["<h1>Titutulo 1</h1>", "<p>Texto parrafo</p>"],
    "https://example.com/pagina2": ["<h1>Titutulo 1</h1>"],
    "https://example.com/pagina3": [],
}
```

## Sobre el proyecto

### Requerimientos

- Python en su última versión
- `pip` y `venv`

### Pasos para inicializar el proyecto

- Crear y activar entorno virtual

```bash
$ python3 -m venv .env
$ source .env/bin/activate
# o
$ .env/Scripts/activate
```
- Instalar las dependencias:

```bash
$ pip install -r requirements.txt
```

- Ejecutar proyecto: 

```bash
$ python3 __init__.py
```