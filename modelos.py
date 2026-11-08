# Módulo de Modelos de Datos - Sistema de Gestión 'Software FJ'

import math
import re
from abc import ABC, abstractmethod
 
from excepciones import ParametroInvalidoError, ClienteInvalidoError
 
 

# FUNCIONES AUXILIARES DE VALIDACIÓN

def _es_numero(valor):
    """True si el valor es un número real válido (excluye bool, NaN e infinito)."""
    return (
        isinstance(valor, (int, float))
        and not isinstance(valor, bool)
        and math.isfinite(valor)
    )
 
 
def _validar_texto(valor, campo):
    """Valida que el valor sea un texto no vacío y lo devuelve sin espacios sobrantes."""
    if not isinstance(valor, str) or not valor.strip():
        raise ParametroInvalidoError(f"{campo} debe ser un texto no vacío.")
    return valor.strip()
 
 
def _validar_numero(valor, campo, minimo_exclusivo=None, minimo=None, maximo=None):
    """Valida que el valor sea numérico y esté dentro del rango indicado."""
    if not _es_numero(valor):
        raise ParametroInvalidoError(f"{campo} debe ser un número válido.")
    if minimo_exclusivo is not None and valor <= minimo_exclusivo:
        raise ParametroInvalidoError(f"{campo} debe ser mayor que {minimo_exclusivo}.")
    if minimo is not None and valor < minimo:
        raise ParametroInvalidoError(f"{campo} no puede ser menor que {minimo}.")
    if maximo is not None and valor > maximo:
        raise ParametroInvalidoError(f"{campo} no puede ser mayor que {maximo}.")
    return valor
 
 

# 1. CLASE ABSTRACTA BASE

class EntidadBase(ABC):
    """Clase abstracta que representa cualquier entidad identificable del sistema."""
 
    def __init__(self, id_entidad):
        if id_entidad is None or (isinstance(id_entidad, str) and not id_entidad.strip()):
            raise ParametroInvalidoError("El identificador de la entidad no puede estar vacío.")
        self._id_entidad = id_entidad  # Atributo protegido
 
    @property
    def id_entidad(self):
        return self._id_entidad
 
    @abstractmethod
    def obtener_informacion(self):
        """Cada entidad debe poder describirse a sí misma en un texto."""
        pass
 
 

# 2. CLASE CLIENTE (ENCAPSULAMIENTO Y VALIDACIONES)

class Cliente(EntidadBase):
    """Cliente de Software FJ. Sus datos personales están encapsulados y validados."""
 
    _PATRON_CEDULA = re.compile(r"[0-9]{6,12}")
    _PATRON_CORREO = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")
    _PATRON_TELEFONO = re.compile(r"\+?[0-9]{7,15}")
 
    def __init__(self, cedula, nombre, correo, telefono):
        super().__init__(self._validar_cedula(cedula))
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
 
    # --- Cédula (solo lectura, se valida al crear el cliente) ---
    @classmethod
    def _validar_cedula(cls, cedula):
        if isinstance(cedula, bool) or not isinstance(cedula, (str, int)):
            raise ClienteInvalidoError("La cédula debe ser un texto o un número.")
        texto = str(cedula).strip()
        if not cls._PATRON_CEDULA.fullmatch(texto):
            raise ClienteInvalidoError("La cédula debe tener solo dígitos (entre 6 y 12).")
        return texto
 
    # --- Nombre ---
    @property
    def nombre(self):
        return self._nombre
 
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise ClienteInvalidoError("El nombre del cliente debe ser un texto de al menos 2 caracteres.")
        self._nombre = valor.strip()
 
    # --- Correo ---
    @property
    def correo(self):
        return self._correo
 
    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or not self._PATRON_CORREO.fullmatch(valor.strip()):
            raise ClienteInvalidoError("Formato de correo electrónico inválido.")
        self._correo = valor.strip()
 
    # --- Teléfono ---
    @property
    def telefono(self):
        return self._telefono
 
    @telefono.setter
    def telefono(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (str, int)):
            raise ClienteInvalidoError("El teléfono debe ser un texto o un número.")
        limpio = re.sub(r"[\s\-]", "", str(valor))
        if not self._PATRON_TELEFONO.fullmatch(limpio):
            raise ClienteInvalidoError("El teléfono debe tener entre 7 y 15 dígitos.")
        self._telefono = limpio
 
    def obtener_informacion(self):
        """Retorna un resumen formateado de los datos del cliente."""
        return (
            f"Cliente: {self.nombre} | CC: {self.id_entidad} | "
            f"Email: {self.correo} | Tel: {self.telefono}"
        )
 
    def __str__(self):
        return self.obtener_informacion()
 
 

