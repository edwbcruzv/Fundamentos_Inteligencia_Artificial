
"""
funcion Agente-Simple-Resolvente-De-Problemas(percepcion)
    variables estaticos:
        sequencia=[]
        estado=estado_inicial
        estado_meta=null
        problema=formulacion del problema
        
    estado=actualizarEstado(estado,percepcion)
    
    
    if sequencia.esVacio()
        estado_meta=FormularObjetivo(estado)
        problema=FormularProblema(estado,objetivo)
        secuencia=Busqueda(problema)
    accion=Primero(secuencia)
    secuencia=Resto(secuencia)

    return accion
"""

"""
frontera:list
frontera.esVacia():bool
frontera.pop():Nodo
frontera.append(Nodo):list
frontera.remove(Nodo):list
"""


# algoritmo base para DFS y BFS, no sirve para grafos
"""
funcion Busqueda-Arbol(problema)
    variables_estaticos:
        frontera=[]
    frontera.append(problema.Estado_Inicial)
        
    while:
    
        if frontera.esVacia()
            return fallo
        
        nodo=frontera.pop() # segun el algoritmo sera LIFO o FIFO
        
        if problema.testObjetivo(nodo)
            return nodo
        
        nodos=nodo.expandir(problema)
        frontera.append(nodos)
"""
# Algoritmo de busqueda en grafos

"""
funcion Busqueda-Grafo(problema)
    variables_estaticos:
        frontera=[]
        explorada=[]:Estado
    
    frontera.append(problema.Estado_Inicial)
    
    while
        is frontera.EsVacia()
            return fallo
        
        nodo=frontera.pop() # segun el algoritmo sera LIFO o FIFO
        
        if problema.testObjetivo(nodo)
            return nodo
            
        explorada.append(nodo.Estado)
        nodos=nodo.expandir(problema)
        
        for nodo in nodos
                if nodo not in frontera and nodo.Estado not in explorada
                    frontera.append(nodos)

"""


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
