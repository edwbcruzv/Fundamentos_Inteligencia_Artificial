from MiBusqueda.NoInformada import *
import numpy as np
if __name__ == '__main__':
    # Acciones
    U = Accion('U')  # Arriba
    D = Accion('D')  # Abajo
    L = Accion('L')  # Izquierda
    R = Accion('R')  # Derecha

    # Estados
    estados_lista = []
    # estados_labels = [
    #     (1, 9),
    #     (1, 14),
    #     (2, 4),
    #     (2, 5),
    #     (2, 9),
    #     (2, 11),
    #     (2, 14),
    #     (2, 15),
    #     (3, 2),
    #     (3, 11),
    #     (4, 3),
    #     (4, 4),
    #     (4, 6),
    #     (4, 13),
    #     (5, 9),
    #     (5, 13),
    #     (7, 4),
    #     (7, 7),
    #     (7, 9),
    #     (7, 12),
    #     (7, 15),
    #     (8, 11),
    #     (9, 4),
    #     (9, 8),
    #     (10, 1),
    #     (10, 10),
    #     (10, 12),
    #     (12, 2),
    #     (12, 14),
    #     (13, 4),
    #     (13, 6),
    #     (13, 8),
    #     (13, 10),
    #     (13, 14),
    #     (14, 14),
    #     (15, 2),
    #     (15, 4),
    #     (15, 8),
    #     (15, 12)
    # ]
    # for i, j in estados_labels:
    #     label = "C_{0}{1}=Estado('C_{0}{1}',[])".format(i, chr(64+j))
    #     print(label)

    
    
    C_1I = Estado('C_1I', [D])
    C_1N = Estado('C_1N', [D])
    C_2D = Estado('C_2D', [L, R, D])
    C_2E = Estado('C_2E', [R])
    C_2I = Estado('C_2I', [L, R, U, D])
    C_2K = Estado('C_2K', [L, R, D])
    C_2N = Estado('C_2N', [L, R, U])
    C_2O = Estado('C_2O', [L])
    C_3B = Estado('C_3B', [U])
    C_3K = Estado('C_3K', [U])
    C_4C = Estado('C_4C', [R])
    C_4D = Estado('C_4D', [L, R, U, D])
    C_4F = Estado('C_4F', [L, R, D])
    C_4M = Estado('C_4M', [D])
    C_5F = Estado('C_5F', [U])
    C_5I = Estado('C_5I', [R, U, D])
    C_5M = Estado('C_5M', [L, R, U])
    C_7D = Estado('C_7D', [L, R, U, D])
    C_7G = Estado('C_7G', [L])
    C_7I = Estado('C_7I', [U])
    C_7L = Estado('C_7L', [D])
    C_7N = Estado('C_7N', [R, U, D])
    C_7O = Estado('C_7O', [L])
    C_8K = Estado('C_8K', [R])
    C_8L = Estado('C_8L', [L, U, D])
    C_9D = Estado('C_9D', [R, U, D])
    C_9H = Estado('C_9H', [L, R, D])
    C_10A = Estado('C_10A', [R])
    C_10J = Estado('C_10J', [U])
    C_10L = Estado('C_10L', [R, U, D])
    C_11F = Estado('C_11F', [D])
    C_12B = Estado('C_12B', [D])
    C_12L = Estado('C_12L', [L, U, D])
    C_12N = Estado('C_12N', [D])
    C_13B = Estado('C_13B', [R, U, D])
    C_13D = Estado('C_13D', [L, U, D])
    C_13F = Estado('C_13F', [R, U, D])
    C_13H = Estado('C_13H', [L, U, D])
    C_13J = Estado('C_13J', [U])
    C_13L = Estado('C_13L', [R, U, D])
    C_13N = Estado('C_13N', [L, U, D])
    C_14F = Estado('C_14F', [U])
    C_14N = Estado('C_14N', [U])
    C_15B = Estado('C_15B', [U])
    C_15D = Estado('C_15D', [U])
    C_15H = Estado('C_15H', [U])
    C_15L = Estado('C_15L', [U])

    Espacio_Estados = {
        C_1I: {D: C_2I},
        C_1N: {D: C_2N},
        C_2D: {L: C_3B, R: C_2E, D: C_4D},
        C_2E: {R: C_2D},
        C_2I: {L: C_4F, R: C_2K, U: C_1I, D: C_5I},
        C_2K: {L: C_2I, R: C_2N, D: C_3K},
        C_2N: {L: C_2K, R: C_2O, U: C_1N},
        C_2O: {L: C_2N},
        C_3B: {U: C_2D},
        C_3K: {U: C_2K},
        C_4C: {R: C_4D},
        C_4D: {L: C_4C, R: C_4F, U: C_2D, D: C_7D},
        C_4F: {L: C_4D, R: C_2I, D: C_5F},
        C_4M: {D: C_5M},
        C_5F: {U: C_4F},
        C_5I: {R: C_5M, U: C_2I, D: C_7I},
        C_5M: {L: C_5I, R: C_7N, U: C_4M},
        C_7D: {L: C_10A, R: C_7G, U: C_4D, D: C_9D},
        C_7G: {L: C_7D},
        C_7I: {U: C_5I},
        C_7L: {D: C_8L},
        C_7N: {R: C_7O, U: C_5M, D: C_10L},
        C_7O: {L: C_7N},
        C_8K: {R: C_8L},
        C_8L: {L: C_8K, U: C_7L, D: C_10L},
        C_9D: {R: C_9H, U: C_7D, D: C_13D},
        C_9H: {L: C_9D, R: C_10J, D: C_13H},
        C_10A: {R: C_7D},
        C_10J: {U: C_9H},
        C_10L: {R: C_7N, U: C_8L, D: C_13L},
        C_11F: {D: C_13F},
        C_12B: {D: C_13B},
        C_12L: {L: C_13J, U: C_10L, D: C_13L},
        C_12N: {D: C_13N},
        C_13B: {R: C_13D, U: C_12B, D: C_15B},
        C_13D: {L: C_13B, U: C_9D, D: C_15D},
        C_13F: {R: C_13H, U: C_11F, D: C_14F},
        C_13H: {L: C_13F, U: C_9H, D: C_15H},
        C_13J: {U: C_12L},
        C_13L: {R: C_13N, U: C_12L, D: C_15L},
        C_13N: {L: C_13L, U: C_12N, D: C_14N},
        C_14F: {U: C_13F},
        C_14N: {U: C_13N},
        C_15B: {U: C_13B},
        C_15D: {U: C_13D},
        C_15H: {U: C_13H},
        C_15L: {U: C_13L}
    }

    Costos = {
        C_1I: {D: 1},
        C_1N: {D: 1},
        C_2D: {L: 3, R: 1, D: 2},
        C_2E: {R: 1},
        C_2I: {L: 5, R: 2, U: 1, D: 3},
        C_2K: {L: 2, R: 3, D: 1},
        C_2N: {L: 3, R: 1, U: 1},
        C_2O: {L: 1},
        C_3B: {U: 3},
        C_3K: {U: 1},
        C_4C: {R: 1},
        C_4D: {L: 1, R: 2, U: 2, D: 3},
        C_4F: {L: 2, R: 5, D: 1},
        C_4M: {D: 1},
        C_5F: {U: 1},
        C_5I: {R: 4, U: 3, D: 2},
        C_5M: {L: 4, R: 3, U: 1},
        C_7D: {L: 6, R: 3, U: 3, D: 2},
        C_7G: {L: 3},
        C_7I: {U: 2},
        C_7L: {D: 1},
        C_7N: {R: 1, U: 3, D: 5},
        C_7O: {L: 1},
        C_8K: {R: 1},
        C_8L: {L: 1,U: 1, D: 2},
        C_9D: {R: 4,U: 2, D: 4},
        C_9H: {L: 4,R: 3, D: 4},
        C_10A: {R: 6},
        C_10J: {U: 3},
        C_10L: {R: 5, U: 2, D: 2},
        C_11F: {D: 2},
        C_12B: {D: 1},
        C_12L: {L: 3,U: 2, D: 1},
        C_12N: {D: 1},
        C_13B: {R: 2, U: 1, D: 2},
        C_13D: {L: 2, U: 4, D: 2},
        C_13F: {R: 2, U: 2, D: 1},
        C_13H: {L: 2, U: 4, D: 2},
        C_13J: {U: 3},
        C_13L: {R: 2, U: 1, D: 2},
        C_13N: {L: 2, U: 1, D: 1},
        C_14F: {U: 1},
        C_14N: {U: 1},
        C_15B: {U: 2},
        C_15D: {U: 2},
        C_15H: {U: 2},
        C_15L: {U: 2}
    }
    
    
    problema_lab=Problema(estado_inicial=C_7O,estados_objetivos=[C_12L],espacio_estados=Espacio_Estados)
    print(problema_lab)
    
    busqueda=BFS(problema_lab)
    muestraSolucion(busqueda)
