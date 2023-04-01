from typing import Iterator
from MiBusqueda_base import *
import numpy as np


class EstadosLaberinto(MutableMapping):
    
    def __init__(self,matriz:np.ndarray) -> None:
        super().__init__()
        self.L = Accion("L")
        self.R = Accion("R")
        self.D = Accion("D")
        self.U = Accion("U")
        
        self.Matriz=matriz
        self.Filas =self.Matriz.shape[0]
        self.Columnas = self.Matriz.shape[1]
        self.Diccionario={}
        
        # se definen los estados
        self.MatrizEstado = np.ndarray((self.Filas, self.Columnas),dtype=Estado)
        for f in range(0,self.Filas):
            for c in range(self.Columnas):
                if self.Matriz[f][c]==1:
                    lista_aux, dicc_aux = self.__acciones(f, c)
                    self.MatrizEstado[f][c]=Estado(str(f+1)+str(chr(c+65)),lista_aux)
                    
                    self.Diccionario[self.MatrizEstado[f][c]] = {}
                else:
                    self.MatrizEstado[f][c] = '0'
        
        for f in range(0,self.Filas):
            for c in range(self.Columnas):
                if self.Matriz[f][c]==1:
                    lista_aux,dicc_aux = self.__acciones(f, c)
                    
                    self.Diccionario[self.MatrizEstado[f][c]] = dicc_aux
                else:
                    self.MatrizEstado[f][c] = '0'
                    
        # for line in self.MatrizEstado:
        #     print('  '.join(map(str,line)))
        

                    
        # for estado, acciones in self.Diccionario.items():
        #     print(estado, end=":")
        #     for accion in acciones:
        #         print(accion, acciones[accion])
                    
    def __acciones(self,f,c):
        lista_aux=[]
        dicc_aux={}
        
        if f+1 < self.Filas and self.Matriz[f+1][c] == 1:
            lista_aux.append(self.D)
            dicc_aux[self.D]= self.MatrizEstado[f+1][c]
        
        if c-1 >= 0 and self.Matriz[f][c-1] == 1:
            lista_aux.append(self.L)
            dicc_aux[self.L] = self.MatrizEstado[f][c-1]
        
        if c+1 < self.Columnas and self.Matriz[f][c+1] == 1:
            lista_aux.append(self.R)
            dicc_aux[self.R] = self.MatrizEstado[f][c+1]
        
        if  f-1 >= 0        and self.Matriz[f-1][c] == 1:
            lista_aux.append(self.U)
            dicc_aux[self.U]= self.MatrizEstado[f-1][c]
        
        return lista_aux,dicc_aux
        
    def __str__(self) -> str:
        return self.Matriz.__str__()+"\n"+str(self.Filas)+" "+str(self.Columnas)
    
    def __delitem__(self, __key: str) -> None:
        return None
    
    def __getitem__(self, __key: Estado)-> Estado:
        return self.Diccionario[__key]
    
    def __iter__(self) -> Iterator:
        return self.Diccionario.__iter__()
    
    def __len__(self) -> int:
        return self.Diccionario.__len__()
    
    def __setitem__(self, __key, __value) -> None:
        return None
    
    def keys(self):
        return self.Diccionario.keys()

    def getEstado(self, num, letra):
        return self.MatrizEstado[num-1][ord(letra)-65]


if __name__ == '__main__':

    Matriz = np.loadtxt("Laberinto1.txt", dtype=int)
    lab = EstadosLaberinto(Matriz)

    # print(lab.getEstado(3,'B'))
    problema_lab = Problema(estado_inicial=lab.getEstado(8, 'D'), estados_objetivos=[
                            lab.getEstado(7, 'E')], espacio_estados=lab.Diccionario)

    # print(problema_lab)

    busqueda = BFS(problema=problema_lab)
    
    muestraSolucionCosto(problema_lab,busqueda)
    
    busqueda = DFS(problema=problema_lab)

    muestraSolucionCosto(problema_lab, busqueda)
