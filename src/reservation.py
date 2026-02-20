"""
Módulo Reservación.
x
Contiene la clase Reservacion y operaciones básicas persistentes
en archivo JSON.
"""

from src.archivos import cargar_lista, guardar_lista
from src.customer import obtener_cliente
from src.hotel import obtener_hotel


RUTA_RESERVACIONES = "data/reservations.json"


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


def cuartos_reservados(hotel_id):
    """Regresa cuántos cuartos están reservados actualmente para un hotel."""
    reservaciones = cargar_lista(RUTA_RESERVACIONES)
    total = 0

    for r in reservaciones:
        if r.get("hotel_id") == str(hotel_id):
            total += int(r.get("cuartos", 0))

    return total


def hay_disponibilidad(hotel_id, cuartos_solicitados):
    """
    Verifica si un hotel tiene disponibilidad.
    Regresa False si no existe el hotel.
    """
    hotel = obtener_hotel(hotel_id)
    if hotel is None:
        return False

    reservados = cuartos_reservados(hotel_id)
    disponibles = hotel.cuartos_totales - reservados
    return disponibles >= int(cuartos_solicitados)


def crear_reservacion(reservacion):
    """
    Crea una reservación si:
    - existe el hotel
    - existe el cliente
    - hay disponibilidad
    - no existe el id de reservación
    Regresa True/False.
    """
    if obtener_hotel(reservacion.hotel_id) is None:
        return False

    if obtener_cliente(reservacion.cliente_id) is None:
        return False

    if not hay_disponibilidad(reservacion.hotel_id, reservacion.cuartos):
        return False

    reservaciones = cargar_lista(RUTA_RESERVACIONES)
    for r in reservaciones:
        if r.get("reservacion_id") == reservacion.reservacion_id:
            return False

    reservaciones.append(reservacion.a_diccionario())
    guardar_lista(RUTA_RESERVACIONES, reservaciones)
    return True


def cancelar_reservacion(reservacion_id):
    """
    Cancela (elimina) una reservación por id.
    Regresa True si eliminó, False si no existe.
    """
    reservaciones = cargar_lista(RUTA_RESERVACIONES)
    nuevas = [r for r in reservaciones
              if r.get("reservacion_id") != str(reservacion_id)]

    if len(nuevas) == len(reservaciones):
        return False

    guardar_lista(RUTA_RESERVACIONES, nuevas)
    return True
