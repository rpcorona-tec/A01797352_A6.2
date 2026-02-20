import os
import unittest

from src.archivos import guardar_lista
from src.hotel import (
    RUTA_HOTELES,
    Hotel,
    actualizar_hotel,
    borrar_hotel,
    crear_hotel,
    obtener_hotel,
)


class TestHotel(unittest.TestCase):
    """Pruebas básicas para operaciones de Hotel."""

    def setUp(self):
        guardar_lista(RUTA_HOTELES, [])

    def test_crear_hotel(self):
        hotel = Hotel("H1", "Hotel Centro", "Veracruz", 10)
        resultado = crear_hotel(hotel)
        self.assertTrue(resultado)

    def test_no_crear_hotel_repetido(self):
        hotel = Hotel("H1", "Hotel Centro", "Veracruz", 10)
        self.assertTrue(crear_hotel(hotel))
        self.assertFalse(crear_hotel(hotel))

    def test_obtener_hotel(self):
        hotel = Hotel("H1", "Hotel Centro", "Veracruz", 10)
        crear_hotel(hotel)

        encontrado = obtener_hotel("H1")
        self.assertIsNotNone(encontrado)
        self.assertEqual("Hotel Centro", encontrado.nombre)

    def test_borrar_hotel(self):
        hotel = Hotel("H1", "Hotel Centro", "Veracruz", 10)
        crear_hotel(hotel)

        self.assertTrue(borrar_hotel("H1"))
        self.assertIsNone(obtener_hotel("H1"))

    def test_borrar_hotel_inexistente(self):
        self.assertFalse(borrar_hotel("NO_EXISTE"))

    def test_actualizar_hotel(self):
        hotel = Hotel("H1", "Hotel Centro", "Veracruz", 10)
        crear_hotel(hotel)

        hotel_actualizado = Hotel("H1", "Hotel Nuevo", "Veracruz", 12)
        self.assertTrue(actualizar_hotel(hotel_actualizado))

        encontrado = obtener_hotel("H1")
        self.assertEqual("Hotel Nuevo", encontrado.nombre)
        self.assertEqual(12, encontrado.cuartos_totales)


if __name__ == "__main__":
    unittest.main()