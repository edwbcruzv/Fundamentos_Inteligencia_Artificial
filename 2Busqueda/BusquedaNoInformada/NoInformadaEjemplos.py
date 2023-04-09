from MiBusqueda import *

if __name__ == '__main__':

    # Acciones
    N = Accion('N')
    S = Accion('S')
    E = Accion('E')
    O = Accion('O')

    NE = Accion('NE')
    NO = Accion('NO')
    SE = Accion('SE')
    SO = Accion('SO')

    # Estados

    lanoi = Estado('Lanoi', [NE])
    nohoi = Estado('Nohoi', [SO, NO, NE])
    ruun = Estado('Ruun', [NO, NE, E, SE])
    milos = Estado('Milos', [O, SO, N])
    ghiido = Estado('Ghiido', [N, E, SE])
    kuart = Estado('Kuart', [O, SO, NE])
    boomon = Estado('Boomon', [N, SO])
    goorum = Estado('Goorum', [O, S])
    shiphos = Estado('Shiphos', [O, E])
    nokshos = Estado('Nokshos', [NO, S, E])
    pharis = Estado('Pharis', [NO, SO])
    khamin = Estado('Khamin', [SE, NO, O])
    tarios = Estado('Tarios', [O, NO, NE, E])
    peranna = Estado('Peranna', [O, E])
    khandan = Estado('Khandan', [O, S])
    tawa = Estado('Tawa', [SO, SE, NE])
    theer = Estado('Theer', [SO, SE])
    roria = Estado('Roria', [NO, SO, E])
    kosos = Estado('Kosos', [O])

    Espacio_Estados = {
        lanoi: {NE: nohoi},
        nohoi: {
            SO: lanoi,
            NO: ruun,
            NE: milos},
        ruun: {
            NO: ghiido,
            NE: kuart,
            E: milos,
            SE: nohoi},
        milos: {
            O: ruun,
            SO: nohoi,
            N: khandan},
        ghiido: {
            N: nokshos,
            E: kuart,
            SE: ruun},
        kuart: {
            O: ghiido,
            SO: ruun,
            NE: boomon},
        boomon: {
            N: goorum,
            SO: kuart},
        goorum: {
            O: shiphos,
            S: boomon},
        shiphos: {
            O: nokshos,
            E: goorum},
        nokshos: {
            NO: pharis,
            S: ghiido,
            E: shiphos},
        pharis: {
            NO: khamin,
            SO: nokshos},
        khamin: {
            SE: pharis,
            NO: tawa,
            O: tarios},
        tarios: {
            O: khamin,
            NO: tawa,
            NE: roria,
            E: peranna},
        peranna: {O: tarios,
                  E: khandan},
        khandan: {O: peranna,
                  S: milos},
        tawa: {
            SO: khamin,
            SE: tarios,
            NE: theer},
        theer: {
            SO: tawa,
            SE: roria},
        roria: {
            NO: theer,
            SO: tarios,
            E: kosos},
        kosos: {O: roria},
    }
    
    Espacio_Costos = {
        lanoi: {NE: 42},
        nohoi: {
            SO: 52,
            NO: 21,
            NE: 95},
        ruun: {
            NO: 88,
            NE: 16,
            E: 90,
            SE: 21},
        milos: {
            O: 90,
            SO: 95,
            N: 133},
        ghiido: {
            N: 17,
            E: 92,
            SE: 88},
        kuart: {
            O: 92,
            SO: 16,
            NE: 83},
        boomon: {
            N: 8,
            SO: 83},
        goorum: {
            O: 59,
            S: 8},
        shiphos: {
            O: 71,
            E: 56},
        nokshos: {
            NO: 5,
            S: 17,
            E: 71},
        pharis: {
            NO: 29,
            SO: 5},
        khamin: {
            SE: 29,
            NO: 121,
            O: 98},
        tarios: {
            O: 98,
            NO: 83,
            NE: 57,
            E: 82},
        peranna: {O: 82,
                  E: 44},
        khandan: {O: 44,
                  S: 133},
        tawa: {
            SO: 121,
            SE: 83,
            NE: 11},
        theer: {
            SO: 11,
            SE: 36},
        roria: {
            NO: 36,
            SO: 57,
            E: 104},
        kosos: {O: 104},
    }

    # Abstraccion del problema 1
    objetivo_1 = [kosos]
    problema_1 = Problema(
        estado_inicial=lanoi, estados_objetivos=objetivo_1, espacio_estados=Espacio_Estados,costos=Espacio_Costos)
    # Abstraccion del problema 2
    objetivo_2 = [goorum]
    problema_2 = Problema(
        estado_inicial=lanoi, estados_objetivos=objetivo_2, espacio_estados=Espacio_Estados, costos=Espacio_Costos)
    # Abstraccion del problema 3
    objetivo_3 = [boomon,goorum]
    problema_3 = Problema(
        estado_inicial=lanoi, estados_objetivos=objetivo_3, espacio_estados=Espacio_Estados, costos=Espacio_Costos)
    
#=====================================================================================================
# busqueda primero por anchura
    # busqueda= BFS(problema=problema_1)
    # print(busqueda.soluciones(problema=problema_1)[1])

#=====================================================================================================
# Busqueda con Costo Iniforme
    # busqueda=UCS(problema_1)
    # print(busqueda.soluciones(problema=problema_1)[2])

#=====================================================================================================
# Busqueda Primero en Profundidad
    # busqueda = DFS(problema=problema_1)
    # print(busqueda.soluciones(problema=problema_1)[1])
    
#=====================================================================================================
# Busqueda Primero en Profundidad Recursiva
    # busqueda= DFS_R(problema=problema_1)
    # print(busqueda.soluciones(problema=problema_1)[1])
    
#=====================================================================================================
# Busqueda Primero en Profundidad Limitada Recursiva
    # limite con 7 (solucion optima) y 10 cambia el recorrido
    # busqueda = LDFS_R(problema=problema_1,limite=10) 
    # print(busqueda.soluciones(problema=problema_1)[2])
    
#=====================================================================================================
# Busqueda Primero en Profundidad Limitada Iterativa
    # Va nivel por nivel buscando la solucion optima, al encontrarla se detiene y regresa la solucion.
    # busqueda = LDFS_I(problema=problema_1,limite=10) 
    # print(busqueda.soluciones(problema=problema_1)[2])
    
#=====================================================================================================
# Busqueda en Profundidad de Costo Iterativo
    # Calculara todos los caminos posibles dependiendo de el limite que pongamos,
    # regregara el que tenga el menor costo y dependera del maximo limite e intervalo que deseeemos
    # Entre todas las soluciones encuentra la minima
    
    
    # busqueda = ICS(problema=problema_1,limite=500) # limite minimo 500
    # print(busqueda.soluciones(problema=problema_1)[2])
    
    # busqueda = ICS(problema=problema_1,limite=1000,intervalo=10)
    # print(busqueda.soluciones(problema=problema_1)[2])
    
    # busqueda = ICS(problema=problema_1, limite=1000, intervalo=100)
    # print(busqueda.soluciones(problema=problema_1)[2])
    
    # busqueda = ICS(problema=problema_2, limite=1000, intervalo=10)
    # print(busqueda.soluciones(problema=problema_1)[2])
#=====================================================================================================
# Busqueda Bidireccional
    # Condiciones: 
    # 1 Se debe de conocer el origen y el destino.
    # 2 No se pueden tener 2 o mas objetivos.

    solucion = BS(problema=problema_1)
    print(solucion)
    
    solucion = BS(problema=problema_2)
    print(solucion)



#=====================================================================================================
