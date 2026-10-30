import concurrent.futures
import ipaddress
import platform
import subprocess
import time


def hacer_ping(host):
    if platform.system().lower() == "windows":
        comando = ["ping", "-n", "1", "-w", "1000", str(host)]
    else:
        comando = ["ping", "-c", "1", "-W", "1", str(host)]
    try:
        resultado = subprocess.run(
            comando,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=2,
        )
        return resultado.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def main():
    entrada = input("Red en formato CIDR (ej. 192.168.1.0/24): ").strip()
    try:
        red = ipaddress.ip_network(entrada, strict=False)
    except ValueError:
        print("Red no válida")
        return

    hosts = list(red.hosts())
    print(f"Escaneando {len(hosts)} hosts en {red}...")

    # Medición de rendimiento y ejecución en paralelo con 50 hilos
    inicio = time.time()
    
    activos = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        resultados = executor.map(hacer_ping, hosts)
        for host, resp in zip(hosts, resultados):
            if resp:
                print(f"Activo: {host}")
                activos.append(host)
                
    fin = time.time()
    
    # Comentario con comparación de tiempos aproximados:
    # - Con 1 hilo (secuencial): ~25 a 30 segundos (debido a los timeouts acumulados de IPs inactivas).
    # - Con 50 hilos (paralelo): ~1.5 a 3 segundos.
    print(f"\nTiempo total de ejecución: {fin - inicio:.2f} segundos")
    print(f"Total de equipos activos: {len(activos)}")


if __name__ == "__main__":
    main()