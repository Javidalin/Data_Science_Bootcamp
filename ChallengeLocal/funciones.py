# funciones.py

import random
from clases import Tablero


def imprimir_tableros(jugador, maquina):
    print("\nTu tablero:")
    jugador.mostrar_tablero()
    print("\nTablero de la máquina:")
    maquina.mostrar_tablero(oculto=True)


def obtener_disparo():
    while True:
        try:
            fila = int(input("Elige la fila (0-9): "))
            columna = int(input("Elige la columna (0-9): "))
            if not (0 <= fila <= 9) or not (0 <= columna <= 9):
                print("Coordenadas fuera de rango. Intenta de nuevo.")
                continue
            return fila, columna
        except ValueError:
            print("Por favor, ingresa coordenadas válidas.")


def disparo_maquina(jugador):
    fila, columna = random.randint(0, 9), random.randint(0, 9)
    print(f"La máquina dispara a la posición ({fila}, {columna})...")
    acierto = jugador.recibir_disparo(fila, columna)
    print("¡La máquina acertó!" if acierto else "La máquina falló.")
    return acierto


def configurar_tablero_jugador(nombre_jugador):
    jugador = Tablero(nombre_jugador)
    while True:
        print("\nGenerando tu tablero...")
        jugador.limpiar_tablero()  # Limpia el tablero y coloca los barcos
        jugador.mostrar_tablero()
        opcion = input(
            "\n¿Te gusta este tablero? (s/n): "
        ).strip().lower()
        if opcion == "s":
            return jugador
        elif opcion == "n":
            print("\nRegenerando tablero...")
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")


def jugar():
    print("------------------------------------------------------------------------")
    print("     ╔╗╔╗╔╗╔╗╔╗ ╔╗╔══╗ ╔══╗╔═══╗  ╔╗  ╔══╗  ╔══╗╔╗  ╔══╗╔════╗╔══╗")
    print("     ║║║║║║║║║╚═╝║║╔╗╚╗╚╗╔╝║╔═╗║  ║║  ║╔╗║  ║╔═╝║║  ║╔╗║╚═╗╔═╝║╔╗║")
    print("     ║╚╝║║║║║║╔╗ ║║║╚╗║ ║║ ║╚═╝║  ║║  ║╚╝║  ║╚═╗║║  ║║║║  ║║  ║╚╝║")
    print("     ║╔╗║║║║║║║╚╗║║║ ║║ ║║ ║╔╗╔╝  ║║  ║╔╗║  ║╔═╝║║  ║║║║  ║║  ║╔╗║")
    print("     ║║║║║╚╝║║║ ║║║╚═╝║╔╝╚╗║║║║   ║╚═╗║║║║  ║║  ║╚═╗║╚╝║  ║║  ║║║║")
    print("     ╚╝╚╝╚══╝╚╝ ╚╝╚═══╝╚══╝╚╝╚╝   ╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝  ╚╝  ╚╝╚╝")
    print("")
    print("╔════╗╔═══╗╔══╗╔╗  ╔╗  ╔═══╗╔══╗╔╗  ╔══╗ ╔═══╗╔╗ ╔╗   ╔╗╔╗╔══╗╔╗ ╔╗╔══╗ ")
    print("╚═╗╔═╝║╔══╝║╔╗║║║  ║║  ║╔══╝║╔╗║║║  ║╔╗╚╗║╔══╝║╚═╝║   ║║║║╚╗╔╝║╚═╝║║╔╗╚╗")
    print("  ║║  ║╚══╗║╚╝║║╚╗╔╝║  ║║╔═╗║║║║║║  ║║╚╗║║╚══╗║╔╗ ║   ║╚╝║ ║║ ║╔╗ ║║║╚╗║")
    print("  ║║  ║╔══╝║╔╗║║╔╗╔╗║  ║║╚╗║║║║║║║  ║║ ║║║╔══╝║║╚╗║   ║╔╗║ ║║ ║║╚╗║║║ ║║")
    print("  ║║  ║╚══╗║║║║║║╚╝║║  ║╚═╝║║╚╝║║╚═╗║╚═╝║║╚══╗║║ ║║   ║║║║╔╝╚╗║║ ║║║╚═╝║")
    print("  ╚╝  ╚═══╝╚╝╚╝╚╝  ╚╝  ╚═══╝╚══╝╚══╝╚═══╝╚═══╝╚╝ ╚╝   ╚╝╚╝╚══╝╚╝ ╚╝╚═══╝")
    print("")
    print("------------------------------------------------------------------------")
    print("                ¡¡Bienvedid@s a Hundir la Flota!!")
    print("            ¿Echamos una partidita? Sigue las instrucciones")
    print("------------------------------------------------------------------------")
    print("")
    print("")
    nombre_jugador = input("Antes de comenzar ¿Cómo te llamas, capitán? ")
    jugador = configurar_tablero_jugador(nombre_jugador)
    maquina = Tablero("Máquina")

    print("\nGenerando el tablero de la máquina...")
    maquina.colocar_barcos()

    while True:
        imprimir_tableros(jugador, maquina)

        print(f"\nEs tu turno, {jugador.nombre}.")
        fila, columna = obtener_disparo()
        acierto = maquina.recibir_disparo(fila, columna)
        print("¡Acertaste!" if acierto else "Fallaste.")
        if maquina.vidas == 0:
            print(f"\n¡{jugador.nombre} ha ganado!")
            break

        input("\nPulsa Enter para continuar...")

        print("\nTurno de la máquina.")
        disparo_maquina(jugador)
        if jugador.vidas == 0:
            print("\n¡La máquina ha ganado!")
            break

        input("\nPulsa Enter para continuar...")