# 3. CLASE ABSTRACTA SERVICIO Y DERIVADAS (HERENCIA Y POLIMORFISMO)

class Servicio(EntidadBase):
    """Clase abstracta base para los servicios ofrecidos por Software FJ."""
 
    # Impuesto (en %) que se aplica si no se indica uno al calcular el costo.
    IMPUESTO_POR_DEFECTO = 0.0
 
    def __init__(self, id_servicio, nombre_servicio, precio_base, disponible=True):
        super().__init__(id_servicio)
        self.nombre_servicio = nombre_servicio
        self.precio_base = precio_base
        self.disponible = disponible
 
    # --- Propiedades encapsuladas ---
    @property
    def id_servicio(self):
        return self.id_entidad
 
    @property
    def nombre_servicio(self):
        return self._nombre_servicio
 
    @nombre_servicio.setter
    def nombre_servicio(self, valor):
        self._nombre_servicio = _validar_texto(valor, "El nombre del servicio")
 
    @property
    def precio_base(self):
        return self._precio_base
 
    @precio_base.setter
    def precio_base(self, valor):
        self._precio_base = _validar_numero(valor, "El precio base", minimo_exclusivo=0)
 
    @property
    def disponible(self):
        return self._disponible
 
    @disponible.setter
    def disponible(self, valor):
        if not isinstance(valor, bool):
            raise ParametroInvalidoError("La disponibilidad del servicio debe ser True o False.")
        self._disponible = valor
 
    # --- Validación de parámetros (se sobrescribe en cada servicio) ---
    def validar_parametros(self):
        """Revalida el estado del servicio. Lanza ParametroInvalidoError si algo es inconsistente."""
        _validar_texto(self._nombre_servicio, "El nombre del servicio")
        _validar_numero(self._precio_base, "El precio base", minimo_exclusivo=0)
        return True
 
    def _validar_parametros_calculo(self, duracion_horas, descuento, impuesto):
        """Valida los datos del cálculo y devuelve el impuesto a aplicar (en %)."""
        _validar_numero(duracion_horas, "La duración", minimo_exclusivo=0)
        _validar_numero(descuento, "El descuento", minimo=0, maximo=100)
        if impuesto is None:
            impuesto = self.IMPUESTO_POR_DEFECTO
        _validar_numero(impuesto, "El impuesto", minimo=0, maximo=100)
        return impuesto
 
    @staticmethod
    def _aplicar_descuento_e_impuesto(subtotal, descuento, impuesto):
        """Aplica primero el descuento y luego el impuesto (ambos en %)."""
        return subtotal * (1 - descuento / 100) * (1 + impuesto / 100)
 
    # --- Métodos abstractos (polimorfismo) ---
    @abstractmethod
    def calcular_costo(self, duracion_horas, descuento=0.0, impuesto=None):
        """
        Calcula el costo del servicio. Parámetros opcionales (sobrecarga):
          - calcular_costo(horas)                        -> sin descuento, impuesto por defecto
          - calcular_costo(horas, descuento)             -> con descuento (%)
          - calcular_costo(horas, descuento, impuesto)   -> con descuento e impuesto (%)
        """
        pass
 
    @abstractmethod
    def obtener_descripcion(self):
        """Descripción polimórfica del servicio."""
        pass
 
    # --- Variante del cálculo de costos (sobrecarga por nombre) ---
    def calcular_costo_con_impuesto(self, duracion_horas, impuesto, descuento=0.0):
        """Variante que obliga a indicar el impuesto (en %) del cálculo."""
        return self.calcular_costo(duracion_horas, descuento, impuesto)
 
    def obtener_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.obtener_descripcion()} | Precio base: ${self.precio_base}/h | {estado}"
 
    def __str__(self):
        return self.obtener_descripcion()
 
 
