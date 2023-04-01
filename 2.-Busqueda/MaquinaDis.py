from MiBusqueda_base import *


if __name__ == '__main__':
    
    
    L=Accion("Izq")
    R=Accion("Der")
    
    S1 = Estado("S1", [L, R])
    S2 = Estado("S2", [L, R])
    S3 = Estado("S3", [L, R])
    S4 = Estado("S4", [L, R])
    S5 = Estado("S5", [L, R])
    
    Espacio_Estados={
        S1: {L: S2, R: S5},
        S2: {L: S3, R: S1},
        S3: {L: S4, R: S2},
        S4: {L: S5, R: S3},
        S5: {L: S1, R: S4}
    }
    
    problema_1 = Problema(estado_inicial=S2, estados_objetivos=[S5], espacio_estados=Espacio_Estados)
    muestraSolucionCosto(problema_1,LDFS_I(problema=problema_1,limite=2))
    problema_1 = Problema(estado_inicial=S5, estados_objetivos=[S1], espacio_estados=Espacio_Estados)
    muestraSolucionCosto(problema_1,LDFS_I(problema=problema_1,limite=2))
    problema_1 = Problema(estado_inicial=S1, estados_objetivos=[S3], espacio_estados=Espacio_Estados)
    muestraSolucionCosto(problema_1,LDFS_I(problema=problema_1,limite=2))

    
