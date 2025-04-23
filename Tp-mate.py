import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def tabla_verdad(operacion):
    limpiar_consola()
    print(f"\nTabla de verdad para: A {nombres_operaciones[operacion]}")
    print("A\tB\tResultado")
    
    for A in [False, True]:
        for B in [False, True]:
            if operacion == "1":
                resultado = A and B
            elif operacion == "2":
                resultado = A or B
            elif operacion == "3":
                resultado = A != B
            elif operacion == "4":
                resultado = not (A and B)
            elif operacion == "5":
                resultado = not (A or B)
            elif operacion == "6":
                resultado = (not A) or B
            elif operacion == "7":
                resultado = A == B
            else:
                print("Operación no válida.")
                return
            print(f"{int(A)}\t{int(B)}\t{int(resultado)}")

# Diccionario para mostrar nombres de operaciones
nombres_operaciones = {
    "1": "AND",
    "2": "OR",
    "3": "XOR",
    "4": "NAND",
    "5": "NOR",
    "6": "IMPLICA",
    "7": "EQUIVALENCIA"
}

operacion = ""  

while operacion != "0":
    print("═════════════════════════════════════")
    print("      GENERADOR DE TABLA DE VERDAD   ")
    print("═════════════════════════════════════")
    print("Operaciones disponibles:")
    for clave, nombre in nombres_operaciones.items():
        print(f"{clave} - {nombre}")
    print("0 - Salir")
    operacion = input("Seleccione una operación: ").strip()

    if operacion in nombres_operaciones:
        tabla_verdad(operacion)
        input("\nPresione Enter para volver al menú...")
        limpiar_consola()
    elif operacion != "0":
        limpiar_consola()
        print("⚠️  Opción no válida. Intente de nuevo.\n")

