from datetime import datetime

def registrar_log(mensaje_error):
    """Esta función recibe un mensaje de error, le agrega la fecha y hora actual y lo guarda en el archivo 'logs.txt'."""
    
    # Obtención de la fecha y hora del momento en que ocurre el error
    tiempo_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Para crear o abrir el archivo 'logs.txt' (si no existe, Python lo crea solo)
    with open("logs.txt", "a", encoding="utf-8") as archivo_log:
        archivo_log.write(f"[{tiempo_actual}] ERROR: {mensaje_error}\n")