import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def tabla_verdad(operacion):
    print(f"\nTabla de verdad para: A {operacion} B")
    print("A\tB\tResultado")
    
    for A in [False, True]:
        for B in [False, True]:
            if operacion == "AND":
                resultado = A and B
            elif operacion == "OR":
                resultado = A or B
            elif operacion == "XOR":
                resultado = A != B
            elif operacion == "NAND":
                resultado = not (A and B)
            elif operacion == "NOR":
                resultado = not (A or B)
            elif operacion == "IMPLICA":
                resultado = (not A) or B
            elif operacion == "EQUIVALENCIA":
                resultado = A == B
            else:
                print("⚠️  Operación no válida.")
                return
            print(f"{int(A)}\t{int(B)}\t{int(resultado)}")

# Menú para el usuario
operacion = ""

while operacion != "SALIR":
    limpiar_consola()
    print("═════════════════════════════════════")
    print("      GENERADOR DE TABLA DE VERDAD   ")
    print("═════════════════════════════════════")
    print("Seleccione una operación:")
    print("AND")
    print("OR")
    print("XOR")
    print("NAND")
    print("NOR")
    print("IMPLICA")
    print("EQUIVALENCIA")
    print("SALIR")
    operacion = input("\nElegí una operación lógica: ").strip().upper()
    
    if operacion != "SALIR":
        tabla_verdad(operacion)
        input("\nPresione Enter para continuar...")

