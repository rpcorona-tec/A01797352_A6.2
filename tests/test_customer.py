import os
import unittest

from src.archivos import guardar_lista
from src.customer import (
    RUTA_CLIENTES,
    Cliente,
    actualizar_cliente,
    borrar_cliente,
    crear_cliente,
    obtener_cliente,
)


class TestCliente(unittest.TestCase):
    """Pruebas básicas para operaciones de Cliente."""

    def setUp(self):
        guardar_lista(RUTA_CLIENTES, [])

    def tearDown(self):
        if os.path.exists(RUTA_CLIENTES):
            os.remove(RUTA_CLIENTES)

    def test_crear_cliente(self):
        cliente = Cliente("C1", "Ricardo", "correo@test.com")
        self.assertTrue(crear_cliente(cliente))

    def test_no_crear_cliente_repetido(self):
        cliente = Cliente("C1", "Ricardo", "correo@test.com")
        self.assertTrue(crear_cliente(cliente))
        self.assertFalse(crear_cliente(cliente))

    def test_obtener_cliente(self):
        cliente = Cliente("C1", "Ricardo", "correo@test.com")
        crear_cliente(cliente)

        encontrado = obtener_cliente("C1")
        self.assertIsNotNone(encontrado)
        self.assertEqual("Ricardo", encontrado.nombre)

    def test_borrar_cliente(self):
        cliente = Cliente("C1", "Ricardo", "correo@test.com")
        crear_cliente(cliente)

        self.assertTrue(borrar_cliente("C1"))
        self.assertIsNone(obtener_cliente("C1"))

    def test_actualizar_cliente(self):
        cliente = Cliente("C1", "Ricardo", "correo@test.com")
        crear_cliente(cliente)

        actualizado = Cliente("C1", "Nuevo Nombre", "nuevo@test.com")
        self.assertTrue(actualizar_cliente(actualizado))

        encontrado = obtener_cliente("C1")
        self.assertEqual("Nuevo Nombre", encontrado.nombre)


if __name__ == "__main__":
    unittest.main()