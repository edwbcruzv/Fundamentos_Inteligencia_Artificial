from collections import deque
from .Estructuras import Accion,Estado,Nodo,Problema


"""
Funciones auxiliares
"""
def __nodoRaiz(problema:Problema)->Nodo: # Listo
    estado_raiz=problema.Estado_Inicial
    acciones_raiz={}
    
    if estado_raiz in problema.Espacio_Estados.keys():
        acciones_raiz= problema.Espacio_Estados[estado_raiz]
    raiz=Nodo(estado=estado_raiz,acciones=acciones_raiz)
    raiz.Costo=0
    return raiz


def __nodoHijo(problema: Problema, padre: Nodo, accion: Accion) -> Nodo:  # Listo
    nuevo_estado=problema.sucesorFN(padre.Estado,accion)
    acciones_nuevo={}
    
    if nuevo_estado in problema.Espacio_Estados.keys():
        acciones_nuevo = problema.Espacio_Estados[nuevo_estado]

    hijo=Nodo(nuevo_estado,accion,acciones_nuevo,padre)
    costo=padre.Costo
    costo+=problema.costoAccion(padre.Estado,accion)
    hijo.Costo=costo
    padre.addNodo(hijo)
    return hijo


def muestraSolucion(objetivo: Nodo = None):  # Listo
    print("=========================Camino del objetivo al nodo raiz============================")
    if not objetivo:
        print("No hay solucion: ", objetivo)
        print("====================================================================================")
        return
    
    nodo=objetivo
    
    while nodo:
        msg= "Estado "+nodo.Estado.__str__()
        print(msg)
        if nodo.Accion_Padre:
            msg = "<----"+nodo.Accion_Padre.__str__()+"--"
            print(msg)
        nodo=nodo.Padre
    print("====================================================================================")

def muestraSolucionCosto(problema:Problema, objetivo: Nodo = None):  # Listo
    print("=========================Camino del objetivo al nodo raiz con costos============================")
    if not objetivo:
        print("No hay solucion: ",objetivo)
        print("===============================================================================================")
        return

    nodo = objetivo

    while nodo:
        msg = "Estado "+nodo.Estado.__str__()+", Costo total:"+str(nodo.Costo)
        print(msg)
        if nodo.Accion_Padre:
            accion =nodo.Accion_Padre
            estado=nodo.Padre.Estado
            costo = problema.costoAccion(estado,accion)
            msg = "<---"+nodo.Accion_Padre.__str__() + "[" + str(costo)+"]"+"--"
            print(msg)
        nodo = nodo.Padre
    print("================================================================================================")
"""
funcion Busqueda_Primero_Anchura(problema)

    nodo_raiz=Nodo(problema)
    
    if problema.testObjetivo(nodo_raiz.Estado)
        return nodo_raiz
        
    frontera=Cola()
    forntera.appendleft(nodo_raiz) # se inserta por la izquierda
    exploradas=[]
    
    while
        if frontera.isEmpty()
            return fallo
            
        nodo=frontera-pop() # se quita y se devuelve el elemento de la derecha
        explorada.append(nodo)
        
        for accion en problema.Estados_Estados(nodo.Estado)
            hijo=Nodo(problema,nodo,accion)
            
            if hijo.Estado not in explorada and hijo.Estado not in frontera.Estados
                if problema.testObjetivo(hijo.Estado)
                    return hijo
                    
                forntera.appendleft(hijo) # se inserta por la izquierda
"""
# Busqueda primero por anchura
def BFS(problema: Problema):  # Listo
    raiz=__nodoRaiz(problema)
    
    if problema.testObjetivo(raiz.Estado):
        return raiz
    # la frontera almacena nodos
    frontera=deque([])
    frontera.appendleft(raiz)  # se inserta por la izquierda
    
    # explorados almacena estados
    explorados=set() # un set tiene elementos unicos sin repetirse
    print("=====================================================")
    while True:
        # print("Explorados:", [estado.__str__() for estado in explorados])
        print("Frontera(DEQUE-LIFO):=IN=>", [nodo.__str__() for nodo in frontera],"=OUT=>")
        
        # hasta que se quede vacia la frontera, si eso pasa no hay solucion.
        if len(frontera)==0:
           return None
        nodo = frontera.pop() # se quita y se devuelve el elemento de la derecha
        explorados.add(nodo.Estado)
        print("Pop:", nodo, end="-->")
        # print("=====================================================")
        if not nodo.Acciones:
            print("no hay acciones")
            continue
        
        # validacionde acciones que podemos realizar
        for accion in nodo.Acciones.keys():
            hijo = __nodoHijo(problema,nodo,accion)
            estados_frontera = [nodo.Estado for nodo in frontera]
            if hijo.Estado not in explorados and hijo.Estado not in estados_frontera:
                print(hijo,end="|")
                if problema.testObjetivo(hijo.Estado):
                    print("\n=====================================================",end='')
                    print("\nSe encontro el objetivo:", hijo)
                    return hijo
                
                frontera.appendleft(hijo) # se inserta por la izquierda
        print("\n=====================================================")
                
