



class Accion:
    
    def __init__(self,nombre) -> None:
        self.nombre=nombre
        
    def __str__(self) -> str:
        return self.nombre
    
    
class Estado:
    
    def __init__(self,nombre,acciones) -> None:
        self.nombre=nombre
        self.acciones=acciones
        
    def __str__(self) -> str:
        return self.nombre




class Problema:
    
    def __init__(self,estado_inicial,estados_objetivos,acciones) -> None:
        self.estado_inicial=estado_inicial
        self.estados_objetivos=estados_objetivos
        self.acciones=acciones
        
    def __str__(self) -> str:
        msg="Estado Inicial:{0}->Objetivos: {1}"
        return msg.format(self.estado_inicial,self.estados_objetivos)
    
    def es_objetivo(self,estado):
        return estado in self.estados_objetivos
    
    def retultado(self,estado,accion):
        if estado.nombre not in self.acciones.keys():
            return None

        acciones_estado=self.acciones[estado.nombre]
        
        if accion.nombre not in acciones_estado.keys():
            return None
        return acciones_estado[accion.nombre]
    
class Nodo:
    
    def __init__(self,estado,accion=None,acciones=None,padre=None) -> None:
        self.estado=estado
        self.accion=accion
        self.acciones=acciones
        
    def __str__(self) -> str:
        return self.nombre
    
    def expandir(self,problema):
        self.hijos=[]
        if not self.acciones:
            if self.estado.nombre not in problema.acciones.keys():
                return self.hijos
            self.acciones=problema.acciones[self.estado.nombre]
    
if __name__ == '__main__':
    acc_N=Accion('Norte')
    acc_S=Accion('Sur')
    acc_E=Accion('Este')
    acc_O=Accion('Oeste')
    
    
    coruna=Estado('A Coruña',[acc_S,acc_E])
    bilbao=Estado('Bilbao',[acc_S,acc_E,acc_O])
    barcelona=Estado('Barcelona',[acc_S,acc_O])
    lisboa=Estado('Lisboa',[acc_N,acc_S,acc_E])
    madrid=Estado('Madrid',[acc_N,acc_S,acc_E,acc_O])
    valencia=Estado('Valencia',[acc_N,acc_S,acc_O])
    faro=Estado('Faro',[acc_N,acc_E])
    sevilla=Estado('Sevilla',[acc_N,acc_E,acc_O])
    granada=Estado('Granada',[acc_N,acc_O])
    
    
    
    viajes={'A Coruña':{'Sur':lisboa,
                        'Este':bilbao},
            'Bilboa':{'Sur':madrid,
                      'Este':barcelona,
                      'Oeste':coruna},
            'Barcelona':{'Sur':valencia,
                         'Oeste':bilbao},
            'Lisboa':{'Norte':coruna,
                      'Sur':faro,
                      'Este':madrid},
            'Madrid':{'Norte':bilbao,
                      'Sur':sevilla,
                      'Este':valencia,
                      'Oeste':lisboa},
            'Valencia':{'Norte':barcelona,
                        'Sur':granada,
                        'Oeste':madrid},
            'Faro':{'Norte':lisboa,
                    'Este':sevilla},
            'Sevilla':{'Norte':madrid,
                       'Este':granada,
                       'Oeste':faro},
            'Granada':{'Norte':valencia,
                       'Oeste':sevilla}
            }
    
        
    