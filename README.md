# Fase-4
Prácticas simuladas
------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ

# Descripción del Proyecto
Este proyecto es una solución orientada a objetos desarrollada en Python para la empresa Software FJ. El sistema gestiona clientes, servicios especializados (reservas de salas, alquiler de equipos y asesorías) y reservas sin el uso de bases de datos.

El objetivo principal es implementar de forma rigurosa los principios de POO (abstracción, herencia, polimorfismo y encapsulamiento), junto con un manejo avanzado de excepciones y un sistema de registro de eventos (logging).

------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Estructura del Código 
#NOTA PARA EL EQUIPO: Cada uno debe crear o trabajar sobre su archivo .py correspondiente (módulo) según el rol asignado, para mantener el proyecto organizado.
- `modelos.py`: Contiene las clases base, herencia, encapsulamiento y polimorfismo del sistema (`EntidadBase`, `Cliente`, `Servicio`, `ReservaSala`, `AlquilerEquipo`, `AsesoriaEspecializada`). Responsable: Jhon Alexander Martínez Molina.
- `excepciones.py`: Define las excepciones personalizadas del sistema (`ReservaError` y sus derivadas: `ServicioNoDisponibleError`, `ParametroInvalidoError`, `ClienteInvalidoError`, `OperacionNoPermitidaError`).
- `logs.py`: Función `registrar_log()` que guarda errores y eventos con fecha y hora en el archivo plano `logs.txt`.
- `reserva.py`: Clase `Reserva` con confirmación, cancelación y procesamiento de reservas, con manejo de excepciones.
- `gestor.py`: Clase `SistemaGestion` que administra las listas internas de clientes, servicios y reservas (sin base de datos). *(Pendiente de crear)*
- `Fase 4.py`: Script principal de entrada donde se ejecutan las 10 simulaciones del sistema. Responsable: Jhon Alexander Martínez Molina.
- `logs.txt`: Archivo generado automáticamente al ejecutar el programa, con el registro de errores y eventos.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  Integrantes del Equipo
-(Por favor, agrega tu nombre completo a esta lista a medida que te unas al repositorio)
- Jhon Alexander Martínez Molina
- Jonny Alberto García Arias
-
-
-
------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Orientación sobre la Arquitectura Modular para el Equipo
**IMPORTANTE SOBRE LA INTEGRACIÓN DEL CÓDIGO:**

1. **No fusionaremos el código en un solo archivo.** Mantendremos la estructura modular del proyecto. Cada archivo `.py` cumple una función específica dentro del sistema.

2. **Trabajo en archivos independientes:**
- `modelos.py`: Ya contiene las clases base, entidades, encapsulamiento y polimorfismo (`Cliente`, `Servicio`, etc.).
- `excepciones.py` y `logs.py`: Aquí están las excepciones personalizadas y la función para registrar eventos en `logs.txt`.
- `reserva.py`: Aquí se implementa la clase `Reserva` integrando los clientes y servicios.
- `gestor.py`: Aquí se implementa la clase `SistemaGestion` con las listas internas de clientes, servicios y reservas.
3. **Conexión en el archivo principal (`Fase 4.py`):**
   Este archivo funcionará como el punto de entrada (Main). Desde allí importaremos las clases de los demás módulos (por ejemplo: `from modelos import Cliente, ReservaSala...`) para ejecutar las 10 simulaciones requeridas.

## Tablón de Inquietudes y Dudas del Equipo

*Si tienes alguna pregunta sobre cómo usar las clases de `modelos.py`, cómo estructurar tu módulo o algún inconveniente con Git/GitHub, déjala en esta sección editando este archivo o en los comentarios de los commits.*

###  Preguntas y Notas Actuales:

- **[Alexander]**: Las clases base de `modelos.py` (`Cliente`, `Servicio`, `ReservaSala`, `AlquilerEquipo`, `AsesoriaEspecializada`) ya están disponibles para ser importadas en los demás archivos.
- **[Espacio para tu duda]**: *(Por favor escribir aquí su duda, nombre y fecha si necesitas ayuda con alguna parte del código)*.
------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Información Académica
- Curso: Programación (Código: 213023)
- Grupo: 213023_280
- Universidad: Universidad Nacional Abierta y a Distancia (UNAD)
- Fase: Fase 4 - Componente Práctico (Prácticas Simuladas)
