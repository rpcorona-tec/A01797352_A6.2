"""
Módulo Hotel.

Contiene la clase Hotel y funciones simples para convertir a/desde diccionarios.
"""


class Hotel:
    """Representa un hotel."""

    def __init__(self, hotel_id, nombre, ciudad, cuartos_totales):
        self.hotel_id = str(hotel_id)
        self.nombre = str(nombre)
        self.ciudad = str(ciudad)
        self.cuartos_totales = int(cuartos_totales)

    def a_diccionario(self):
        """Convierte el objeto a un diccionario para guardarlo en JSON."""
        return {
            "hotel_id": self.hotel_id,
            "nombre": self.nombre,
            "ciudad": self.ciudad,
            "cuartos_totales": self.cuartos_totales,
        }

    @staticmethod
    def desde_diccionario(data):
        """Crea un Hotel desde un diccionario."""
        return Hotel(
            data.get("hotel_id"),
            data.get("nombre"),
            data.get("ciudad"),
            data.get("cuartos_totales"),
        )