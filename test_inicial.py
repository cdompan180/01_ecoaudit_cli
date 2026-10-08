nombre1 = input("Nombre del primer auditor: ").strip()
nombre2 = input("Nombre del segundo auditor: ").strip()
pareja_auditora = [nombre1, nombre2]
nombredispositivo = input("Nombre del dispositivo auditado: ").strip()
potenciaWh = float(input("Introduce la potencia en Wh: ").strip ())
consumo_diariowh = potenciaWh * 24
print(f"Pareja auditora: {pareja_auditora}")
print(f"Dispositivo: {nombredispositivo}")
print(f"Consumo en 24 horas: {consumo_diariowh} Wh")