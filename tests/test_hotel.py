import unittest

from src.hotel import Hotel


class TestHotel(unittest.TestCase):
    """Pruebas básicas para Hotel."""

    def test_creacion_hotel(self):
        hotel = Hotel("H1", "Hotel Centro", "Veracruz", 10)
        self.assertEqual("H1", hotel.hotel_id)
        self.assertEqual(10, hotel.cuartos_totales)


if __name__ == "__main__":
    unittest.main()