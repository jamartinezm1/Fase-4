# Módulo de Gestión de Reservas
# Se define por meido de la clase Reserva con encapsulamiento, la validación de tipos y manejo de excepciones.

from excepciones import (
    ServicioNoDisponibleError,
    ParametroInvalidoError,
    OperacionNoPermitidaError,
)
from logs import registrar_log
from modelos import Cliente, Servicio


class Reserva:
    #Representa una reserva asociando a un Cliente con un Servicio.

    def __init__(self, cliente, servicio, duracion):
        
        #Constructor de la reserva: procede a validar que cliente y el servicio sean instancias válidas,
        #procede a encapsular los atributos e inicializa el estado en 'Pendiente'.
        
        if not isinstance(cliente, Cliente):
            raise ParametroInvalidoError("La reserva requiere una instancia válida de Cliente.")
        if not isinstance(servicio, Servicio):
            raise ParametroInvalidoError("La reserva requiere una instancia válida de Servicio.")

        self._cliente = cliente
        self._servicio = servicio
        self.duracion = duracion
        self._estado = "Pendiente"  # Atributo protegido: solo cambia mediante métodos controlados

    # Propiedades encapsuladas 
    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def estado(self):
        return self._estado

    # Propiedad duracion con validación
    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ParametroInvalidoError("La duración de la reserva debe ser un valor numérico.")
        self._duracion = valor

    # Método auxiliar de costo
    def calcular_total(self, descuento=0.0, impuesto=None):
        # Delega el cálculo del costo al servicio.
        return self._servicio.calcular_costo(self._duracion, descuento, impuesto)

    # Métodos de negocio con manejo de excepciones 
    def confirmar_reserva(self):
        # Método para confirmar la reserva.
        try:
            # No se permite confirmar una reserva previamente cancelada
            if self._estado == "Cancelada":
                raise OperacionNoPermitidaError("No se puede confirmar una reserva que ya fue cancelada.")

            # Validación de tiempo
            if self._duracion <= 0:
                raise ParametroInvalidoError("La duración de la reserva debe ser mayor a 0.")

            # Verificación de disponibilidad
            if hasattr(self._servicio, "disponible") and not self._servicio.disponible:
                raise ServicioNoDisponibleError("El servicio no se encuentra disponible.")

        except (ParametroInvalidoError, ServicioNoDisponibleError, OperacionNoPermitidaError) as error:
            registrar_log(f"Error al confirmar reserva: {error}")
            print(f"[-] Ocurrió un problema: {error}")
        except Exception as error:
            registrar_log(f"Error inesperado en reserva: {error}")
            print(f"[-] Error inesperado: {error}")
        else:
            self._estado = "Confirmada"
            print("[+] ¡Reserva confirmada con éxito!")
        finally:
            print("[*] Proceso de confirmación de reserva finalizado.\n")

    def cancelar_reserva(self):
        # Método para cancelar la reserva.
        try:
            if self._estado == "Cancelada":
                raise OperacionNoPermitidaError("La reserva ya se encuentra cancelada.")
        except OperacionNoPermitidaError as error:
            registrar_log(f"Error al cancelar reserva: {error}")
            print(f"[-] No se pudo cancelar: {error}")
        else:
            self._estado = "Cancelada"
            print("[+] Reserva cancelada exitosamente.")
        finally:
            print("[*] Proceso de cancelación finalizado.\n")

    def obtener_resumen(self):
        # Retorna un resumen legible de la reserva.
        return (
            f"Reserva [{self._estado}] | Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre_servicio} | Duración: {self._duracion}h"
        )

    def __str__(self):
        return self.obtener_resumen()