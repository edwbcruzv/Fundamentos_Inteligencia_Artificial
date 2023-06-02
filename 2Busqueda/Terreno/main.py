from TerrenoTemplate import *

if __name__ == '__main__':
    T=Terreno("Humano.txt",['L','R','D','U'])
    # print(T)
    
    T_P=Problema(estado_inicial=T.getEstado(7,'C'),
                 estados_objetivos=[T.getEstado(7,'G')],
                 espacio_estados=T.EspacioEstados)
    # print(T_P)
    
    Arbol,Trayectoria = UCS_A(problema=T_P)
    Camino=Arbol.soluciones(T_P)
    print([e.__str__() for e in Trayectoria])
    print(Camino[0])
    