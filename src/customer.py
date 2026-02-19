"""
Módulo Cliente.

Contiene la clase Cliente y funciones simples para convertir a/desde diccionarios.
"""


class Cliente:
    """Representa un cliente."""

    def __init__(self, cliente_id, nombre, correo):
        self.cliente_id = str(cliente_id)
        self.nombre = str(nombre)
        self.correo = str(correo)

    def a_diccionario(self):
        """Convierte el objeto a un diccionario para guardarlo en JSON."""
        return {
            "cliente_id": self.cliente_id,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @staticmethod
    def desde_diccionario(data):
        """Crea un Cliente desde un diccionario."""
        return Cliente(
            data.get("cliente_id"),
            data.get("nombre"),
            data.get("correo"),
        )