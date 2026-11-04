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
- `modelos.py`: Contiene las clases base, herencia, encapsulamiento y polimorfismo del sistema (`Cliente`, `Servicio`, `ReservaSala`, `AlquilerEquipo`, `AsesoriaEspecializada`).
- `excepciones_y_logs.py`: Módulo para el manejo de excepciones personalizadas y el registro de eventos en archivo plano (`logs.txt`).
- `reserva.py`: Módulo para la gestión y procesamiento de reservas de clientes.
- `Fase 4.py`: Script principal de entrada donde se ejecutan las simulaciones del sistema.

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
 - `excepciones_y_logs.py`: Aquí se deben definir las excepciones personalizadas y la función para registrar eventos en `logs.txt`.
 - `reserva.py`: Aquí se debe implementar la clase `Reserva` integrando los clientes y servicios.
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
