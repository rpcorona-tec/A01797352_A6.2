"""
Módulo Hotel.

Contiene la clase Hotel y operaciones básicas persistentes en archivo JSON.
"""

from src.archivos import cargar_lista, guardar_lista


RUTA_HOTELES = "data/hotels.json"


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


def crear_hotel(hotel):
    """
    Guarda un hotel nuevo.
    Regresa True si se guardó, False si ya existía.
    """
    hoteles = cargar_lista(RUTA_HOTELES)

    for h in hoteles:
        if h.get("hotel_id") == hotel.hotel_id:
            return False

    hoteles.append(hotel.a_diccionario())
    guardar_lista(RUTA_HOTELES, hoteles)
    return True


def borrar_hotel(hotel_id):
    """
    Borra un hotel por id.
    Regresa True si borró, False si no existía.
    """
    hoteles = cargar_lista(RUTA_HOTELES)
    hoteles_nuevos = [h for h in hoteles if h.get("hotel_id") != str(hotel_id)]

    if len(hoteles_nuevos) == len(hoteles):
        return False

    guardar_lista(RUTA_HOTELES, hoteles_nuevos)
    return True


def obtener_hotel(hotel_id):
    """Regresa un Hotel si existe, si no, None."""
    hoteles = cargar_lista(RUTA_HOTELES)
    for h in hoteles:
        if h.get("hotel_id") == str(hotel_id):
            return Hotel.desde_diccionario(h)
    return None


def actualizar_hotel(hotel):
    """
    Actualiza un hotel existente por id.
    Regresa True si actualizó, False si no existía.
    """
    hoteles = cargar_lista(RUTA_HOTELES)

    for i, h in enumerate(hoteles):
        if h.get("hotel_id") == hotel.hotel_id:
            hoteles[i] = hotel.a_diccionario()
            guardar_lista(RUTA_HOTELES, hoteles)
            return True

    return False


def reservar_cuarto(hotel_id, cliente_id, reservacion_id, cuartos):
    """Crea una reservación (atajo desde hotel)."""
    from src.reservation import Reservacion, crear_reservacion

    reservacion = Reservacion(reservacion_id, hotel_id, cliente_id, cuartos)
    return crear_reservacion(reservacion)


def cancelar_reserva(reservacion_id):
    """Cancela una reservación (atajo desde hotel)."""
    from src.reservation import cancelar_reservacion

    return cancelar_reservacion(reservacion_id)
