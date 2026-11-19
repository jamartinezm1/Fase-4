# Módulo controlador del sistema - Software FJ
# Centraliza el registro de clientes, el catálogo de servicios y el control de reservas.

from excepciones import (
    ClienteInvalidoError,
    ParametroInvalidoError,
    ServicioNoDisponibleError,
    OperacionNoPermitidaError,
)
from modelos import Cliente, Servicio
from reserva import Reserva


class GestorSistema:
    #Administra las operaciones principales de Software FJ desde un solo punto.

    def __init__(self):
        # Usamos diccionarios indexados por ID/cédula para evitar duplicados y buscar rápido
        self._clientes = {}
        self._servicios = {}
        self._reservas = []

    # Propiedades de solo lectura (devuelven copias para proteger las colecciones internas)
    @property
    def clientes(self):
        return list(self._clientes.values())

    @property
    def servicios(self):
        return list(self._servicios.values())

    @property
    def reservas(self):
        return list(self._reservas)

    
    # GESTIÓN DE CLIENTES
    
    def registrar_cliente(self, cliente):
        # Agrega un cliente al sistema verificando que no esté duplicado por cédula.
        if not isinstance(cliente, Cliente):
            raise ClienteInvalidoError("Solo se pueden registrar objetos de tipo Cliente.")

        if cliente.id_entidad in self._clientes:
            raise OperacionNoPermitidaError(
                f"Ya existe un cliente registrado con la cédula {cliente.id_entidad}."
            )

        self._clientes[cliente.id_entidad] = cliente
        return cliente

    def buscar_cliente(self, cedula):
        # Busca un cliente por su número de cédula. Lanza error si no aparece.
        cedula_limpia = str(cedula).strip()
        cliente = self._clientes.get(cedula_limpia)
        if cliente is None:
            raise ClienteInvalidoError(f"No se encontró ningún cliente con la cédula {cedula_limpia}.")
        return cliente

    # =========================================================
    # GESTIÓN DE SERVICIOS
    # =========================================================
    def agregar_servicio(self, servicio):
        # Incorpora un servicio al catálogo de Software FJ.
        if not isinstance(servicio, Servicio):
            raise ParametroInvalidoError("El elemento debe ser un Servicio válido.")

        if servicio.id_servicio in self._servicios:
            raise OperacionNoPermitidaError(
                f"El código de servicio '{servicio.id_servicio}' ya está en uso."
            )

        self._servicios[servicio.id_servicio] = servicio
        return servicio

    def buscar_servicio(self, id_servicio):
        # Localiza un servicio por su código identificador.
        codigo = str(id_servicio).strip()
        servicio = self._servicios.get(codigo)
        if servicio is None:
            raise ParametroInvalidoError(f"No existe un servicio registrado con el código '{codigo}'.")
        return servicio

    def listar_servicios_disponibles(self):
        # Filtra y retorna únicamente los servicios que están habilitados para reservar.
        return [srv for srv in self._servicios.values() if srv.disponible]

   
    # GESTIÓN DE RESERVAS
    
    def crear_reserva(self, cedula_cliente, id_servicio, duracion, confirmar_de_inmediato=True):
       
        #1. Verifica que cliente y servicio existan en el gestor.
        #2. Valida que el servicio esté disponible.
        #3. Instancia la reserva, la confirma (si se solicita) y la guarda en el historial.
        
        cliente = self.buscar_cliente(cedula_cliente)
        servicio = self.buscar_servicio(id_servicio)

        if not servicio.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio '{servicio.nombre_servicio}' no está disponible en este momento."
            )

        nueva_reserva = Reserva(cliente, servicio, duracion)
        self._reservas.append(nueva_reserva)

        if confirmar_de_inmediato:
            nueva_reserva.confirmar_reserva()

        return nueva_reserva

    def obtener_reservas_por_cliente(self, cedula_cliente):
        # Retorna todas las reservas asociadas a la cédula de un cliente.
        cliente = self.buscar_cliente(cedula_cliente)
        return [res for res in self._reservas if res.cliente.id_entidad == cliente.id_entidad]

    def generar_reporte_general(self):
        # Construye un resumen del estado actual del sistema (clientes, servicios y reservas).
        confirmadas = sum(1 for r in self._reservas if r.estado == "Confirmada")
        canceladas = sum(1 for r in self._reservas if r.estado == "Cancelada")
        pendientes = sum(1 for r in self._reservas if r.estado == "Pendiente")

        ingresos_proyectados = sum(
            r.calcular_total() for r in self._reservas if r.estado == "Confirmada"
        )

        lineas = [
            "--- RESUMEN OPERATIVO SOFTWARE FJ ---",
            f"Clientes registrados : {len(self._clientes)}",
            f"Servicios en catálogo: {len(self._servicios)} ({len(self.listar_servicios_disponibles())} disponibles)",
            f"Reservas totales     : {len(self._reservas)} "
            f"(Confirmadas: {confirmadas} | Pendientes: {pendientes} | Canceladas: {canceladas})",
            f"Ingresos confirmados : ${ingresos_proyectados:,.2f}",
        ]
        return "\n".join(lineas)