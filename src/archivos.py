"""
Módulo para manejo básico de archivos JSON.
"""

import json


def cargar_lista(ruta_archivo):
    """
    Carga una lista desde un archivo JSON.
    Si el archivo no existe o está corrupto, regresa lista vacía.
    """
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error al cargar archivo:", ruta_archivo)
        return []


def guardar_lista(ruta_archivo, lista):
    """
    Guarda una lista en un archivo JSON.
    """
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4)