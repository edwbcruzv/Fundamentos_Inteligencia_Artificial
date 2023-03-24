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


class AgenteTabla:
    """Agente racional tipo tabla"""
    def __init__(self,acciones) -> None:
        self.acciones=acciones
        self.percepciones=""
        
    def actuar(self,percepcion,accion_basica=''):
        """Actua segun la precepcion, devolviendo una accion
        Args:
            percepcion (_type_): _description_
            accion_basica (str, optional): _description_. Defaults to ''.
        """
        if not percepcion:
            return accion_basica
        if len(self.percepciones) != 0:
            self.percepciones+=','
        self.percepciones+=percepcion
        
        if self.percepciones in self.acciones.keys():
            return self.acciones[self.percepciones]

        self.percepciones=''
        return accion_basica

print("Agente tabla: Maquina Expendedora")

expendedora= AgenteTabla(ACCIONES)
percepcion=input("indicar percepcion: ")

while percepcion:
    accion=expendedora.actuar(percepcion,'reiniciarse')
    print(accion)
    percepcion=input('indicar percepcion: ')