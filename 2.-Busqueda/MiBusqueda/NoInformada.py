from collections import deque
from .Estructuras import Accion,Estado,Nodo,Problema


"""
funcion BFS(problema)

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

def __nodoRaiz(problema:Problema)->Nodo:
    estado_raiz=problema.Estado_Inicial
    acciones_raiz={}
    
    if estado_raiz in problema.Espacio_Estados.keys():
        acciones_raiz= problema.Espacio_Estados[estado_raiz]
    
    return Nodo(estado=estado_raiz,acciones=acciones_raiz)


def __nodoHijo(problema:Problema,padre:Nodo,accion:Accion)->Nodo:
    nuevo_estado=problema.sucesorFN(padre.Estado,accion)
    acciones_nuevo={}
    
    if nuevo_estado in problema.Espacio_Estados.keys():
        acciones_nuevo = problema.Espacio_Estados[nuevo_estado]

    hijo=Nodo(nuevo_estado,accion,acciones_nuevo,padre)
    padre.addNodo(hijo)
    return hijo
    

def BFS(problema:Problema):
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
        print("Explorados:", [estado.__str__() for estado in explorados])
        print("Frontera:==IN==>", [nodo.__str__() for nodo in frontera],"===OUT==>")
        
        # hasta que se quede vacia la frontera, si eso pasa no hay solucion.
        if len(frontera)==0:
           return None
        nodo = frontera.pop() # se quita y se devuelve el elemento de la derecha
        explorados.add(nodo.Estado)
        print("Pop:", nodo)
        print("=====================================================")
        if not nodo.Acciones:
            print("no hay acciones")
            continue
        
        # validacionde acciones que podemos realizar
        for accion in nodo.Acciones.keys():
            hijo = __nodoHijo(problema,nodo,accion)
            
            estados_frontera = [nodo.Estado for nodo in frontera]
            if hijo.Estado not in explorados and hijo.Estado not in estados_frontera:
                if problema.testObjetivo(hijo.Estado):
                    return hijo
                
                frontera.appendleft(hijo) # se inserta por la izquierda


def muestraSolucion(objetivo:Nodo=None):
    if not objetivo:
        print("No hay solucion")
        return 
    
    nodo=objetivo
    
    while nodo:
        msg= "Estado "+nodo.Estado.__str__()
        print(msg)
        if nodo.Accion_Padre:
            msg = "<----"+nodo.Accion_Padre.__str__()+"----"
            print(msg)
        nodo=nodo.Padre
        
        
"""
funcion DFS(problema)

    nodo_raiz=Nodo(problema)
    
    if problema.testObjetivo(nodo_raiz.Estado)
        return nodo_raiz
        
    frontera=pila()
    forntera.appendleft(nodo_raiz) # se inserta por la izquierda
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
                    
                forntera.push(hijo) # se inserta por la izquierda

"""


def DFS(problema: Problema):
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
        print("Explorados:", [estado.__str__() for estado in explorados])
        print("Frontera:==IN==>", [nodo.__str__()
              for nodo in frontera], "===OUT==>")

        # hasta que se quede vacia la frontera, si eso pasa no hay solucion.
        if len(frontera) == 0:
           return None
        nodo = frontera.pop()
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
                if problema.testObjetivo(hijo.Estado):
                    return hijo

                frontera.append(hijo)
