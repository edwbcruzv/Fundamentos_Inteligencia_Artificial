REGLAS={
    'moneda':'pedir codigo',
    'a1':'servir.bebida1',
    'a2':'servir.bebida2',
    'a3':'servir.bebida3'
}

"""Peudocodigo
funcion Agente-Reactivo-Simple(percepcion,accion_inicial)
    variables estaticas
            accion=accion_inicial|vacia
            reglas={
                condicion1:accion1,
                condicion2:accion2,
                condicion3:accion3,
                ...
                }
    estado=interpretar_entrada(percepcion)
    regla=reglas.estado
    accion=regla.accion[regla]
    
    return accion
"""


class AgenteSimple:
    """Agente reactivo simple"""
    def __init__(self,reglas) -> None:
        self.reglas=reglas
        
    def actuar(self,percepcion,accion_basica=''):
        """Actua segun la precepcion, devolviendo una accion
        Args:
            percepcion (_type_): _description_
            accion_basica (str, optional): _description_. Defaults to ''.
        """
        # validacion de la percepcion
        if not percepcion:
            return accion_basica
        
        # si el estado de la percepcion esta en las reglas
        if percepcion in self.reglas.keys():
            # se busca la regla y se regresa la accion
            return self.reglas[percepcion]
        else:
            # si no se reinicia
            return accion_basica

print("Agente reactivo simple: Maquina Expendedora")

expendedora= AgenteSimple(REGLAS)
percepcion=input("indicar percepcion: ")

while percepcion:
    accion=expendedora.actuar(percepcion,'reiniciarse')
    print(accion)
    percepcion=input('indicar percepcion: ')