class ReservaSala(Servicio):
    """Servicio especializado de reserva de salas de reuniones o desarrollo."""
 
    def __init__(self, id_servicio, nombre_servicio, precio_base, capacidad_personas, disponible=True):
        super().__init__(id_servicio, nombre_servicio, precio_base, disponible)
        self.capacidad_personas = capacidad_personas
 
    @property
    def capacidad_personas(self):
        return self._capacidad_personas
 
    @capacidad_personas.setter
    def capacidad_personas(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int) or valor <= 0:
            raise ParametroInvalidoError("La capacidad de la sala debe ser un entero mayor que 0.")
        self._capacidad_personas = valor
 
    def validar_parametros(self):
        super().validar_parametros()
        if isinstance(self._capacidad_personas, bool) or not isinstance(self._capacidad_personas, int) \
                or self._capacidad_personas <= 0:
            raise ParametroInvalidoError("La capacidad de la sala debe ser un entero mayor que 0.")
        return True
 
    def calcular_costo(self, duracion_horas, descuento=0.0, impuesto=None):
        # Costo por horas, con descuento e impuesto opcionales
        self.validar_parametros()
        impuesto = self._validar_parametros_calculo(duracion_horas, descuento, impuesto)
        subtotal = self.precio_base * duracion_horas
        return round(self._aplicar_descuento_e_impuesto(subtotal, descuento, impuesto), 2)
 
    def obtener_descripcion(self):
        return f"[Sala] {self.nombre_servicio} (Capacidad: {self.capacidad_personas} pers.)"
 
 
class AlquilerEquipo(Servicio):
    """Servicio especializado de alquiler de hardware y equipos de cómputo."""
 
    def __init__(self, id_servicio, nombre_servicio, precio_base, deposito_garantia, disponible=True):
        super().__init__(id_servicio, nombre_servicio, precio_base, disponible)
        self.deposito_garantia = deposito_garantia
 
    @property
    def deposito_garantia(self):
        return self._deposito_garantia
 
    @deposito_garantia.setter
    def deposito_garantia(self, valor):
        self._deposito_garantia = _validar_numero(valor, "El depósito de garantía", minimo=0)
 
    def validar_parametros(self):
        super().validar_parametros()
        _validar_numero(self._deposito_garantia, "El depósito de garantía", minimo=0)
        return True
 
    def calcular_costo(self, duracion_horas, descuento=0.0, impuesto=None):
        # El descuento y el impuesto aplican al alquiler; el depósito de garantía
        # es reembolsable, por eso se suma al final sin descuento ni impuesto.
        self.validar_parametros()
        impuesto = self._validar_parametros_calculo(duracion_horas, descuento, impuesto)
        alquiler = self.precio_base * duracion_horas
        total = self._aplicar_descuento_e_impuesto(alquiler, descuento, impuesto) + self.deposito_garantia
        return round(total, 2)
 
    def obtener_descripcion(self):
        return f"[Equipo] {self.nombre_servicio} (Depósito: ${self.deposito_garantia})"
 
 
class AsesoriaEspecializada(Servicio):
    """Servicio especializado de consultoría en software y arquitectura."""
 
    # Las asesorías incluyen un 19% de IVA obligatorio por honorarios
    IMPUESTO_POR_DEFECTO = 19.0
 
    def __init__(self, id_servicio, nombre_servicio, precio_base, especialidad, disponible=True):
        super().__init__(id_servicio, nombre_servicio, precio_base, disponible)
        self.especialidad = especialidad
 
    @property
    def especialidad(self):
        return self._especialidad
 
    @especialidad.setter
    def especialidad(self, valor):
        self._especialidad = _validar_texto(valor, "La especialidad")
 
    def validar_parametros(self):
        super().validar_parametros()
        _validar_texto(self._especialidad, "La especialidad")
        return True
 
    def calcular_costo(self, duracion_horas, descuento=0.0, impuesto=None):
        self.validar_parametros()
        impuesto = self._validar_parametros_calculo(duracion_horas, descuento, impuesto)
        if impuesto < self.IMPUESTO_POR_DEFECTO:
            raise ParametroInvalidoError(
                f"El IVA de {self.IMPUESTO_POR_DEFECTO}% es obligatorio en las asesorías."
            )
        subtotal = self.precio_base * duracion_horas
        return round(self._aplicar_descuento_e_impuesto(subtotal, descuento, impuesto), 2)
 
    def obtener_descripcion(self):
        return f"[Asesoría] {self.nombre_servicio} - Área: {self.especialidad}"