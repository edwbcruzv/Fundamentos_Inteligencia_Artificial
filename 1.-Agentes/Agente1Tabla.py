
# Tabla de acciones
ACCIONES={
    'moneda':'pedir codigo',
    'moneda,a1':'servir.bebida1',
    'moneda,a2':'servir.bebida2',
    'moneda,a3':'servir.bebida3',
    'moneda,a1,moneda':'pedir.codigo',
    'moneda,a2,moneda':'pedir.codigo',
    'moneda,a3,moneda':'pedir.codigo',
    'moneda,a1,moneda,a1':'servir.bebida1',
    'moneda,a1,moneda,a2':'servir.bebida2',
    'moneda,a1,moneda,a3':'servir.bebida3',
    'moneda,a2,moneda,a1':'servir.bebida1',
    'moneda,a2,moneda,a2':'servir.bebida2',
    'moneda,a2,moneda,a3':'servir.bebida3',
    'moneda,a3,moneda,a1':'servir.bebida1',
    'moneda,a3,moneda,a2':'servir.bebida2',
    'moneda,a3,moneda,a3':'servir.bebida3'
}

""" Pseudocodigo
funcion Agente-Dirigido-Mediante-Tabla(percepcion,accion_inicial) 
    variables estaticas
            accion=accion_inicial|vacia
            percepciones=[]
            tabla_acciones={"p1,p2,...,pn":"accion",
                            "p1,p2,...,pn":"accion",
                            "p1,p2,...,pn":"accion",
                            ...}
    percepciones.append(percepcion)
    accion=tabla_acciones.consultar(percepciones)
    
    return accion
"""



class AgenteTabla:
    """Agente racional tipo tabla"""
    def __init__(self,acciones) -> None:
        self.acciones=acciones
        self.percepciones=""
        
    def actuar(self,percepcion,accion_basica=''):
        """Actua segun la precepcion, devolviendo una accion
        Args:
            percepcion (_type_): percepcion del agente
            accion_basica (str, optional): si la percepcion no e svalida, Defaults to ''.
        """
        
        # si no se percibe nada
        if not percepcion:
            return accion_basica
        
        # en caso de existir percepciones previas
        if len(self.percepciones) != 0:
            # se le agrega una coma para agregar a la lista de percepciones
            self.percepciones+=','
            
        self.percepciones+=percepcion
        
        # se busca las percepciones que llevamos en la tabla
        if self.percepciones in self.acciones.keys():
            # se regresa la accion
            return self.acciones[self.percepciones]
        else:
            self.percepciones=''
            return accion_basica

print("Agente tabla: Maquina Expendedora")

expendedora= AgenteTabla(ACCIONES)
percepcion=input("indicar percepcion: ")

while percepcion:
    
    accion=expendedora.actuar(percepcion,'reiniciarse')
    print(accion)
    percepcion=input('indicar percepcion: ')