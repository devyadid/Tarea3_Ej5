# vehiculos.py

from datetime import datetime

class Vehiculo:
    """Clase base para un vehículo."""
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        """Mensaje genérico al arrancar un vehículo."""
        return f"{self.marca} {self.modelo}: El vehículo está en marcha."

class Coche(Vehiculo):
    """Subclase que representa un coche."""
    def arrancar(self):
        """Mensaje personalizado al arrancar un coche."""
        return f"{self.marca} {self.modelo}: El coche está arrancando con suavidad."

class Moto(Vehiculo):
    """Subclase que representa una moto."""
    def arrancar(self):
        """Mensaje personalizado al arrancar una moto."""
        return f"{self.marca} {self.modelo}: La moto está rugiendo lista para rodar."

if __name__ == "__main__":
    # Fecha y hora para la evidencia
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Ejecución realizada el: {ahora}\n")

    # Crear instancias y mostrar mensajes
    vehiculos = [
        Vehiculo("Genérico", "ModeloX"),
        Coche("Toyota", "Corolla"),
        Moto("Yamaha", "MT-07")
    ]

    for v in vehiculos:
        print(v.arrancar())
