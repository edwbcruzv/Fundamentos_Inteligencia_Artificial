import os
from time import sleep
from tkinter import Frame, Label, Tk
from tkinter.ttk import Notebook
from TableroFrame import *
from Controls import *
from LaberintoTemplate import *
from TerrenoTemplate import *
from Agente import *

class App(Frame):
    
    def __init__(s,master,width:int,height:int):
        s.Width=width
        s.Height=height
        # Constructor de Frame()
        super().__init__(master,width=s.Width,height=s.Height,background="gray")
        
        s.__changeMenu()
        s.__updateWidgets()
    
    # se  encargara de cargar los radiobuton para escojer la practica a correr
    def __changeMenu(s):
        s.CTL=Controls(s)
        s.CTL.place(x=10, y=10)
        # cada que se lececcione un radiobutton se actualizaran los widgets dependiendo de la opcion a escojer
        s.CTL.Menu.Rbtn_Laberintos.config(command=s.__updateWidgets)
        s.CTL.Menu.Rbtn_Terrenos.config(command=s.__updateWidgets)
        s.CTL.Menu.Rbtn_Proyecto1.config(command=s.__updateWidgets)
        s.pack()
        
        
    def __updateWidgets(s):
        
        # se conectan todos los botones con las funcionalidades de esta clase
        s.CTL.updateWidgets()
        
        # s.CTL.Libre.Btn_L.config(command=s.__L)
        # s.CTL.Libre.Btn_R.config(command=s.__R)
        # s.CTL.Libre.Btn_U.config(command=s.__U)
        # s.CTL.Libre.Btn_D.config(command=s.__D)
        
        # dependiendo de la opcion se carganar los laberintos o terrenos que esten en dichas carpetas,
        # los archivos txt se cargran en un combobox, excepto el proyecto
        list_values =[]
        if s.CTL.Menu.Opcion_Tablero.get() == 0 and os.path.exists('Laberintos'):
            s.CTL.Principal.Btn_Cargar.config(command=s.__Cargar)
            s.CTL.Auto.Btn_Iniciar.config(command=s.__Iniciar)
            s.CTL.Auto.Btn_Pausar.config(command=s.__Pausar)
            s.CTL.Auto.Btn_Cancelar.config(command=s.__Cancelar)
            s.CTL.Manual.Btn_Cancelar.config(command=s.__Cancelar)
            s.CTL.Manual.Btn_Back.config(command=s.__Back)
            s.CTL.Manual.Btn_Next.config(command=s.__Next)
            s.CTL.Manual.Btn_Cancelar.config(command=s.__Cancelar)
            
            list_values=os.listdir('Laberintos')
            s.CTL.Principal.Cbx_Archivos_Txt.config(values=list_values)
            s.CTL.Principal.Cbx_Archivos_Txt.bind('<<ComboboxSelected>>',s.__changeTablero)
            s.CTL.Principal.Cbtn_Vista_Agente.config(command=s.__Vista_Agente)
            
        elif s.CTL.Menu.Opcion_Tablero.get() == 1 and os.path.exists('Terrenos'):
            s.CTL.Principal.Btn_Cargar.config(command=s.__Cargar)
            s.CTL.Auto.Btn_Iniciar.config(command=s.__Iniciar)
            s.CTL.Auto.Btn_Pausar.config(command=s.__Pausar)
            s.CTL.Auto.Btn_Cancelar.config(command=s.__Cancelar)
            s.CTL.Manual.Btn_Cancelar.config(command=s.__Cancelar)
            s.CTL.Manual.Btn_Back.config(command=s.__Back)
            s.CTL.Manual.Btn_Next.config(command=s.__Next)
            s.CTL.Manual.Btn_Cancelar.config(command=s.__Cancelar)
            
            list_values = os.listdir('Terrenos')
            s.CTL.Principal.Cbx_Archivos_Txt.config(values=list_values)
            s.CTL.Principal.Cbx_Archivos_Txt.bind('<<ComboboxSelected>>',s.__changeTablero)
            s.CTL.Principal.Cbtn_Vista_Agente.config(command=s.__Vista_Agente)
            
        elif s.CTL.Menu.Opcion_Tablero.get() == 2 and os.path.exists('Proyecto1'):
            s.__proyecto1()
        else:
            return
        
        s.pack()
        
    def __changeTablero(s,event):
        
        # se define el tamaño estatico del canvas en pixeles y la posicion
        if s.CTL.Menu.Opcion_Tablero.get() == 0:
            s.Archivo_Txt = "Laberintos/" + s.CTL.Principal.Cbx_Archivos_Txt.get()
            matriz_tablero = np.loadtxt(s.Archivo_Txt, dtype=int)
            # Laberinto
            s.Tablero_cv = TableroFrame(master=s, matrix_laberinto=matriz_tablero,
                                        cells_side=matriz_tablero.shape[0], size_px=700)
        elif s.CTL.Menu.Opcion_Tablero.get() == 1:
            s.Archivo_Txt = "Terrenos/" + s.CTL.Principal.Cbx_Archivos_Txt.get()
            matriz_tablero = np.loadtxt(s.Archivo_Txt, dtype=int)
            # Terreno
            list_aux = s.CTL.Principal.Cbx_Archivos_Txt.get().split('.')
            if list_aux[0] == "Humano":
                s.Tablero_cv = HumanoFrame(master=s, matrix_laberinto=matriz_tablero,
                                        cells_side=matriz_tablero.shape[0], size_px=700)
            elif list_aux[0] == "Monkey":
                s.Tablero_cv = MonkeyFrame(master=s, matrix_laberinto=matriz_tablero,
                                        cells_side=matriz_tablero.shape[0], size_px=700)
            elif list_aux[0] == "Octopus":
                s.Tablero_cv = OctopusFrame(master=s, matrix_laberinto=matriz_tablero,
                                        cells_side=matriz_tablero.shape[0], size_px=700)
            elif list_aux[0] == "Sasquatch":
                s.Tablero_cv = SasquatchFrame(master=s, matrix_laberinto=matriz_tablero,
                                        cells_side=matriz_tablero.shape[0], size_px=700)
            else:
                return None
        else:
            return None
        
        s.Tablero_cv.place(x=(s.Width/2)+s.Tablero_cv.SideCellPX,
                       y=s.Tablero_cv.SideCellPX)

        str_lbl_char = []
        str_lbl_num = []
        for n, l in zip(range(15), range(15)):
            # print(str(n+1)+str(chr(l+65)))
            str_lbl_char.append(str(chr(l+65)))
            str_lbl_num.append(str(n+1))

        LX = LY = s.Tablero_cv.SideCellPX
        POS_X = (s.Width/2)+LX
        POS_Y = 0
        labels_X = []
        for i, text in zip(range(15), str_lbl_char):
            labels_X.append(Label(s, text="|-"+text+"-|"))
            labels_X[i].place(x=POS_X+(LX*i), y=POS_Y, width=LX, height=LY)

        POS_X = (s.Width/2)
        POS_Y = LY
        labels_Y = []
        for i, text in zip(range(15), str_lbl_num):
            labels_Y.append(Label(s, text="|-"+text+"-|"))
            labels_Y[i].place(x=POS_X, y=POS_Y+(LY*i), width=LX, height=LY)
            
        s.CTL.Principal.Fila_Origen.config(values=str_lbl_num)
        s.CTL.Principal.Columna_Origen.config(values=str_lbl_char)
        s.CTL.Principal.Fila_Destino.config(values=str_lbl_num)
        s.CTL.Principal.Columna_Destino.config(values=str_lbl_char)
        
        
        s.__Vista_Agente()
        s.pack()
    
    def __Vista_Agente(s):
        if s.CTL.Principal.VistaAgente.get():
            s.Tablero_cv.render()
        else:
            s.Tablero_cv.hide()
            
    def __Cargar(s):

        if not len(s.CTL.Principal.Lbl_Estado_Orden["text"]) == 4:
            return
        list_orden_acciones = [a for a in s.CTL.Principal.Lbl_Estado_Orden["text"]]
        # print(list_orden_acciones)
            
        s.f_o = s.CTL.Principal.Fila_Origen.get()
        s.c_o = s.CTL.Principal.Columna_Origen.get()
        s.f_d = s.CTL.Principal.Fila_Destino.get()
        s.c_d = s.CTL.Principal.Columna_Destino.get()

        print(s.f_o, s.c_o, s.f_d, s.c_d)

        if s.CTL.Menu.Opcion_Tablero.get() == 0:
            # Laberinto
            laberinto = Laberinto(s.Archivo_Txt, list_orden_acciones)
            s.agente = Agente(laberinto, origen=(int(s.f_o), s.c_o),
                              destino=(int(s.f_d), s.c_d), color=COLOR_3)
            if not s.agente.calcular(s.CTL.Principal.AlgoritmoNoInfo.get()):
                print("No se puede resolver")
                return None
            
        elif s.CTL.Menu.Opcion_Tablero.get() == 1:
            # Terreno
            terreno= Terreno(s.Archivo_Txt, list_orden_acciones)
            s.agente = Agente(terreno, origen=(int(s.f_o), s.c_o),
                              destino=(int(s.f_d), s.c_d), color=COLOR_4)
            if not s.agente.calcular(s.CTL.Principal.AlgoritmoInfo.get(),True):
                print("No se puede resolver")
                return None
        
        # Se coloca al agente en el estado inicial
        s.Tablero_cv.drawAgent(s.agente.F, s.agente.C, None)

        s.CTL.cargar()
        s.Centinela_Auto = True

    def __Iniciar(s):
        
        while s.Centinela_Auto and s.__Next():
            s.Tablero_cv.update()
            sleep(s.CTL.Auto.Scale_Velocidad.get())
        print("hecho")
        
        s.generaArbol()
        
    def generaArbol(s):
        
        s.agente.
        
        item=s.CTL.Arbol.insertar("","1")
        item2=s.CTL.Arbol.insertar(item,"2")
        s.CTL.Arbol.insertar(item,"jbhfb")
        s.CTL.Arbol.insertar(item2,"4")
        s.CTL.Arbol.insertar(item2,"oddd")
        

    def __Pausar(s):
        pass

    def __Cancelar(s):
        s.Centinela_Auto = False
        #2inicia los controles
        s.CTL.cancelar()
        # se resetea el laberinto
        s.Tablero_cv.clear()

        s.__Vista_Agente()

    def __L(s):
        pass

    def __R(s):
        pass

    def __U(s):
        pass

    def __D(s):
        pass

    def __Back(s):
        if s.CTL.Principal.OpcionRecorrido.get() == 0:
            return s.__Camino_Back()
        elif s.CTL.Principal.OpcionRecorrido.get() == 1:
            return s.__Nodo_Back()
        elif s.CTL.Principal.OpcionRecorrido.get() == 2:
            return s.__Estado_Back()
        return None

    def __Next(s):
        if s.CTL.Principal.OpcionRecorrido.get() == 0:
            return s.__Camino_Next()
        elif s.CTL.Principal.OpcionRecorrido.get() == 1:
            return s.__Nodo_Next()
        elif s.CTL.Principal.OpcionRecorrido.get() == 2:
            return s.__Estado_Next()
        return None

    def __Camino_Back(s):
        elem = s.agente.backCamino()
        s.Tablero_cv.drawAgent(s.agente.F, s.agente.C)
        return elem

    def __Camino_Next(s):
        elem = s.agente.nextCamino()
        s.Tablero_cv.drawAgent(s.agente.F, s.agente.C)
        return elem

    def __Nodo_Back(s):
        elem = s.agente.backNode()
        s.Tablero_cv.drawAgent(s.agente.F, s.agente.C)
        return elem

    def __Nodo_Next(s):
        elem = s.agente.nextNode()
        s.Tablero_cv.drawAgent(s.agente.F, s.agente.C)
        return elem

    def __Estado_Back(s):
        elem = s.agente.backState()
        if isinstance(elem, Estado):
            s.Tablero_cv.drawAgent(s.agente.F, s.agente.C)
        elif isinstance(elem, Accion):
            s.Tablero_cv.drawAgent(s.agente.F, s.agente.C, True)
        return elem

    def __Estado_Next(s):
        elem = s.agente.nextState()
        if isinstance(elem, Estado):
            s.Tablero_cv.drawAgent(s.agente.F, s.agente.C)
        elif isinstance(elem, Accion):
            s.Tablero_cv.drawAgent(s.agente.F, s.agente.C, True)
        return elem
    
    
    def __proyecto1(s):
        Humano_Txt = "Proyecto1/Humano.txt"
        matriz_tablero_humano = np.loadtxt(Humano_Txt, dtype=int)
        
        Octopus_Txt = "Proyecto1/Octopus.txt"
        matriz_tablero_octopus = np.loadtxt(Octopus_Txt, dtype=int)
        
        s.Tablero_cv_humano = Humano2Frame(master=s, matrix_laberinto=matriz_tablero_humano,
                                        cells_side=matriz_tablero_humano.shape[0], size_px=400)
        
        s.Tablero_cv_octopus = Octopus2Frame(master=s, matrix_laberinto=matriz_tablero_octopus,
                                        cells_side=matriz_tablero_octopus.shape[0], size_px=400)
        
        s.Tablero_cv_humano.place(x=(s.Width/2)+s.Tablero_cv_humano.SideCellPX,
                       y=s.Tablero_cv_humano.SideCellPX)
        
        s.Tablero_cv_humano.render() ## opaca el laberinto
        
        s.Tablero_cv_octopus.place(x=(s.Width/2)+s.Tablero_cv_octopus.SideCellPX,
                       y=s.Tablero_cv_octopus.SideCellPX+(s.Height/2))
        
        s.Tablero_cv_octopus.render()
        
        # al tener las mismas medidas se toma el del humano
        str_lbl_char = []
        str_lbl_num = []
        for n, l in zip(range(15), range(15)):
            # print(str(n+1)+str(chr(l+65)))
            str_lbl_char.append(str(chr(l+65)))
            str_lbl_num.append(str(n+1))

        LX = LY = s.Tablero_cv_humano.SideCellPX
        POS_X = (s.Width/2)+LX
        POS_Y = 0
        labels_X = []
        for i, text in zip(range(15), str_lbl_char):
            labels_X.append(Label(s, text="|-"+text+"-|"))
            labels_X[i].place(x=POS_X+(LX*i), y=POS_Y, width=LX, height=LY)

        POS_X = (s.Width/2)
        POS_Y = LY
        labels_Y = []
        for i, text in zip(range(15), str_lbl_num):
            labels_Y.append(Label(s, text="|-"+text+"-|"))
            labels_Y[i].place(x=POS_X, y=POS_Y+(LY*i), width=LX, height=LY)
        
        ##################
        LX = LY = s.Tablero_cv_humano.SideCellPX
        POS_X = (s.Width/2)+LX
        POS_Y = (s.Height/2)
        labels_X = []
        for i, text in zip(range(15), str_lbl_char):
            labels_X.append(Label(s, text="|-"+text+"-|"))
            labels_X[i].place(x=POS_X+(LX*i), y=POS_Y, width=LX, height=LY)

        POS_X = (s.Width/2)
        POS_Y = LY+(s.Height/2)
        labels_Y = []
        for i, text in zip(range(15), str_lbl_num):
            labels_Y.append(Label(s, text="|-"+text+"-|"))
            labels_Y[i].place(x=POS_X, y=POS_Y+(LY*i), width=LX, height=LY)
        
        s.CTL.Proyecto1.Fila_Humano.config(values=str_lbl_num)
        s.CTL.Proyecto1.Fila_Octopus.config(values=str_lbl_num)
        s.CTL.Proyecto1.Fila_Portal.config(values=str_lbl_num)
        s.CTL.Proyecto1.Fila_Templo.config(values=str_lbl_num)
        s.CTL.Proyecto1.Fila_Llave.config(values=str_lbl_num)
        s.CTL.Proyecto1.Columna_Humano.config(values=str_lbl_char)
        s.CTL.Proyecto1.Columna_Octopus.config(values=str_lbl_char)
        s.CTL.Proyecto1.Columna_Portal.config(values=str_lbl_char)
        s.CTL.Proyecto1.Columna_Templo.config(values=str_lbl_char)
        s.CTL.Proyecto1.Columna_Llave.config(values=str_lbl_char)
        
        s.CTL.Proyecto1.Btn_Cargar.config(command=s.__CargarProyecto1)
        ###########################################################
    
    def __CargarProyecto1(s):
        
        F_Hum=s.CTL.Proyecto1.Fila_Humano.get()
        C_Hum=s.CTL.Proyecto1.Columna_Humano.get()
        
        F_Oct=s.CTL.Proyecto1.Fila_Octopus.get()
        C_Oct=s.CTL.Proyecto1.Columna_Octopus.get()
        
        F_Port=s.CTL.Proyecto1.Fila_Portal.get()
        C_Port=s.CTL.Proyecto1.Columna_Portal.get()
        
        F_Templo=s.CTL.Proyecto1.Fila_Templo.get()
        C_Templo=s.CTL.Proyecto1.Columna_Templo.get()
        
        F_Key=s.CTL.Proyecto1.Fila_Llave.get()
        C_Key=s.CTL.Proyecto1.Columna_Llave.get()
        
        
        
        F_Hum=2
        C_Hum='A'
                
        F_Oct=15
        C_Oct='A'
                
        F_Port=9
        C_Port='D'
                
        F_Templo=4
        C_Templo='M'
                
        F_Key=10
        C_Key='N'
        
        H_Origen_Portal=0
        H_Origen_Llave=0
        H_Origen_Templo=0
        H_Llave_Templo=0
        H_Templo_Llave=0
        H_Llave_Portal=0
        H_Templo_Portal=0
        
        Archivo_Txt_Humano="Proyecto1/Humano.txt"
        #===================HUMANO=================
        
        s.Tablero_cv_humano.paintCellOrigen(int(F_Hum)-1, ord(C_Hum)-65)
        s.Tablero_cv_octopus.paintCellOrigen(int(F_Oct)-1, ord(C_Oct)-65)
        
        # Origen-Portal
        agente_P1 = Agente(Terreno(Archivo_Txt_Humano, ["L","D","R","U"]), 
                          origen=(int(F_Hum), C_Hum),
                          destino=(int(F_Port), C_Port),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        
        H_Origen_Portal=agente_P1.Costo_Total
        
        s.Tablero_cv_humano.paintCellPortal(int(F_Port)-1, ord(C_Port)-65)
        s.Tablero_cv_octopus.paintCellPortal(int(F_Port)-1, ord(C_Port)-65)
        
        
        # Origen-Llave
        agente_P1 = Agente(Terreno(Archivo_Txt_Humano, ["L","D","R","U"]), 
                          origen=(int(F_Hum), C_Hum),
                          destino=(int(F_Key), C_Key),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        
        H_Origen_Llave=agente_P1.Costo_Total
        
        # Origen-Templo
        agente_P1 = Agente(Terreno(Archivo_Txt_Humano, ["L","D","R","U"]), 
                          origen=(int(F_Hum), C_Hum),
                          destino=(int(F_Templo), C_Templo),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        
        H_Origen_Templo=agente_P1.Costo_Total
        
        # Llave-Templo
        agente_P1 = Agente(Terreno(Archivo_Txt_Humano, ["L","D","R","U"]), 
                          origen=(int(F_Key), C_Key),
                          destino=(int(F_Templo), C_Templo),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        
        s.Tablero_cv_humano.paintCellKey(agente_P1.F, agente_P1.C)
        s.Tablero_cv_octopus.paintCellKey(agente_P1.F, agente_P1.C)
        
        H_Llave_Templo=agente_P1.Costo_Total
        
        
        
        # Templo-Llave
        agente_P1 = Agente(Terreno(Archivo_Txt_Humano, ["L","D","R","U"]), 
                          origen=(int(F_Templo), C_Templo),
                          destino=(int(F_Key), C_Key),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        
        # Se coloca al agente en el estado inicial
        s.Tablero_cv_humano.paintCellTemplo(agente_P1.F, agente_P1.C)
        s.Tablero_cv_octopus.paintCellTemplo(agente_P1.F, agente_P1.C)
        
        H_Templo_Llave=agente_P1.Costo_Total
        
        
        
        # Llave-Portal
        agente_P1 = Agente(Terreno(Archivo_Txt_Humano, ["L","D","R","U"]), 
                          origen=(int(F_Key), C_Key),
                          destino=(int(F_Port), C_Port),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        
        H_Llave_Portal=agente_P1.Costo_Total
        
        
        # Templo-Portal
        agente_P1 = Agente(Terreno(Archivo_Txt_Humano, ["L","D","R","U"]), 
                          origen=(int(F_Templo), C_Templo),
                          destino=(int(F_Port), C_Port),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        
        H_Templo_Portal=agente_P1.Costo_Total
        
        
        O_Origen_Portal=0
        O_Origen_Llave=0
        O_Origen_Templo=0
        O_Llave_Templo=0
        O_Templo_Llave=0
        O_Llave_Portal=0
        O_Templo_Portal=0
        
        Archivo_Txt_Octopus = "Proyecto1/Octopus.txt"
        #===================OCTOPUS=================
        # Origen-Portal
        agente_P1 = Agente(Terreno(Archivo_Txt_Octopus, ["L","D","R","U"]), 
                          origen=(int(F_Oct), C_Oct),
                          destino=(int(F_Port), C_Port),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        
        O_Origen_Portal=agente_P1.Costo_Total
        
        # Origen-Llave
        agente_P1 = Agente(Terreno(Archivo_Txt_Octopus, ["L","D","R","U"]), 
                          origen=(int(F_Oct), C_Oct),
                          destino=(int(F_Key), C_Key),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        
        O_Origen_Llave=agente_P1.Costo_Total
        
        # Origen-Templo
        agente_P1 = Agente(Terreno(Archivo_Txt_Octopus, ["L","D","R","U"]), 
                          origen=(int(F_Oct), C_Oct),
                          destino=(int(F_Templo), C_Templo),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        
        O_Origen_Templo=agente_P1.Costo_Total
        
        # Llave-Templo
        agente_P1 = Agente(Terreno(Archivo_Txt_Octopus, ["L","D","R","U"]), 
                          origen=(int(F_Key), C_Key),
                          destino=(int(F_Templo), C_Templo),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        
        O_Llave_Templo=agente_P1.Costo_Total
        
        # Templo-Llave
        agente_P1 = Agente(Terreno(Archivo_Txt_Octopus, ["L","D","R","U"]), 
                          origen=(int(F_Templo), C_Templo),
                          destino=(int(F_Key), C_Key),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        
        O_Templo_Llave=agente_P1.Costo_Total
        
        # Llave-Portal
        agente_P1 = Agente(Terreno(Archivo_Txt_Octopus, ["L","D","R","U"]), 
                          origen=(int(F_Key), C_Key),
                          destino=(int(F_Port), C_Port),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        
        O_Llave_Portal=agente_P1.Costo_Total
        
        # Templo-Portal
        agente_P1 = Agente(Terreno(Archivo_Txt_Octopus, ["L","D","R","U"]), 
                          origen=(int(F_Templo), C_Templo),
                          destino=(int(F_Port), C_Port),
                          color=COLOR_4)
        if not agente_P1.calcular(1,True):
            print("No se puede resolver")
            return None
        O_Templo_Portal=agente_P1.Costo_Total
        
    
        
        # print(s.CTL.Proyecto1.tv1.selection())
        
        # Actualizacion Tabla 1
        s.CTL.Proyecto1.tv1.delete("I001")
        s.CTL.Proyecto1.tv1.delete("I002")
        
        s.CTL.Proyecto1.tv1.insert("",END,iid="I001",text="Humano",values=(str(H_Origen_Portal),str(H_Origen_Llave),str(H_Origen_Templo),str(H_Llave_Templo),str(H_Templo_Llave),str(H_Llave_Portal),str(H_Templo_Portal)))
        s.CTL.Proyecto1.tv1.insert("",END,iid="I002",text="Octopus",values=(str(O_Origen_Portal),str(O_Origen_Llave),str(O_Origen_Templo),str(O_Llave_Templo),str(O_Templo_Llave),str(O_Llave_Portal),str(O_Templo_Portal)))
        
        
        # Actualizacion Tabla 2
        
        # print(s.CTL.Proyecto1.tv2.selection())
               
        s.CTL.Proyecto1.tv2.delete("I001")
        s.CTL.Proyecto1.tv2.delete("I002")
        s.CTL.Proyecto1.tv2.delete("I003")
        s.CTL.Proyecto1.tv2.delete("I004")
        s.CTL.Proyecto1.tv2.delete("I005")
        s.CTL.Proyecto1.tv2.delete("I006")
        s.CTL.Proyecto1.tv2.delete("I007")
        s.CTL.Proyecto1.tv2.delete("I008")
        s.CTL.Proyecto1.tv2.delete("I009")
        s.CTL.Proyecto1.tv2.delete("I00A")
        
        diccH={
            "I-P":H_Origen_Portal,
            "I-K-P":H_Origen_Llave+H_Llave_Portal,
            "I-D-P":H_Origen_Templo+H_Templo_Portal,
            "I-K-D-P":H_Origen_Llave+H_Llave_Templo+H_Templo_Portal,
            "I-D-K-P":H_Origen_Templo+H_Templo_Llave+H_Llave_Portal
        }
        
        s.CTL.Proyecto1.tv2.insert("",END,iid="I001",text="Humano",values=("I-P",str(diccH.get("I-P"))))
        s.CTL.Proyecto1.tv2.insert("",END,iid="I002",text="Humano",values=("I-K-P",str(diccH.get("I-K-P"))))
        s.CTL.Proyecto1.tv2.insert("",END,iid="I003",text="Humano",values=("I-D-P",str(diccH.get("I-D-P"))))
        s.CTL.Proyecto1.tv2.insert("",END,iid="I004",text="Humano",values=("I-K-D-P",str(diccH.get("I-K-D-P"))))
        s.CTL.Proyecto1.tv2.insert("",END,iid="I005",text="Humano",values=("I-D-K-P",str(diccH.get("I-D-K-P"))))
        
        # I_P=s.CTL.Proyecto1.tv2
        diccO={
            "I-P":O_Origen_Portal,
            "I-K-P":O_Origen_Llave+O_Llave_Portal,
            "I-D-P":O_Origen_Templo+O_Templo_Portal,
            "I-K-D-P":O_Origen_Llave+O_Llave_Templo+O_Templo_Portal,
            "I-D-K-P":O_Origen_Templo+O_Templo_Llave+O_Llave_Portal
        }
        
        
        s.CTL.Proyecto1.tv2.insert("",END,iid="I006",text="Octopus",values=("I-P",str(diccO.get("I-P"))))
        s.CTL.Proyecto1.tv2.insert("",END,iid="I007",text="Octopus",values=("I-K-P",str(diccO.get("I-K-P"))))
        s.CTL.Proyecto1.tv2.insert("",END,iid="I008",text="Octopus",values=("I-D-P",str(diccO.get("I-D-P"))))
        s.CTL.Proyecto1.tv2.insert("",END,iid="I009",text="Octopus",values=("I-K-D-P",str(diccO.get("I-K-D-P"))))
        s.CTL.Proyecto1.tv2.insert("",END,iid="I00A",text="Octopus",values=("I-D-K-P",str(diccO.get("I-D-K-P"))))
        
        
        min_ruta_H = min(diccH, key=diccH.get)
        min_valor_H = diccH[min_ruta_H]
        
        min_ruta_O = min(diccO, key=diccO.get)
        min_valor_O = diccO[min_ruta_O]
        
        # Actualizacion Tabla 3
        
        s.CTL.Proyecto1.tv3.delete("I001")
        s.CTL.Proyecto1.tv3.delete("I002")
        s.CTL.Proyecto1.tv3.delete("I003")
        
        s.CTL.Proyecto1.tv3.insert("",END,iid="I001",text="Humano",values=(min_ruta_H,min_valor_H))
        s.CTL.Proyecto1.tv3.insert("",END,iid="I002",text="Octopus",values=(min_ruta_O,min_valor_O))
        s.CTL.Proyecto1.tv3.insert("",END,iid="I003",text="Total",values=("",str(min_valor_H+min_valor_O)))
        s.pack()

if __name__ == '__main__':
    root = Tk()
    root.title("Ventana Principal")
    app = App(root, 1600, 900)
    app.mainloop()
