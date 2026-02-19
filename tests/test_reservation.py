import unittest

from src.reservation import Reservacion


class TestReservacion(unittest.TestCase):
    """Pruebas básicas para Reservacion."""

    def test_creacion_reservacion(self):
        reservacion = Reservacion("R1", "H1", "C1", 1)
        self.assertEqual("R1", reservacion.reservacion_id)
        self.assertEqual(1, reservacion.cuartos)


if __name__ == "__main__":
    unittest.main()