from MiBusqueda_base import *


class Helados(MutableMapping):
    def __init__(s) -> None:
        super().__init__()
        # self.BCajeta = Accion('BolaCajeta')
        # self.BChocolate = Accion('BolaChocolate')
        # self.BCafe = Accion('BolaCajeta')
        # self.BVainilla = Accion('BolaVainilla')
        # self.Paleta=Accion("Paleta")
        
        s.B1 = Accion("1 Bola")
        s.B2 = Accion("2 Bola")
        s.B3 = Accion("3 Bola")
        s.Diccionario={}
        
        Inicial=Estado("Inicial",[s.B1,s.B2,s.B3])
        Helado1B=Estado("Helado1B",[B])
        Helado2B=Estado("Helado2B",[B])
        Helado3B=Estado("Helado3B",[B])
        Helado3B=Estado("Helado3B",[B])
        

if __name__ == '__main__':
    # Accione: Pedir una bola de helado

    
    
    Espacio_Estados = {
        Helado1B: {Bola: Helado2B},
        Helado2B: {Bola: Helado3B}
    }
