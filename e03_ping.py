import platform
import subprocess


def hacer_ping(host):
    if platform.system().lower() == "windows":
        comando = ["ping", "-n", "1", "-w", "1000", host]
    else:
        comando = ["ping", "-c", "1", "-W", "1", host]
    try:
        # Ejecutar el comando con subprocess.run ocultando la salida y con un timeout de 5 segundos
        resultado = subprocess.run(
            comando, 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL, 
            timeout=5
        )
        # Devuelve True si el código de retorno es 0 (éxito)
        return resultado.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


host = input("Host o IP a probar: ").strip()
if hacer_ping(host):
    print(host, "responde")
else:
    print(host, "no responde")