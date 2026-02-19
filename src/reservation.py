"""
Módulo Reservación.

Contiene la clase Reservacion y funciones simples para convertir a/desde diccionarios.
"""


class Reservacion:
    """Representa una reservación."""

    def __init__(self, reservacion_id, hotel_id, cliente_id, cuartos):
        self.reservacion_id = str(reservacion_id)
        self.hotel_id = str(hotel_id)
        self.cliente_id = str(cliente_id)
        self.cuartos = int(cuartos)

    def a_diccionario(self):
        """Convierte el objeto a un diccionario para guardarlo en JSON."""
        return {
            "reservacion_id": self.reservacion_id,
            "hotel_id": self.hotel_id,
            "cliente_id": self.cliente_id,
            "cuartos": self.cuartos,
        }

    @staticmethod
    def desde_diccionario(data):
        """Crea una Reservacion desde un diccionario."""
        return Reservacion(
            data.get("reservacion_id"),
            data.get("hotel_id"),
            data.get("cliente_id"),
            data.get("cuartos"),
        )