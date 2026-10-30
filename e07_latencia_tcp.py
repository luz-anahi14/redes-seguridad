import socket
import time
import statistics

def medir_latencia_tcp(host, puerto=80, intentos=20):
    print(f"\n[+] Midiendo latencia TCP hacia '{host}:{puerto}' ({intentos} intentos)...")
    print("-" * 65)
    
    tiempos = []
    exitos = 0
    
    for i in range(1, intentos + 1):
        # Crear un socket TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)  # Timeout de 2 segundos para la conexión
        
        try:
            # Medir el tiempo de inicio de la conexión con perf_counter (el más preciso)
            inicio = time.perf_counter()
            
            # Intentar conectar al host y puerto
            s.connect((host, puerto))
            
            # Medir el tiempo de fin
            fin = time.perf_counter()
            
            # Calcular la latencia en milisegundos
            latencia_ms = (fin - inicio) * 1000
            tiempos.append(latencia_ms)
            exitos += 1
            
            print(f"Intento {i:2d}: Conectado en {latencia_ms:.2f} ms")
            
        except (socket.timeout, socket.error):
            print(f"Intento {i:2d}: Tiempo de espera agotado / Error de conexión")
            
        finally:
            # Asegurar el cierre del socket en cada iteración
            s.close()
            
        # Pequeña pausa opcional de medio segundo entre intentos para no saturar
        time.sleep(0.5)

    print("-" * 65)
    
    # Mostrar estadísticas si hubo conexiones exitosas
    if tiempos:
        print(f"Resultados para {host}:")
        print(f"  - Intentos exitosos: {exitos}/{intentos}")
        print(f"  - Mínima:   {min(tiempos):.2f} ms")
        print(f"  - Máxima:   {max(tiempos):.2f} ms")
        print(f"  - Promedio: {statistics.mean(tiempos):.2f} ms")
        print(f"  - Mediana:  {statistics.median(tiempos):.2f} ms")
        if len(tiempos) > 1:
            print(f"  - Desviación estándar: {statistics.stdev(tiempos):.2f} ms")
    else:
        print(f"[-] No se pudo establecer conexión exitosa con {host}:{puerto}.")

def main():
    print("=== Ejercicio 7: Latencia TCP con estadísticas ===")
    
    # 1. Medir un servidor local (localhost en un puerto común, ej. 80 u 8080 si tienes algo corriendo)
    # Nota: Asegúrate de tener algún servicio local o cambia el puerto si es necesario.
    medir_latencia_tcp("127.0.0.1", puerto=80, intentos=20)
    
    # 2. Medir un sitio de Internet conocido (ej. puerto 80 u 443 de google.com)
    medir_latencia_tcp("www.google.com", puerto=80, intentos=20)

if __name__ == "__main__":
    main()