# Importamos las excepciones y el sistema de logs que ya creamos
from excepciones import ServicioNoDisponibleError, ParametroInvalidoError, OperacionNoPermitidaError, ReservaError
from logs import registrar_log

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if cliente is None:
            raise ParametroInvalidoError("El cliente es obligatorio.")
        if servicio is None:
            raise ParametroInvalidoError("El servicio es obligatorio.")
        if not isinstance(duracion, (int, float)):
            raise ParametroInvalidoError("La duración debe ser un número válido.")
        """Constructor de la reserva: recibe un objeto cliente, un objeto servicio y la duración en horas/días."""
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente" # Toda reserva inicia como pendiente

    def confirmar_reserva(self):
        """Método para confirmar la reserva aplicando manejo avanzado de excepciones."""
        try:
            #Rechazo de metodos no validos
            if self.estado == "Cancelada":
                raise OperacionNoPermitidaError("No se puede confirmar una reserva cancelada.")
            if self.estado == "Confirmada":
                raise OperacionNoPermitidaError("La reserva ya se encuentra confirmada.")
            
            # Validación de tiempo 
            if self.duracion <= 0:
                raise ParametroInvalidoError("La duración de la reserva debe ser mayor a 0.")
            
            # Verificacón de disponibilidiad
            if hasattr(self.servicio, 'disponible') and not self.servicio.disponible:
                raise ServicioNoDisponibleError("El servicio no se encuentra disponible.")
        
        except OperacionNoPermitidaError as error:
            registrar_log(f"Operación no permitida: {error}")
            print(f"[-] Operación no permitida: {error}")
            # Si todo sale bien, entra al bloque 'else'
        except ParametroInvalidoError as error:
            # Si ocurre un error, lo guarda en log
            registrar_log(f"Error al confirmar reserva: {error}")
            print(f"[-] Ocurrió un problema: {error}")
        except ServicioNoDisponibleError as error:
            registrar_log(f"Servicio no disponible: {error}")
            print(f"[-] Servicio no disponible: {error}")
        except Exception as error:
            registrar_log(f"Error inesperado en reserva: {error}")
            print(f"[-] Error inesperado: {error}")
        else:
            # Para confirmar la reserva
            self.estado = "Confirmada"
            registrar_log("Reserva confirmada", "INFO")
            print("[+] ¡Reserva confirmada con éxito!")
        finally:
            # Cierre de la reserva
            print("[*] Proceso de confirmación de reserva finalizado.\n")
            
    def cancelar_reserva(self):
        """Método para cancelar la reserva aplicando manejo avanzado de excepciones."""
        try:
            if self.estado == "Cancelada":
                raise OperacionNoPermitidaError("La reserva ya se encuentra cancelada.")
        except OperacionNoPermitidaError as error:
            registrar_log(f"Error al cancelar reserva: {error}")
            print(f"[-] No se pudo cancelar: {error}")
        else:
            self.estado = "Cancelada"
            print("[+] Reserva cancelada exitosamente.")
        finally:
            print("[*] Proceso de cancelación finalizado.\n")
            
    def procesar_reserva(self):
        """Procesa la reserva, calcula el y la confirma."""
        try:
            costo = self.servicio.calcular_costo(self.duracion)
        except (TypeError, ValueError, ParametroInvalidoError) as error:
            raise ReservaError("No se pudo calcular el costo de la reserva") from error
        
        self.confirmar_reserva()
        return costo
            
