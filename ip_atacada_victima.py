registros = {
    "reg1":{
    "ip":"192.168.2.1",
    "puerto":80,
    "usuario":"us_9080",
    "estado":"Acceso exitoso"
    },
    "reg2":{
        "ip":"192.168.12.1",
        "puerto":40,
        "usuraio":"us_9080",
        "estado":"Acceso exitoso"
    },
    "reg3": {
        "ip": "192.168.2.13",
        "puerto": 40,
        "usuraio": "us_9080",
        "estado": "Acceso fallido"
    },
    "reg4": {
        "ip": "192.168.2.1",
        "puerto": 20,
        "usuraio": "us_9080",
        "estado": "Acceso fallido"
    },
    "reg5": {
        "ip": "192.168.2.1",
        "puerto": 40,
        "usuraio": "us_9080",
        "estado": "Acceso fallido"
    },
    "reg6": {
        "ip": "192.168.2.1",
        "puerto": 40,
        "usuraio": "us_9080",
        "estado": "Acceso fallido"
    },
    "reg7": {
        "ip": "192.168.2.1",
        "puerto": 40,
        "usuraio": "us_9080",
        "estado": "Acceso fallido"
    }

}
ips_victimas={}
cuenta_victimas=0
ips_atacadas={}
cuenta_atacado=0

for registro in registros.values():
    ip = registro.get('ip')
    estado = registro.get('estado')
    if estado == "Acceso exitoso":
        if ip in ips_victimas:
            ips_victimas[ip] += 1
        else:
            ips_victimas[ip] = 0

    elif estado== "Acceso fallido":
        if ip in ips_atacadas:
            ips_atacadas[ip] += 1
        else:
            ips_atacadas[ip]= 0

for ip, intentos in ips_atacadas.items():
    if intentos > 2:
        print(f"La ip {ip} sufrió {intentos} intentos de ataque ")
    elif intentos <=0:
        print(f"La ip {ip} fue vulnerada")

for ip, intentos in ips_victimas.items():
    print(f"La ip {ip} fue vulnerada")

