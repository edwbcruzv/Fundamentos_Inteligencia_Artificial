from MiBusqueda.NoInformada import *

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

    # Abstraccion del problema 1
    objetivo_1 = [kosos]
    problema_1 = Problema(
        estado_inicial=lanoi, estados_objetivos=objetivo_1, espacio_estados=Espacio_Estados)
    # Abstraccion del problema 2
    objetivo_2 = [goorum]
    problema_2 = Problema(
        estado_inicial=lanoi, estados_objetivos=objetivo_2, espacio_estados=Espacio_Estados)
    # Abstraccion del problema 3
    objetivo_3 = [boomon,goorum]
    problema_3 = Problema(
        estado_inicial=lanoi, estados_objetivos=objetivo_3, espacio_estados=Espacio_Estados)
    
    
    busqueda= BFS(problema=problema_1)
    muestraSolucion(busqueda) 