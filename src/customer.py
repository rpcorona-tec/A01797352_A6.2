"""
Módulo Cliente.

Contiene la clase Cliente y operaciones básicas persistentes en archivo JSON.
"""

from src.archivos import cargar_lista, guardar_lista


RUTA_CLIENTES = "data/customers.json"


class Cliente:
    """Representa un cliente."""

    def __init__(self, cliente_id, nombre, correo):
        self.cliente_id = str(cliente_id)
        self.nombre = str(nombre)
        self.correo = str(correo)

    def a_diccionario(self):
        """Convierte el objeto a diccionario."""
        return {
            "cliente_id": self.cliente_id,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @staticmethod
    def desde_diccionario(data):
        """Crea un Cliente desde diccionario."""
        return Cliente(
            data.get("cliente_id"),
            data.get("nombre"),
            data.get("correo"),
        )


def crear_cliente(cliente):
    clientes = cargar_lista(RUTA_CLIENTES)

    for c in clientes:
        if c.get("cliente_id") == cliente.cliente_id:
            return False

    clientes.append(cliente.a_diccionario())
    guardar_lista(RUTA_CLIENTES, clientes)
    return True


def borrar_cliente(cliente_id):
    clientes = cargar_lista(RUTA_CLIENTES)
    nuevos = [c for c in clientes if c.get("cliente_id") != str(cliente_id)]

    if len(nuevos) == len(clientes):
        return False

    guardar_lista(RUTA_CLIENTES, nuevos)
    return True


def obtener_cliente(cliente_id):
    clientes = cargar_lista(RUTA_CLIENTES)

    for c in clientes:
        if c.get("cliente_id") == str(cliente_id):
            return Cliente.desde_diccionario(c)

    return None


def actualizar_cliente(cliente):
    clientes = cargar_lista(RUTA_CLIENTES)

    for i, c in enumerate(clientes):
        if c.get("cliente_id") == cliente.cliente_id:
            clientes[i] = cliente.a_diccionario()
            guardar_lista(RUTA_CLIENTES, clientes)
            return True

    return False
