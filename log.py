import sys

def log_error(*str):
    """
        Imprime un mensaje de error en la salida de error.
    """
    print(file=sys.stderr, *str)
