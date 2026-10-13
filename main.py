# =====================================================================
# EcoAudit CLI - Módulo Principal
# Autores: Carmen y Cristina
# =====================================================================

while True:
    print("\n=========================================")
    print(" 🌿 ECOAUDIT CLI - MENÚ PRINCIPAL 🌿 ")
    print("=========================================")
    print("1. Realizar nueva auditoría")
    print("2. Consultar histórico")
    print("3. Salir")

    entrada = input("\nSeleccione una opción (1-3): ").strip()

    #Validación robusta de la opción introducida

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

    
    elif opcion == 2:
        print("\n[OPCIÓN 2] Consultando registros históricos...")

    
    elif opcion == 3:
        print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
        break

    
    else:
        print("⚠️ Opción no válida. Elija un número entre 1 y 3.")