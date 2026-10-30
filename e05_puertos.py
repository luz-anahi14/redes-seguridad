import socket
from datetime import datetime

# Definir la lista de puertos a escanear (incluyendo los adicionales solicitados)
PUERTOS = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 1433, 3306, 3389, 5432, 8080]

def main():
    # Solicitar el objetivo (IP o hostname)
    objetivo = input("Ingrese la IP o host a escanear: ").strip()
    
    if not objetivo:
        objetivo = "localhost"

    print("-" * 60)
    print(f"Escaneando el objetivo: {objetivo}...")
    print(f"Hora de inicio: {datetime.now()}")
    print("-" * 60)

    try:
        # Resolver el nombre del host a dirección IP
        ip_objetivo = socket.gethostbyname(objetivo)
        print(f"IP resuelta: {ip_objetivo}\n")

        abiertos = 0

        for puerto in PUERTOS:
            # Crear un socket TCP/IP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Establecer un tiempo de espera (timeout) corto
            s.settimeout(0.8)
            
            # connect_ex devuelve 0 si la conexión se establece (puerto abierto)
            resultado = s.connect_ex((ip_objetivo, puerto))
            
            if resultado == 0:
                print(f"[+] Puerto {puerto}: ABIERTO")
                abiertos += 1
            
            # Cerrar el socket en cada iteración
            s.close()

        print("-" * 60)
        print(f"Escaneo finalizado. Puertos abiertos encontrados: {abiertos}")
        print("-" * 60)

    except KeyboardInterrupt:
        print("\n[!] Escaneo cancelado por el usuario.")
    except socket.gaierror:
        print("\n[-] Error: No se pudo resolver el nombre del host.")
    except socket.error:
        print("\n[-] Error: No se pudo conectar al servidor.")

if __name__ == "__main__":
    main()