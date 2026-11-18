# Fase-4
Prácticas simuladas
------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ

# Descripción del Proyecto
Este proyecto es una solución orientada a objetos desarrollada en **Python 3** para la empresa **Software FJ**. El sistema gestiona clientes, servicios especializados (reservas de salas, alquiler de equipos y asesorías) y reservas sin el uso de bases de datos.

El objetivo principal es implementar de forma rigurosa los principios de POO (abstracción, herencia, polimorfismo y encapsulamiento), junto con un manejo avanzado de excepciones y un sistema de registro de eventos (`logging`).

------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Estructura del Código 
El proyecto está organizado de manera modular en 6 archivos `.py` independientes y un archivo de registro generado en tiempo de ejecución:

- `modelos.py`: Contiene las clases base, herencia, encapsulamiento (`@property`) y polimorfismo del sistema (`EntidadBase`, `Cliente`, `Servicio`, `ReservaSala`, `AlquilerEquipo`, `AsesoriaEspecializada`).
- `excepciones.py`: Define las excepciones personalizadas del sistema (`ReservaError` y sus derivadas: `ServicioNoDisponibleError`, `ParametroInvalidoError`, `ClienteInvalidoError`, `OperacionNoPermitidaError`).
- `logs.py`: Función `registrar_log()` que guarda errores y eventos con fecha y hora en el archivo plano `logs.txt`.
- `reserva.py`: Clase `Reserva` con atributos encapsulados, validación estricta de tipos y métodos de confirmación y cancelación bajo bloques `try / except / else / finally`.
- `gestor.py`: Clase `GestorSistema` que administra las colecciones internas de clientes, servicios y reservas en memoria, controla duplicados y emite el reporte operativo consolidado.
- `Fase 4.py`: Script principal de entrada donde se ejecutan de forma secuencial y automática las **11 simulaciones** del sistema (operaciones exitosas y fallos controlados).
- `logs.txt`: Archivo plano generado automáticamente al ejecutar el programa, con el historial de errores y eventos registrados.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  Integrantes del Equipo

- Jhon Alexander Martínez Molina (modelos.py, encapsulamiento en reserva.py, gestor.py e integración de simulaciones en Fase 4.py).
- Jonny Alberto García Arias (excepciones.py, logs.py, base de reserva.py, simulaciones iniciales y documento técnico de entrega).
  
------------------------------------------------------------------------------------------------------------------------------------------------------------------


## Ejecución del Proyecto

1. Clonar o descargar el repositorio:
   ```bash
   git clone [https://github.com/jamartinezm1/Fase-4.git](https://github.com/jamartinezm1/Fase-4.git)
   cd Fase-4
   
------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Información Académica
- Curso: Programación (Código: 213023)
- Grupo: 213023_280
- Universidad: Universidad Nacional Abierta y a Distancia (UNAD)
- Fase: Fase 4 - Componente Práctico (Prácticas Simuladas)