# Busqueda con Costo Uniforme
def UCS(problema: Problema):  # Listo
    raiz = __nodoRaiz(problema)
    # la frontera almacena nodos
    frontera = [raiz,]

    # explorados almacena estados
    explorados = set()  # un set tiene elementos unicos sin repetirse
    print("=====================================================")
    while True:
        print("Explorados:", [estado.__str__() for estado in explorados])
        print("Frontera(PRIORY-LIFO):<=IN==", [(nodo.__str__(),nodo.Costo)
              for nodo in frontera], "<====")

        # hasta que se quede vacia la frontera, si eso pasa no hay solucion.
        if len(frontera) == 0:
            print("Frontera vacia, no se encontro el objetivo")
            print("=====================================================")
            return None
        nodo = frontera.pop(0)  
        if problema.testObjetivo(nodo.Estado):
            print("Se encontro el objetivo:",nodo)
            print("=====================================================")
            return nodo
        explorados.add(nodo.Estado)
        print("Pop:", nodo)
        print("=====================================================")
        if not nodo.Acciones:
            print("no hay acciones")
            continue

        # validacionde acciones que podemos realizar
        for accion in nodo.Acciones.keys():
            hijo = __nodoHijo(problema, nodo, accion)

            estados_frontera = [nodo.Estado for nodo in frontera]
            if hijo.Estado not in explorados and hijo.Estado not in estados_frontera:
                frontera.append(hijo) 
            else:
                buscar = [nodo for nodo in frontera 
                          if nodo.Estado== hijo.Estado]
                
                if buscar:
                    if hijo.Costo < buscar[0].Costo:
                        indice=frontera.index(buscar[0])
                        frontera[indice]=hijo
            frontera.sort(key=lambda nodo: nodo.Costo)
