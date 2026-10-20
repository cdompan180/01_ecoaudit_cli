# =====================================================================
# EcoAudit CLI - Módulo Principal
# Autores: Carmen y Cristina
# =====================================================================

from calculadora import estimar_consumo_wh, calcular_huella_co2


def solicitar_numero_positivo(mensaje: str, tipo=float):
    """Solicita un número positivo y controla los errores de entrada."""
    while True:
        try:
            valor = tipo(input(mensaje))

            if valor <= 0:
                print("Error: introduce un número mayor que cero.")
                continue

            return valor

        except ValueError:
            print("Error: introduce un número válido.")


def main():
    """Muestra el menú principal y ejecuta las opciones."""
    while True:
        print("\n========== ECOAUDIT CLI ==========")
        print("1. Realizar auditoría energética")
        print("2. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            print("\n--- AUDITORÍA ENERGÉTICA ---")

            proceso = input("Nombre del equipo/proceso: ").strip()

            if not proceso:
                print("Error: el nombre no puede estar vacío.")
                continue

            potencia = solicitar_numero_positivo("Potencia consumida en Vatios (W): ")

            horas = solicitar_numero_positivo("Horas de uso diario: ")

            iteraciones = solicitar_numero_positivo("Número de iteraciones del proceso: ",int)

            
            consumo = estimar_consumo_wh(potencia,horas,iteraciones)

            
            huella = calcular_huella_co2(consumo)

            print(f"\nResultados calculados para '{proceso}':")
            print(f"   • Consumo total: {consumo:.2f} Wh")
            print(f"   • Huella de carbono estimada: "f"{huella:.4f} g CO2")

        elif opcion == "2":
            print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Selecciona 1 o 2.")


if __name__ == "__main__":
    main()



"""
======================================================================
REGISTRO DE INTERACCIÓN CON IA (PROMPT LOG)
======================================================================
Herramienta consultada : [ChatGPT / Claude / Copilot en VS Code]
Fecha y hora : 20/10/2026 - 11:07

1. Consulta exacta planteada (Prompt o instrucción):
"¿Porque nos da error la variable calcular_huella_co2? ¿Como podemmos solucionarlo?"

2. Síntesis de la respuesta recibida:
"La IA explicó que nos falta añadir la función calcular_huella_co2, que es la que provoca el error de importación."

3. Aplicación crítica y modificaciones realizadas:
"No copiamos el bloque propuesto de forma literal; creamos la función calcular_huella_co2 en el archivo calculadora.py, 
siguiendo la estructura de las funciones ya existentes."

======================================================================
"""