import unittest

from src.customer import Cliente


class TestCliente(unittest.TestCase):
    """Pruebas básicas para Cliente."""

    def test_creacion_cliente(self):
        cliente = Cliente("C1", "Ricardo", "ricardo@email.com")
        self.assertEqual("C1", cliente.cliente_id)


if __name__ == "__main__":
    unittest.main()