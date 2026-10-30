import socket
import time

def resolver_dominio(dominio):
    print(f"\nResolviendo: {dominio}")
    print("-" * 50)
    
    # Medir el tiempo de inicio de la consulta
    inicio = time.perf_counter()
    
    try:
        # gethostbyname_ex devuelve una tupla de tres elementos:
        # (nombre_host, lista_aliases, lista_ips)
        resultado = socket.gethostbyname_ex(dominio)
        
        # Medir el tiempo de fin
        fin = time.perf_counter()
        tiempo_transcurrido = (fin - inicio) * 1000  # Convertir a milisegundos
        
        print(f"[+] Nombre oficial: {resultado[0]}")
        print(f"[+] Aliases: {resultado[1]}")
        print(f"[+] Direcciones IP: {resultado[2]}")
        print(f" Tiempo de resolución: {tiempo_transcurrido:.4f} ms")
        
    except socket.gaierror:
        fin = time.perf_counter()
        tiempo_transcurrido = (fin - inicio) * 1000
        print(f"[-] Error: No se pudo resolver el nombre (dominio inexistente o sin conexión).")
        print(f"  Tiempo transcurrido: {tiempo_transcurrido:.4f} ms")

def main():
    print("=== Ejercicio 6: Resolución de nombres y tiempo (DNS) ===")
    
    # 1. Resolver un sitio conocido
    resolver_dominio("www.google.com")
    
    # 2. Resolver localhost
    resolver_dominio("localhost")
    
    # 3. Resolver un nombre inexistente para probar el manejo de errores
    resolver_dominio("este.dominio.no.existe.abc123xyz.com")
    
    print("\n" + "=" * 50)
    print("PRUEBA DE CACHÉ (Ejecutar el mismo dominio dos veces seguidas):")
    print("=" * 50)
    
    dominio_prueba = "www.github.com"
    print(f"\n1ª Consulta para '{dominio_prueba}':")
    resolver_dominio(dominio_prueba)
    
    print(f"\n2ª Consulta para '{dominio_prueba}' (Debería ser más rápida por la caché):")
    resolver_dominio(dominio_prueba)

if __name__ == "__main__":
    main()