# Módulo de Modelos de Datos - Sistema de Gestión 'Software FJ'

from abc import ABC, abstractmethod

# 1. CLASE ABSTRACTA BASE

class EntidadBase(ABC):
  #Clase abstracta base para garantizar la identificacion de entidades
  
  def __init__(self, id_entidad):
        self._id_entidad = id_entidad  # Atributo protegido
    @property
  def id_entidad(self):
    return self._id_entidad

# 2. CLASE CLIENTE "ENCAPSULAMIENTO Y VALIDACIONES"
class Cliente(EntidadBase):
  #Clase que representa a un cliente

def __init__(self, cedula, nombre, correo, telefono):
        super().__init__(cedula)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
@property
    def nombre(self):
        return self._nombre

@nombre.setter
    def nombre(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre del cliente no puede estar vacío.")
        self._nombre = valor.strip()

@property
    def correo(self):
        return self._correo

@correo.setter
    def correo(self, valor):
        if "@" not in valor or "." not in valor:
            raise ValueError("Formato de correo electrónico inválido.")
        self._correo = valor.strip()

def obtener_informacion(self):
        #Retorna un resumen formateado de los datos del cliente
        return f"Cliente: {self.nombre} | CC: {self.id_entidad} | Email: {self.correo}"
