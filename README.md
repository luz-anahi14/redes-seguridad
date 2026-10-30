# redes-seguridad
#  Prácticas de Redes y Seguridad Informática
##  Requisitos del sistema
* Python 3.x instalado (versión 3.8 o superior).
* Sistema operativo Windows o Linux.
* Biblioteca estándar de Python.
* Conexión a Internet para las prácticas que requieren comunicación de red.
* No requiere instalar paquetes externos mediante `pip`.
## Índice de programas y descripciones

| Archivo                    | Operación / Categoría         | Descripción                                                                                    |
| -------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------- |
| `e01_mi_equipo.py`         | Información del equipo        | Permite consultar información básica del equipo y sus datos de red.                            |
| `e02_subred.py`            | Direccionamiento IP           | Permite trabajar con direcciones IP y analizar información relacionada con las subredes.       |
| `e03_ping.py`              | Conectividad de red           | Comprueba la conectividad entre equipos mediante el envío de solicitudes Ping.                 |
| `e04_barrido.py`           | Exploración de red            | Permite realizar un barrido de direcciones IP para identificar equipos disponibles en una red. |
| `e05_puertos.py`           | Servicios en escucha (Capa 4) | Utiliza sockets TCP para identificar puertos abiertos y servicios disponibles en un equipo.    |
| `e06_dns.py`               | Servicio DNS (Capa 7)         | Permite resolver nombres de dominio y obtener información de las direcciones IP asociadas.     |
| `e07_latencia_tcp.py`      | Medición de rendimiento       | Mide los tiempos de respuesta de conexiones TCP y calcula estadísticas de latencia.            |
| `e08_https_certificado.py` | Seguridad HTTPS (TLS)         | Verifica conexiones HTTPS y obtiene información sobre los certificados SSL/TLS.                |

## Descripción detallada de los scripts
### 1. Información del equipo (`e01_mi_equipo.py`)
Permite consultar información básica del equipo, como datos relacionados con su configuración de red y su identificación dentro de la red.
### 2. Análisis de subred (`e02_subred.py`)
Trabaja con direcciones IP y conceptos de direccionamiento de red, permitiendo analizar información relacionada con las subredes.
### 3. Comprobación de conectividad (`e03_ping.py`)
Permite comprobar si existe comunicación entre equipos mediante el comando Ping, verificando la disponibilidad de un dispositivo en la red.
### 4. Barrido de red (`e04_barrido.py`)
Realiza un recorrido por un conjunto de direcciones IP para identificar qué equipos se encuentran disponibles dentro de una red.
### 5. Escáner de puertos TCP (`e05_puertos.py`)
Utiliza sockets TCP para comprobar la disponibilidad de determinados puertos e identificar posibles servicios activos en un equipo.
### 6. Resolución DNS (`e06_dns.py`)
Permite consultar nombres de dominio y obtener las direcciones IP asociadas mediante el servicio DNS.
### 7. Medición de latencia TCP (`e07_latencia_tcp.py`)
Realiza mediciones del tiempo de respuesta de conexiones TCP y utiliza estadísticas para calcular valores como promedio y mediana.
### 8. Verificación de certificados HTTPS (`e08_https_certificado.py`)
Permite verificar conexiones HTTPS, consultar información de certificados SSL/TLS y comprobar su período de validez.
##  Instrucciones de uso
Clonar el repositorio:git clone https://github.com/luz-anahi14/redes-seguridad.git
Ingresar a la carpeta:cd redes-seguridad
Ejecutar un programa:python e01_mi_equipo.py
Para ejecutar los demás programas, reemplazar el nombre del archivo por el script correspondiente.
##  Autora
Luz Anahí Gamarra
