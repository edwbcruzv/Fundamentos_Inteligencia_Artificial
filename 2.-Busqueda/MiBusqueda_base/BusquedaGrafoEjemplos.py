
from MiBusqueda.Estructuras import Accion, Estado, Nodo, Problema


if __name__ == '__main__':
    #Acciones
    Norte = Accion('Norte')
    Sur = Accion('Sur')
    Este = Accion('Este')
    Oeste = Accion('Oeste')

    # Estados
    coruna = Estado('Coruña', [Sur, Este])
    bilbao = Estado('Bilbao', [Sur, Este, Oeste])
    barcelona = Estado('Barcelona', [Sur, Oeste])
    lisboa = Estado('Lisboa', [Norte, Sur, Este])
    madrid = Estado('Madrid', [Norte, Sur, Este, Oeste])
    valencia = Estado('Valencia', [Norte, Sur, Oeste])
    faro = Estado('Faro', [Norte, Este])
    sevilla = Estado('Sevilla', [Norte, Este, Oeste])
    granada = Estado('Granada', [Norte, Oeste])

    # Espacio de estados de un grafo, cada estado tiene su par <accion:sucesor>
    Espacio_Estados = {
        coruna: {Sur: lisboa,
                 Este: bilbao},
        bilbao: {Sur: madrid,
                 Este: barcelona,
                 Oeste: coruna},
        barcelona: {Sur: valencia,
                    Oeste: bilbao},
        lisboa: {Norte: coruna,
                 Sur: faro,
                 Este: madrid},
        madrid: {Norte: bilbao,
                 Sur: sevilla,
                 Este: valencia,
                 Oeste: lisboa},
        valencia: {Norte: barcelona,
                   Sur: granada,
                   Oeste: madrid},
        faro: {Norte: lisboa,
               Este: sevilla},
        sevilla: {Norte: madrid,
                  Este: granada,
                  Oeste: faro},
        granada: {Norte: valencia,
                  Oeste: sevilla}
    }

    kilometros = {
        coruna: {Sur: 608,
                 Este: 545},
        bilbao: {Sur: 408,
                 Este: 613,
                 Oeste: 545},
        barcelona: {Sur: 350,
                    Oeste: 613},
        lisboa: {Norte: 608,
                 Sur: 275,
                 Este: 624},
        madrid: {Norte: 408,
                 Sur: 534,
                 Este: 357,
                 Oeste: 624},
        valencia: {Norte: 350,
                   Sur: 487,
                   Oeste: 357},
        faro: {Norte: 278,
               Este: 200},
        sevilla: {Norte: 534,
                  Este: 252,
                  Oeste: 200},
        granada: {Norte: 487,
                  Oeste: 252}
    }


#============================================================================================================
    # Definimos un problema, este problema se podra usar para resolver algunos cuentionamientos
    problema_definido = Problema(estado_inicial=faro, estados_objetivos=[
                                 barcelona, madrid], espacio_estados=Espacio_Estados, costos=kilometros)
    print(problema_definido)
#============================================================================================================
#============================================================================================================
    # Faro
#============================================================================================================
    # Creamos el nodo raiz
    nodo_faro = Nodo(
        estado=faro, acciones=problema_definido.Espacio_Estados[faro])
    # obtenemos los hijos de faro
    hijos_faro = nodo_faro.expandir(problema_definido)
    print("Hijos de ", nodo_faro, ":", [hijo.__str__() for hijo in hijos_faro])
    # Obtenemos el costo del mejor hijo
    menor = nodo_faro.mejorHijo(problema_definido)
    print("Mejor hijo de ", nodo_faro, " es ", menor,
          ", con un costo de de camino ", problema_definido.costoCamino(menor))
    # Buscamos un nuevo destino por medio de una accion valida
    destino = problema_definido.sucesorFN(estado=faro, accion=Este)
    print("\nDesde ", faro, " por el ", Este, ", llegamos a ", destino)
#============================================================================================================
    # Sevilla