"""
funcion Busqueda_Primero_Profundidad(problema)

    nodo_raiz=Nodo(problema)
    
    if problema.testObjetivo(nodo_raiz.Estado)
        return nodo_raiz
        
    frontera=pila()
    forntera.push(nodo_raiz) # se inserta en la pila
    exploradas=[]
    
    while
        if frontera.isEmpty()
            return fallo
            
        nodo=frontera.pop() # se saca de la pila
        explorada.append(nodo)
        
        for accion en problema.Estados_Estados(nodo.Estado)
            hijo=Nodo(problema,nodo,accion)
            
            if hijo.Estado not in explorada and hijo.Estado not in frontera.Estados
                if problema.testObjetivo(hijo.Estado)
                    return hijo
                    
                forntera.push(hijo) # se inserta a la pila

"""
# Busqueda Primero en Profundidad
def DFS(problema: Problema):  # Listo
    raiz = __nodoRaiz(problema)

    if problema.testObjetivo(raiz.Estado):
        return raiz
    # la frontera almacena nodos
    frontera = []
    frontera.append(raiz) 

    # explorados almacena estados
    explorados = set()  # un set tiene elementos unicos sin repetirse
    print("=====================================================")
    while True:
        # print("Explorados:", [estado.__str__() for estado in explorados])
        print("Frontera(SKACK-FIFO):", [nodo.__str__()
              for nodo in frontera], "<==OUTOUT==>")

        # hasta que se quede vacia la frontera, si eso pasa no hay solucion.
        if len(frontera) == 0:
           return None
        nodo = frontera.pop()
        explorados.add(nodo.Estado)
        print("Pop:", nodo, end="-->")
        # print("=====================================================")
        if not nodo.Acciones:
            print("no hay acciones")
            continue

        # validacionde acciones que podemos realizar
        for accion in nodo.Acciones.keys():
            hijo = __nodoHijo(problema, nodo, accion)

            estados_frontera = [nodo.Estado for nodo in frontera]
            if hijo.Estado not in explorados and hijo.Estado not in estados_frontera:
                print(hijo, end="|")
                
                if problema.testObjetivo(hijo.Estado):
                    print("\n=====================================================",end='')
                    print("\nSe encontro el objetivo:", hijo)
                    return hijo

                frontera.append(hijo)
        print("\n=====================================================")

"""
funcion Busqueda_Primero_Profundidad_Recursiva(problema)
    explorada=set()
    nodo_raiz=Nodo_Raiz(problema)
    
    return BPP_R(nodo_raiz,problema,explorada)

funcion BPP_R(nodo,problema,explorada)

    if problema.testObjetivo(nodo.Estado)
        return nodo
        
    for accion in problema.Espacio_Estados[nodo.Estado]
        hijo=Nodo_Hijo(problema,nodo,accion)
        if hijo.Estado not in explorada:
            resultado=BPP_R(hijo,problema,explorada)
            
            if resultado:
                return resultado

    retunr fallo
"""
# Busqueda Primero en Profundidad (Recursiva)
def DFS_R(problema: Problema):  # Listo
    print("=====================================================")
    explorados = set()
    nodo_raiz = __nodoRaiz(problema)
    return __BPP_R(nodo_raiz, problema, explorados)
    

def __BPP_R(nodo: Nodo, problema: Problema, explorados: set):  # Listo
    if problema.testObjetivo(nodo.Estado):
        return nodo
    explorados.add(nodo.Estado)
    print([estado.__str__() for estado in explorados])
    if not nodo.Acciones:
        return None
    for accion in problema.Espacio_Estados[nodo.Estado]:
        hijo = __nodoHijo(problema, nodo, accion)
        
        if hijo.Estado not in explorados:
            resultado = __BPP_R(hijo, problema, explorados)
            if resultado:
                return resultado
    print("=====================================================")
    return None

"""
funcion Busqueda_Profundidad_Limitada(problema,limite)
    explorara=set()
    nodo_raiz=Nodo_Raiz(problema)
    return BLP_R(nodo_raiz,problema,limite,explorada)
    
funcion BLP_R(nodo,problema,limite,explorada)
    if problema.testObjetivo(nodo.Estado)
        return nodo
    
    if limite = 0
        return corte
        
    for accion in problema.Espacio_Estados[Estado]
        hijo=Nodo_Hijo(problema,nodo,accion)
        if hijo.Estado not in explorada
            resultado=BLP_R(hijo,problema,limite-1,explorada)
            
            if resultado!= fallo
                return resultado
    
    return fallo

"""

# Busqueda Primero en Profundidad Limitada Recursiva
# Seria el DFS_R pero limitada a niveles
def LDFS_R(problema, limite=99999):  # Listo
    explorados = set()
    nodo_raiz = __nodoRaiz(problema)
    return __BPL_R(nodo_raiz, problema, limite, explorados)

