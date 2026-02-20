import unittest

from src.archivos import cargar_lista, guardar_lista


class TestArchivos(unittest.TestCase):
    """Pruebas básicas para manejo de archivos."""

    def setUp(self):
        self.ruta_prueba = "data/prueba.json"

    def test_guardar_y_cargar_lista(self):
        datos = [{"id": 1, "nombre": "test"}]
        guardar_lista(self.ruta_prueba, datos)

        resultado = cargar_lista(self.ruta_prueba)
        self.assertEqual(datos, resultado)

    def test_cargar_archivo_inexistente(self):
        resultado = cargar_lista("data/no_existe.json")
        self.assertEqual([], resultado)


if __name__ == "__main__":
    unittest.main()