#============================================================================================================
    # Creamos el nodo de sevilla
    nodo_sevilla = Nodo(estado=destino, accion_padre=Este,
                        acciones=problema_definido.Espacio_Estados[sevilla])
    print("\n¿Es ", nodo_sevilla, " el destino?: ",
          "Si" if problema_definido.testObjetivo(estado=nodo_sevilla.Estado) else "No")
    # Se agrega al el nodo al padre
    nodo_faro.addNodo(nodo_sevilla)
    # Obtenemos los hijos de sevilla
    hijos_sevilla = nodo_sevilla.expandir(problema_definido)
    print("Hijos de ", nodo_sevilla, ":", [
          hijo.__str__() for hijo in hijos_sevilla])
    # Obtenemos el costo del nodo
    print("Costo: ", problema_definido.costoCamino(nodo_sevilla))
    # Obtenemos el costo del mejor hijo
    menor = nodo_sevilla.mejorHijo(problema_definido)
    print("Mejor hijo de ", nodo_sevilla, " es ", menor,
          ", con un costo de camino ", problema_definido.costoCamino(menor))
    # Buscamos un nuevo destino por medio de una accion valida
    destino = problema_definido.sucesorFN(estado=sevilla, accion=Norte)
    print("\nDe ", sevilla, " por el ", Norte, " llegamos a ", destino)
#============================================================================================================
    # Madrid
#============================================================================================================
    # Creamos el nodo de madrid
    nodo_madrid = Nodo(estado=madrid, accion_padre=Norte,
                       acciones=problema_definido.Espacio_Estados[madrid])
    print("\n¿Es ", nodo_madrid, "el destino?: ",
          "Si" if problema_definido.testObjetivo(estado=nodo_madrid.Estado) else "No")
    # agregamos el nodo al padre
    nodo_sevilla.addNodo(nodo_madrid)
    # Obtenemos los hijos de madrid
    hijos_madrid = nodo_madrid.expandir(problema_definido)
    print("Hijos de ", nodo_madrid, ":", [
          hijo.__str__() for hijo in hijos_madrid])
    # Obtenemos el costo del nodo
    print("Costo: ", problema_definido.costoCamino(nodo_madrid))
    # Obtenemos el costo del mejor hijo
    menor = nodo_madrid.mejorHijo(problema_definido)
    print("Mejor hijo de ", nodo_madrid, " es ", menor,
          ", con un costo de de camino ", problema_definido.costoCamino(menor))
    # Buscamos un nuevo destino por medio de una accion valida
    destino = problema_definido.sucesorFN(estado=madrid, accion=Este)
    print("\nDe ", madrid, " por el ", Este, " llegamos a ", destino)
#============================================================================================================
    # Valencia
#============================================================================================================
    # Creamos el nodo valencia
    nodo_valencia = Nodo(estado=valencia, accion_padre=Este,
                         acciones=problema_definido.Espacio_Estados[valencia])
    print("\n¿Es ", nodo_valencia, " el destino?: ",
          "Si" if problema_definido.testObjetivo(estado=nodo_valencia.Estado) else "No")
    # Agregamos el nodo al padre
    nodo_madrid.addNodo(nodo_valencia)
    # Obtenemos los hijos de valencia
    hijos_valencia = nodo_valencia.expandir(problema_definido)
    print("Hijos de ", nodo_valencia, ":", [
          hijo.__str__() for hijo in hijos_valencia])
    # Obtenemos el costo del nodo
    print("Costo: ", problema_definido.costoCamino(nodo_valencia))
    # Obtenemos el costo del mejor hijo
    menor = nodo_valencia.mejorHijo(problema_definido)
    print("Mejor hijo de ", nodo_valencia, " es ", menor,
          ", con un costo de de camino ", problema_definido.costoCamino(menor))
    # Buscamos un nuevo destino por medio de una accion valida
    destino = problema_definido.sucesorFN(estado=valencia, accion=Norte)
    print("\nDe ", Norte, " por el ", Norte, " llegamos a ", destino)
#============================================================================================================
    # Barcelona
#============================================================================================================
    # Creamos el nodo barcelona
    nodo_barcelona = Nodo(estado=barcelona, accion_padre=Norte,
                          acciones=problema_definido.Espacio_Estados[barcelona])
    print("\n¿Es ", nodo_barcelona, " el destino?: ",
          "Si" if problema_definido.testObjetivo(estado=nodo_barcelona.Estado) else "No")
    # Agregamos el nodo al padre
    nodo_valencia.addNodo(nodo_barcelona)
    # Obtenemos los hijos de valencia
    hijos_barcelona = nodo_barcelona.expandir(problema_definido)
    print("Hijos de ", nodo_barcelona, ":", [
          hijo.__str__() for hijo in hijos_barcelona])
    # Obtenemos el costo del nodo
    print("Costo: ", problema_definido.costoCamino(nodo_barcelona))
    # Obtenemos el costo del mejor hijo
    menor = nodo_barcelona.mejorHijo(problema_definido)
    print("Mejor hijo de ", nodo_barcelona, " es ", menor,
          ", con un costo de de camino ", problema_definido.costoCamino(menor))
#============================================================================================================