def __BPL_R(nodo, problema, limite, explorados):  # Listo
    
    if problema.testObjetivo(nodo.Estado):
       return nodo

    if limite == 0:
        return None # corte
    explorados.add(nodo.Estado)

    for accion in problema.Espacio_Estados[nodo.Estado]:
        hijo = __nodoHijo(problema,nodo,accion)
        if hijo.Estado not in explorados:
            resultado = __BPL_R(hijo,problema,limite-1,explorados.copy())

            if resultado:
               return resultado

    return None

"""
funcion Busqueda_Profundidad_Iterativa(problema)
    for limite=0 to maximo
        resultado=Busqueda_Profundidad_Limitada(problema,limite)
        
        if resultado = solucion
            return solucion
    
    return fallo
"""
# Busqueda Primero en Profundidad Limitada Iterativa
def LDFS_I(problema, limite)->Nodo: # Listo
    if limite is None:
        # Si el limite no fue definida por defecto sera
        # por busqueda primero a profundidad
       resultado = DFS_R(problema)

    for i in range(1, limite + 1):
        resultado = LDFS_R(problema, i)
        if resultado:
         return resultado
    return None

"""
funcion Busqueda_Costo_Iterativo(Problema)

    for limite = 0 to maximo
        resultado=Busqueda_Costo_Limitado(problema, limite)
        if resultado=solucion
            return solucion
    return fallo

funcion Busqueda_Costo_Limitado(problema, limite)
    explorada=set()
    nodo_raiz=NodoRaiz(problema)
    
    return BCL_R(nodo_raiz,problema,explorada,limite)
    
funcion BCL_R(nodo_raiz,problema,explorada,limite)

    if problema.testObjetivo(nodo.Estado)
        return
        
    if limite<=0
        return fallo
        
    for accion in problema.Espacio_Estados[accion]
        hijo=NodoHijo(problema, nodo, accion)
        if hijo.Estado not in explorada
            resultado =BCL_R(hijo,problema,explorada,limite-hijo.Costo)
            
            if resultado!=fallo
                return resultado
    return fallo
    
"""
# Busqueda en Profundidad de Costo Iterativo
# Busqueda en Costo Iterativo
def ICS(problema:Problema,limite:int=99999,intervalo:int=1):
    
    for i in range(1,limite+1,intervalo):
        nodo_raiz = __nodoRaiz(problema)
        explorados=set()
        soluciones=[]
        __Costo_Recursivo(nodo_raiz, problema,limite, explorados,soluciones)
        if soluciones:
            print("==========================Lista del conjunto de soluciones===========================")
            print([(nodo.__str__(), nodo.Costo) for nodo in soluciones])
            mejor=min(soluciones,key=lambda nodo: nodo.Costo)
            return mejor
    return None

def __Costo_Recursivo(nodo: Nodo, problema: Problema,limite:int, explorados: set,soluciones:list):
    if limite <= 0:
        # print("Menor",limite)
        return None
    if problema.testObjetivo(nodo.Estado):
        soluciones.append(nodo)
        return nodo
    explorados.add(nodo.Estado)
    if not nodo.Acciones:
        return None
    for accion in nodo.Acciones.keys():
        hijo = __nodoHijo(problema, nodo, accion)
        if hijo.Estado not in explorados:
            costo=problema.costoAccion(nodo.Estado,accion)
            # print(limite) # tiene que ser mas grande que el costo, sino no regrega nada
            __Costo_Recursivo(hijo, problema,limite - costo, explorados.copy(),soluciones)
    return None


# Busqueda Bidireccional 
def __nodoBS(problema: Problema,estado:Estado) -> Nodo:  # Listo
    acciones = {}
    
    if estado in problema.Espacio_Estados.keys():
        acciones = problema.Espacio_Estados[estado]
        
    raiz = Nodo(estado=estado, acciones=acciones)
    raiz.Costo = 0
    return raiz

