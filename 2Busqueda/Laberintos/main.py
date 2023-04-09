from MiBusqueda import *
from LaberintoTemplate import Laberinto


def laberinto1():
    L1 = Laberinto("Laberinto1.txt")
    print(L1)
    print("=====Soluciones para la ruta del 2B a 15L")
    p_l1 = Problema(estado_inicial=L1.getEstado(2, 'B'), estados_objetivos=[
                                L1.getEstado(15, 'L')], espacio_estados=L1.EspacioEstados)
    nodo_sol = DFS(p_l1)
    sol= nodo_sol.soluciones(problema=p_l1)
    print(sol[0])


def laberinto2():
    L2 = Laberinto("Laberinto2.txt")
    print(L2)
    print("=====Soluciones para la ruta del 10A a 2O")
    p_l2 = Problema(estado_inicial=L2.getEstado(10, 'A'), estados_objetivos=[
        L2.getEstado(2, 'O')], espacio_estados=L2.EspacioEstados)
    nodo_sol = DFS(p_l2)
    sol = nodo_sol.soluciones(problema=p_l2)
    print(sol[0])


def laberinto3():
    L3 = Laberinto("Laberinto3.txt")
    print(L3)
    print("=====Soluciones para la ruta del 10A a 2O")
    p_l3 = Problema(estado_inicial=L3.getEstado(2, 'O'), estados_objetivos=[
        L3.getEstado(4, 'M')], espacio_estados=L3.EspacioEstados)
    nodo_sol = DFS(p_l3)
    sol = nodo_sol.soluciones(problema=p_l3)
    print(sol[0])
    
if __name__ == '__main__':
    laberinto1()
    laberinto2()
    laberinto3()
