REGLAS={
    'moneda':'pedir codigo',
    'a1':'servir.bebida1',
    'a2':'servir.bebida2',
    'a3':'servir.bebida3'
}


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
        if not percepcion:
            return accion_basica
        if percepcion in self.reglas.keys():
            return self.reglas[percepcion]
        
        return accion_basica

print("Agente reactivo simple: Maquina Expendedora")

expendedora= AgenteSimple(REGLAS)
percepcion=input("indicar percepcion: ")

while percepcion:
    accion=expendedora.actuar(percepcion,'reiniciarse')
    print(accion)
    percepcion=input('indicar percepcion: ')