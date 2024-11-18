# clases.py

import random

class Tablero:
    VACIO = " "
    BARCO = "O"
    IMPACTO = "X"
    AGUA = "-"

    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero = [[self.VACIO for _ in range(10)] for _ in range(10)]  # Tablero vacío
        self.coordenadas_barcos = []  # Para almacenar las coordenadas de los barcos
        self.vidas = 0  # Para contar cuántos barcos (vidas) quedan

    def limpiar_tablero(self):
        """Reinicia el tablero, eliminando los barcos y dejando todo vacío."""
        self.tablero = [[self.VACIO for _ in range(10)] for _ in range(10)]  # Vuelve a estar vacío
        self.coordenadas_barcos = []  # Vacía las coordenadas de los barcos
        self.vidas = 0  # Restablece el contador de vidas
        self.colocar_barcos()  # Vuelve a colocar los barcos de forma automática

    def colocar_barcos(self):
        """Coloca los barcos en el tablero de manera aleatoria."""
        barcos = {1: 4, 2: 3, 3: 2, 4: 1}  # Eslora de los barcos: 4 barcos de 1, 3 de 2, 2 de 3, 1 de 4
        for eslora, cantidad in barcos.items():
            for _ in range(cantidad):
                self._colocar_barco_aleatorio(eslora)

    def _colocar_barco_aleatorio(self, eslora):
        """Coloca un barco de una eslora determinada en el tablero aleatoriamente."""
        colocado = False
        while not colocado:
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            orientacion = random.choice(["horizontal", "vertical"])

            if self._puede_colocar_barco(fila, columna, eslora, orientacion):
                for i in range(eslora):
                    if orientacion == "horizontal":
                        self.tablero[fila][columna + i] = self.BARCO
                        self.coordenadas_barcos.append((fila, columna + i))
                    else:
                        self.tablero[fila + i][columna] = self.BARCO
                        self.coordenadas_barcos.append((fila + i, columna))
                colocado = True

    def _puede_colocar_barco(self, fila, columna, eslora, orientacion):
        """Verifica si el barco puede ser colocado sin salir del tablero o superponerse con otro barco."""
        if orientacion == "horizontal" and columna + eslora <= 10:
            return all(self.tablero[fila][columna + i] == self.VACIO for i in range(eslora))
        elif orientacion == "vertical" and fila + eslora <= 10:
            return all(self.tablero[fila + i][columna] == self.VACIO for i in range(eslora))
        return False

    def recibir_disparo(self, fila, columna):
        """Recibe un disparo y marca el impacto si hay barco."""
        if (fila, columna) in self.coordenadas_barcos:
            self.tablero[fila][columna] = self.IMPACTO
            self.coordenadas_barcos.remove((fila, columna))
            self.vidas -= 1
            return True
        else:
            self.tablero[fila][columna] = self.AGUA
            return False

    def mostrar_tablero(self, oculto=False):
        """Muestra el tablero. Si 'oculto' es True, oculta los barcos del oponente."""
        # Imprimir encabezado de columnas
        print("    ", end="")
        for i in range(10):
            print(f"[{i}]", end=" ")  # Índices de columna con corchetes
        print()

        # Imprimir filas con sus índices
        for i, fila in enumerate(self.tablero):
            print(f"[{i}]", end=" ")  # Índices de fila con corchetes
            for columna in fila:
                print(f"[{columna}]", end=" ")  # Imprime el contenido del tablero con corchetes
            print()  # Salto de línea después de cada fila
