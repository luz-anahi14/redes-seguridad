import ipaddress

entrada = input("Red en formato CIDR (ej. 192.168.10.0/26): ")
try:
    red = ipaddress.ip_network(entrada, strict=False)
except ValueError:
    print("Dirección no válida")
    raise SystemExit(1)

print("Red:", red.network_address)
print("Máscara:", red.netmask)
print("Prefijo: /" + str(red.prefixlen))
print("Broadcast:", red.broadcast_address)

# Cálculo de hosts útiles y límites
if red.num_addresses < 4:
    print("Hosts útiles: Sin hosts útiles")
else:
    print(f"Hosts útiles: {red.num_addresses - 2}")
    print(f"Primer host: {red.network_address + 1}")
    print(f"Último host: {red.broadcast_address - 1}")