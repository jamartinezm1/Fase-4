# Módulo de Modelos de Datos - Sistema de Gestión 'Software FJ'

from abc import ABC, abstractmethod

# 1 CLASE ABSTRACTA BASE

class EntidadBase(ABC):
  #Clase abstracta base para garantizar la identificacion de entidades
  
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad  # Atributo protegido
    @property

    def id_entidad(self):
        return self._id_entidad

# 2 CLASE CLIENTE "ENCAPSULAMIENTO Y VALIDACIONES"
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

# 3 CLASE ABSTRACTA SERVICIO Y DERIVADAS "HERENCIA Y POLIMORFISMO"

class Servicio(ABC):
  # Clase abstracta base para los servicios ofrecidos.
     def __init__(self, id_servicio, nombre_servicio, precio_base):
        self.id_servicio = id_servicio
        self.nombre_servicio = nombre_servicio
        self.precio_base = precio_base
    
     @abstractmethod
     def calcular_costo(self, duracion_horas, descuento=0.0):
      pass
    # Método abstracto para calcular el costo según la duración y descuentos.
     @abstractmethod
     def obtener_descripcion(self):
      pass
    # Método abstracto para la descripción polimórfica del servicio.

class ReservaSala(Servicio):
  # Servicio especializado de reserva de salas de reuniones o desarrollo.
  
    def __init__(self, id_servicio, nombre_servicio, precio_base, capacidad_personas):
        super().__init__(id_servicio, nombre_servicio, precio_base)
        self.capacidad_personas = capacidad_personas

    def calcular_costo(self, duracion_horas, descuento=0.0):
        subtotal = self.precio_base * duracion_horas
        total = subtotal * (1 - (descuento / 100))
        return round(total, 2)

    def obtener_descripcion(self):
        return f"[Sala] {self.nombre_servicio} (Capacidad: {self.capacidad_personas} pers.)"

class AlquilerEquipo(Servicio):
  # Servicio especializado de alquiler de hardware y equipos de computo.

    def __init__(self, id_servicio, nombre_servicio, precio_base, deposito_garantia):
        super().__init__(id_servicio, nombre_servicio, precio_base)
        self.deposito_garantia = deposito_garantia

    def calcular_costo(self, duracion_horas, descuento=0.0):
        subtotal = (self.precio_base * duracion_horas) + self.deposito_garantia
        total = subtotal * (1 - (descuento / 100))
        return round(total, 2)

    def obtener_descripcion(self):
        return f"[Equipo] {self.nombre_servicio} (Depósito: ${self.deposito_garantia})"

class AsesoriaEspecializada(Servicio):
  # Servicio especializado de consultoría en software y arquitectura.

    def __init__(self, id_servicio, nombre_servicio, precio_base, especialidad):
        super().__init__(id_servicio, nombre_servicio, precio_base)
        self.especialidad = especialidad

    def calcular_costo(self, duracion_horas, descuento=0.0):
        subtotal = self.precio_base * duracion_horas
        total_con_iva = subtotal * 1.19
        total = total_con_iva * (1 - (descuento / 100))
        return round(total, 2)

    def obtener_descripcion(self):
        return f"[Asesoría] {self.nombre_servicio} - Área: {self.especialidad}"

  



