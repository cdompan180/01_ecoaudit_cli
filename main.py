# =====================================================================
# EcoAudit CLI - Módulo Principal
# Autores: Carmen y Cristina
# =====================================================================

from calculadora import estimar_consumo_wh, calcular_huella_co2

while True:
    print("\n=========================================")
    print(" 🌿 ECOAUDIT CLI - MENÚ PRINCIPAL 🌿 ")
    print("=========================================")
    print("1. Realizar nueva auditoría")
    print("2. Consultar histórico")
    print("3. Salir")

    entrada = input("\nSeleccione una opción (1-3): ").strip()
    
    try:
        opcion = int(entrada)
    except ValueError:
        print("⚠️ Error: Debe introducir un número entero.")
        continue

    if opcion == 1:
        print("\n[OPCIÓN 1] Iniciando proceso de auditoría...")

        try:
            num_iter = int(input("Introduzca el número de iteraciones: ").strip())
        except ValueError:
            print("⚠️ Error de formato: debe introducir un número entero.")
            continue

        if num_iter <= 0:
            print("⚠️ El valor debe ser mayor que cero.")
        else:
            print(f"✔️ Configurado con éxito para {num_iter} iteraciones.")
            
            print("\n--- AUDITORÍA ENERGÉTICA ---")
            proceso = input("Nombre del equipo: ").strip()
            
            try:
                potencia = float(input("Potencia consumida en Vatios (W): "))
                horas = float(input("Horas de uso diario: "))
            except ValueError:
                print("⚠️ Error de formato: debe introducir valores numéricos válidos.")
                continue

            # SIMULACIÓN ITERATIVA PASO A PASO (PARA INSPECCIÓN EN DEPURADOR)
            print("\nIniciando simulación ciclo a ciclo...")
            consumo_ciclo = estimar_consumo_wh(potencia, horas, 1) # Consumo de un solo ciclo
            consumo_acumulado = 0.0
            ciclo = 1

            while ciclo <= num_iter:
                consumo_acumulado = consumo_acumulado + consumo_ciclo # <--- PONDRÉIS AQUÍ EL PUNTO ROJO
                print(f" [Ciclo {ciclo}] Consumo acumulado parcial: {consumo_acumulado:.2f} Wh")
                ciclo = ciclo + 1

            # Cálculos y guardado en archivo
            consumo = estimar_consumo_wh(potencia, horas, num_iter)
            huella = calcular_huella_co2(consumo)

            print(f"\n✅ Resultados calculados para '{proceso}':")
            print(f"   • Consumo total: {consumo:.2f} Wh")
            print(f"   • Huella de carbono estimada: {huella:.4f}")

            with open("auditorias.csv", mode="a", encoding="utf-8") as archivo:
                archivo.write(f"{proceso},{potencia},{horas},{num_iter},{consumo:.2f},{huella:.4f}\n")

            print("💾 Registro guardado con éxito en 'auditorias.csv'.")

    elif opcion == 2:
        print("\n================ HISTORIAL DE AUDITORÍAS ================")
        try:
            with open("auditorias.csv", mode="r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                print(contenido)
        except FileNotFoundError:
            print("ℹ️ Aún no existen registros. Realiza una auditoría primero.")

    elif opcion == 3:
        print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
        break

    else:
        print("⚠️ Opción no válida. Elija un número entre 1 y 3.")