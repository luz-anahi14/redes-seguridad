import socket
import ssl
from datetime import datetime

def revisar_certificado(hostname, puerto=443):
    print(f"\n[+] Analizando certificado para: {hostname}")
    print("-" * 55)
    
    # Crear un contexto SSL por defecto
    contexto = ssl.create_default_context()
    
    try:
        # Crear socket y envolverlo en SSL
        s = socket.create_connection((hostname, puerto), timeout=5)
        s_ssl = contexto.wrap_socket(s, server_hostname=hostname)
        
        # getpeercert() devuelve un diccionario con los detalles del certificado
        cert = s_ssl.getpeercert()
        s_ssl.close()
        
        # Extraer el campo notAfter (fecha de vencimiento)
        not_after_str = cert.get('notAfter')
        
        # Formato típico que devuelve Python: 'Mar 15 12:00:00 2027 GMT'
        fecha_expiracion = datetime.strptime(not_after_str, '%b %d %H:%M:%S %Y %Z')
        
        # Calcular los días restantes
        dias_restantes = (fecha_expiracion - datetime.utcnow()).days
        
        print(f"Expira el: {fecha_expiracion}")
        print(f"Días restantes para el vencimiento: {dias_restantes} días")
        
        return {
            "hostname": hostname,
            "dias": dias_restantes,
            "fecha": fecha_expiracion
        }

    except ssl.SSLError as e:
        print(f"[-] Error de certificado SSL en '{hostname}': {e}")
        print("    (Causa frecuente: certificado vencido, autofirmado o error de confianza).")
        return None
    except Exception as e:
        print(f"[-] Error de conexión en '{hostname}': {e}")
        return None

def main():
    print("=== Ejercicio 8: Estado HTTPS y vencimiento del certificado ===")
    
    # 1. Revisar tres sitios válidos y ordenar los resultados de menor a mayor días
    sitios = ["www.google.com", "www.github.com", "www.wikipedia.org"]
    resultados = []
    
    for sitio in sitios:
        res = revisar_certificado(sitio)
        if res:
            resultados.append(res)
            
    if resultados:
        # Ordenar de menor a mayor cantidad de días restantes
        resultados_ordenados = sorted(resultados, key=lambda x: x["dias"])
        print("\n" + "=" * 55)
        print("SITIOS ORDENADOS DE MENOR A MAYOR CANTIDAD DE DÍAS:")
        print("=" * 55)
        for idx, item in enumerate(resultados_ordenados, 1):
            print(f"{idx}. {item['hostname']} -> {item['dias']} días (Vence: {item['fecha'].strftime('%Y-%m-%d')})")

    # 2. Probar con un dominio sin HTTPS válido (ej. certificado vencido)
    print("\n" + "=" * 55)
    print("PRUEBA CON DOMINIO SIN HTTPS VÁLIDO (Ej: expired.badssl.com):")
    print("=" * 55)
    revisar_certificado("expired.badssl.com")

if __name__ == "__main__":
    main()