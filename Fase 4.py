"""
Programa principal - Sistema Integral de Gestión de Clientes, Servicios y Reservas
Empresa: Software FJ
 
Este archivo es el punto de entrada: importa las clases de los demás módulos
(modelos, excepciones, logs y reserva) y ejecuta 10 simulaciones completas.
Cada simulación puede fallar sin detener el programa: los errores se capturan,
se registran en 'logs.txt' y la ejecución continúa con la siguiente.
 

"""

from excepciones import (
    ReservaError,
    ParametroInvalidoError,
    ClienteInvalidoError,
)
from logs import registrar_log
from modelos import Cliente, ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
 
 

# FUNCIONES DE APOYO

def reportar_error(contexto, error):
    """Muestra un error controlado en pantalla y lo guarda en el archivo de logs."""
    registrar_log(f"{contexto}: {error}")
    print(f"[-] Error controlado ({contexto}): {error}")
 
 
def crear_cliente_demo():
    """Cliente válido que reutilizan varias simulaciones."""
    return Cliente("1234567", "Ana Pérez", "ana@mail.com", "3001234567")
 
 

# SIMULACIONES 1 a 5: CLIENTES Y SERVICIOS

def simulacion_1():
    """Registro de un cliente válido"""
    cliente = crear_cliente_demo()
    print("[+] Cliente registrado correctamente:")
    print("   ", cliente.obtener_informacion())
 
 
def simulacion_2():
    """Registro de un cliente con correo inválido"""
    # Lanza ClienteInvalidoError: lo captura main() y lo registra en el log
    Cliente("7654321", "Carlos Ruiz", "carlos-sin-arroba", "3109876543")
 
 
def simulacion_3():
    """Registro de clientes con cédula y teléfono inválidos"""
    try:
        Cliente("ABC123", "Laura Gómez", "laura@mail.com", "3201112233")
    except ClienteInvalidoError as error:
        reportar_error("Cédula inválida", error)
 
    # Este segundo error no se captura aquí: lo maneja main() y el programa sigue
    Cliente("9988776", "Pedro Díaz", "pedro@mail.com", "12")
 
 
def simulacion_4():
    """Creación de los tres servicios y cálculo polimórfico de costos"""
    servicios = [
        ReservaSala("S-01", "Sala Innovación", 50000, 10),
        AlquilerEquipo("E-01", "Portátil Gamer", 10000, 200000),
        AsesoriaEspecializada("A-01", "Arquitectura de Software", 100000, "Backend"),
    ]
    horas = 3
    print(f"[+] Costo de cada servicio por {horas} horas (mismo método, distinto resultado):")
    for servicio in servicios:
        print(f"    {servicio.obtener_descripcion()} -> ${servicio.calcular_costo(horas):,.2f}")
 
    # Sobrecarga: parámetros opcionales de descuento e impuesto
    sala = servicios[0]
    print(f"    Sala con 10% de descuento: ${sala.calcular_costo(horas, 10):,.2f}")
    print(f"    Sala con 10% de descuento y 19% de impuesto: ${sala.calcular_costo(horas, 10, 19):,.2f}")
    print(f"    Sala con 19% de impuesto (variante): ${sala.calcular_costo_con_impuesto(horas, 19):,.2f}")
 
 
def simulacion_5():
    """Servicio inválido y cálculo inconsistente (con encadenamiento de excepciones)"""
    try:
        ReservaSala("S-02", "Sala Fantasma", -50000, 5)
    except ParametroInvalidoError as error:
        reportar_error("Servicio inválido", error)
 
    sala = ReservaSala("S-03", "Sala Ejecutiva", 80000, 6)
    try:
        sala.calcular_costo(2, 150)  # Un descuento de 150% es inconsistente
    except ParametroInvalidoError as error:
        # Encadenamiento: se lanza una excepción nueva conservando la causa original
        raise ReservaError("No se pudo calcular el costo del servicio") from error
 
 

# SIMULACIONES 6 a 10: RESERVAS

def simulacion_6():
    """Reserva exitosa"""
    cliente = crear_cliente_demo()
    sala = ReservaSala("S-01", "Sala Innovación", 50000, 10)
    reserva = Reserva(cliente, sala, 2)
    reserva.confirmar_reserva()
    print(f"    Estado: {reserva.estado} | Costo: ${sala.calcular_costo(2):,.2f}")
 
 
def simulacion_7():
    """Reserva fallida: duración igual a 0"""
    cliente = crear_cliente_demo()
    equipo = AlquilerEquipo("E-01", "Portátil Gamer", 10000, 200000)
    reserva = Reserva(cliente, equipo, 0)
    reserva.confirmar_reserva()
    print(f"    Estado: {reserva.estado}")
 
 
def simulacion_8():
    """Reserva fallida: servicio no disponible"""
    cliente = crear_cliente_demo()
    asesoria = AsesoriaEspecializada("A-01", "Arquitectura de Software", 100000, "Backend")
    asesoria.disponible = False
    reserva = Reserva(cliente, asesoria, 1)
    reserva.confirmar_reserva()
    print(f"    Estado: {reserva.estado}")
 
 
def simulacion_9():
    """Cancelación de una reserva y segundo intento de cancelarla"""
    cliente = crear_cliente_demo()
    sala = ReservaSala("S-01", "Sala Innovación", 50000, 10)
    reserva = Reserva(cliente, sala, 3)
    reserva.confirmar_reserva()
    reserva.cancelar_reserva()
    reserva.cancelar_reserva()  # Segundo intento: operación no permitida
    print(f"    Estado final: {reserva.estado}")
 
 
def simulacion_10():
    """Intento de confirmar una reserva que ya fue cancelada"""
    cliente = crear_cliente_demo()
    equipo = AlquilerEquipo("E-02", "Proyector", 15000, 100000)
    reserva = Reserva(cliente, equipo, 2)
    reserva.cancelar_reserva()
    reserva.confirmar_reserva()  # No debería permitirse
    print(f"    Estado final: {reserva.estado} (debe seguir 'Cancelada')")
 
 

# PROGRAMA PRINCIPAL

def main():
    print("Bienvenidos al curso de Programación")
    print("Universidad Nacional Abierta y a Distancia")
    print("Sistema de Gestión Software FJ - Fase 4\n")
 
    simulaciones = [
        simulacion_1, simulacion_2, simulacion_3, simulacion_4, simulacion_5,
        simulacion_6, simulacion_7, simulacion_8, simulacion_9, simulacion_10,
    ]
 
    for numero, simulacion in enumerate(simulaciones, start=1):
        print(f"=== Simulación {numero}: {simulacion.__doc__} ===")
        try:
            simulacion()
        except ReservaError as error:
            causa = f" | Causa: {error.__cause__}" if error.__cause__ else ""
            registrar_log(f"Simulación {numero}: {error}{causa}")
            print(f"[-] Error controlado: {error}{causa}")
        except Exception as error:
            # Última red de seguridad: ningún error detiene el programa
            registrar_log(f"Simulación {numero}, error inesperado: {error}")
            print(f"[-] Error inesperado: {error}")
        print()
 
    print("Las 10 simulaciones finalizaron. El programa continuó funcionando ante todos los errores.")
    print("Revisa el archivo 'logs.txt' para ver el registro de errores.")
 
 
if __name__ == "__main__":
    main()