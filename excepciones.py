# Se definió una excepción base para todos los errores de reserva
class ReservaError(Exception):
    """Clase base para excepciones relacionadas con las reservas."""
    pass

# Esta es una excepción específica si un servicio no se encuentra disponible
class ServicioNoDisponibleError(ReservaError):
    def __init__(self, mensaje="El servicio seleccionado no está disponible en este momento."):
        super().__init__(mensaje)

# Esta excepción específica es para cuando los parámetros de la reserva no son válidos 
class ParametroInvalidoError(ReservaError):
    def __init__(self, mensaje="Los datos o parámetros proporcionados para la reserva son inválidos."):
        super().__init__(mensaje)
        
#Esta excepción específica es para cuando los datos del cliente no son válidos        
class ClienteInvalidoError(ReservaError):
    def __init__(self, mensaje="Los datos del cliente no son válidos."):
        super().__init__(mensaje)
        
# Excepción para controlar reglas de negocio cuando se intenta ejecutar una acción no válida según el estado actual del sistema
class OperacionNoPermitidaError(ReservaError):
    def __init__(self, mensaje="La operación solicitada no está permitida."):
        super().__init__(mensaje)