def __ampliaFrontera(problema:Problema,nodo:Nodo,objetivo:Estado,frontera:list,explorados:list):
    for accion in nodo.Acciones.keys():
        hijo=__nodoHijo(problema,nodo,accion)
        estados_frontera = [nodo.Estado for nodo in frontera]
        estados_explorados = [nodo.Estado for nodo in explorados]
        
        if hijo.Estado not in estados_explorados and hijo.Estado not in estados_frontera:
            if hijo.Estado == objetivo:
                return hijo
            
            frontera.append(hijo)
    
    return None

def BS(problema:Problema):
    nodo_i=__nodoBS(problema,problema.Estado_Inicial)
    nodo_f=__nodoBS(problema,problema.Estados_Objetivos[0])
    
    if problema.testObjetivo(nodo_f):
        return (nodo_i,nodo_f)
    
    if problema.Estado_Inicial==nodo_f.Estado:
        return (nodo_i, nodo_f)
    
    frontera_i = [nodo_i, ]
    frontera_f = [nodo_f, ]
    
    explorados_i=[]
    explorados_f=[]
    
    while True:
        if not frontera_i or not frontera_f:
            return (None,None)
        
        nodo_i = frontera_i.pop(0)
        nodo_f = frontera_f.pop()
        
        explorados_i.append(nodo_i)
        explorados_f.append(nodo_f)
        
        resultado_i = __ampliaFrontera(
            problema, nodo_i, problema.Estados_Objetivos[0], frontera_i, explorados_i)
        resultado_f = __ampliaFrontera(
            problema, nodo_f, problema.Estado_Inicial, frontera_f, explorados_f)
        
        if resultado_i:
            return (resultado,None)
        
        if resultado_f:
            return (None, resultado)
        
        nodos_arbol_i=[]
        nodos_arbol_f=[]
        nodos_arbol_i.extend(frontera_i)
        nodos_arbol_f.extend(frontera_f)
        nodos_arbol_i.extend(explorados_i)
        nodos_arbol_f.extend(explorados_f)
        print("nodos_i:",[nodo.__str__() for nodo in nodos_arbol_i])
        print("nodos_f:",[nodo.__str__() for nodo in nodos_arbol_f])
        print()
        estados_i = set(nodo.Estado for nodo in frontera_i)
        estados_f = set(nodo.Estado for nodo in frontera_f)
        
        estados_i = estados_i.union(set(nodo.Estado for nodo in explorados_i))
        estados_f = estados_f.union(set(nodo.Estado for nodo in explorados_f))
        
        comunes = estados_i.intersection(estados_f)
        if comunes:
            
            
            comun= comunes.pop()
            comun_i = [
                nodo for nodo in nodos_arbol_i if nodo.Estado == comun][0]
            comun_f = [
                nodo for nodo in nodos_arbol_f if nodo.Estado == comun][0]

            return (comun_i,comun_f)
        

def muestraSolucionBS(solucion:tuple=(None|Nodo,None|Nodo)):
    print("==================Camino Bidireccional del objetivo al nodo raiz=====================")
    nodo_i=solucion[0]
    nodo_f=solucion[1]
    
    costo_i=nodo_i.Costo if nodo_i else 0
    costo_f=nodo_f.Costo if nodo_f else 0
    camino=[]
    
    # Se recorren los nodos en su respectivo sentido
    if nodo_i:
        while nodo_i:
            camino.insert(0,nodo_i)
            nodo_i=nodo_i.Padre
    if nodo_f:
        nodo_f=nodo_f.Padre # es el nodod comun, lo saltamos para no repetirlo
        while nodo_f:
            camino.append(nodo_f)
            nodo_f=nodo_f.Padre
    
    
    if not camino:
        print("No hay solucion")
        print("====================================================================================")
        return
    
    for nodo in camino:
        msg = "Estado "+nodo.Estado.__str__()
        print(msg)
        # if nodo.Accion_Padre:
        #     msg = "<----"+nodo.Accion_Padre.__str__()+"--"
        #     print(msg)
    
    print("====================================================================================")
    print("Costo total:",costo_i+costo_f)
    print("====================================================================================")
        
