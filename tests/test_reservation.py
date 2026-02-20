import os
import unittest

from src.archivos import guardar_lista
from src.customer import RUTA_CLIENTES, Cliente, crear_cliente
from src.hotel import RUTA_HOTELES, Hotel, crear_hotel
from src.reservation import (
    RUTA_RESERVACIONES,
    Reservacion,
    cancelar_reservacion,
    crear_reservacion,
    hay_disponibilidad,
)


class TestReservacion(unittest.TestCase):
    """Pruebas básicas para reservaciones."""

    def setUp(self):
        guardar_lista(RUTA_HOTELES, [])
        guardar_lista(RUTA_CLIENTES, [])
        guardar_lista(RUTA_RESERVACIONES, [])

    def tearDown(self):
        for ruta in [RUTA_HOTELES, RUTA_CLIENTES, RUTA_RESERVACIONES]:
            if os.path.exists(ruta):
                os.remove(ruta)

    def test_crear_reservacion_ok(self):
        crear_hotel(Hotel("H1", "Hotel Centro", "Veracruz", 2))
        crear_cliente(Cliente("C1", "Ricardo", "correo@test.com"))

        r = Reservacion("R1", "H1", "C1", 1)
        self.assertTrue(crear_reservacion(r))

    def test_no_crear_reservacion_hotel_inexistente(self):
        crear_cliente(Cliente("C1", "Ricardo", "correo@test.com"))

        r = Reservacion("R1", "H_NO", "C1", 1)
        self.assertFalse(crear_reservacion(r))

    def test_no_crear_reservacion_cliente_inexistente(self):
        crear_hotel(Hotel("H1", "Hotel Centro", "Veracruz", 2))

        r = Reservacion("R1", "H1", "C_NO", 1)
        self.assertFalse(crear_reservacion(r))

    def test_no_crear_reservacion_sin_disponibilidad(self):
        crear_hotel(Hotel("H1", "Hotel Centro", "Veracruz", 1))
        crear_cliente(Cliente("C1", "Ricardo", "correo@test.com"))
        crear_cliente(Cliente("C2", "Paulina", "paulina@test.com"))

        r1 = Reservacion("R1", "H1", "C1", 1)
        self.assertTrue(crear_reservacion(r1))

        r2 = Reservacion("R2", "H1", "C2", 1)
        self.assertFalse(crear_reservacion(r2))

    def test_no_crear_reservacion_id_repetido(self):
        crear_hotel(Hotel("H1", "Hotel Centro", "Veracruz", 2))
        crear_cliente(Cliente("C1", "Ricardo", "correo@test.com"))
        crear_cliente(Cliente("C2", "Paulina", "paulina@test.com"))

        r1 = Reservacion("R1", "H1", "C1", 1)
        self.assertTrue(crear_reservacion(r1))

        r2 = Reservacion("R1", "H1", "C2", 1)
        self.assertFalse(crear_reservacion(r2))

    def test_cancelar_reservacion_ok(self):
        crear_hotel(Hotel("H1", "Hotel Centro", "Veracruz", 2))
        crear_cliente(Cliente("C1", "Ricardo", "correo@test.com"))

        r = Reservacion("R1", "H1", "C1", 1)
        self.assertTrue(crear_reservacion(r))
        self.assertTrue(cancelar_reservacion("R1"))

    def test_cancelar_reservacion_inexistente(self):
        self.assertFalse(cancelar_reservacion("NO_EXISTE"))

    def test_hay_disponibilidad(self):
        crear_hotel(Hotel("H1", "Hotel Centro", "Veracruz", 1))
        crear_cliente(Cliente("C1", "Ricardo", "correo@test.com"))

        self.assertTrue(hay_disponibilidad("H1", 1))

        r = Reservacion("R1", "H1", "C1", 1)
        self.assertTrue(crear_reservacion(r))

        self.assertFalse(hay_disponibilidad("H1", 1))


if __name__ == "__main__":
    unittest.main()