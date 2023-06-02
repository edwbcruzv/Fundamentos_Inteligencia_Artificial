##conexion con la interfaz grafica comando>   pyuic5 -x Interfaz.ui -o Interfaz.py
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Interfaz import *
import sys

import numpy as np
import pandas as pd


class Ventana(QtWidgets.QWidget):


    def __init__(s,parent=None):
        super(Ventana,s).__init__(parent)
        s.ui=Ui_Form()
        s.ui.setupUi(s)

        s.ui.pushButton_Buscar_Dataset.clicked.connect(s.__searchFile)
        s.ui.pushButton_Cargar_Dataset.clicked.connect(s.__changeDataset)
        s.ui.pushButton_Vector.clicked.connect(s.__getVector)
    
    def __updateWidgets(s):
        pass
    
    def __searchFile(s):
        
        s.str_file_dataset,_=QFileDialog.getOpenFileName(s,"buscalee","","Text Files (*.txt) ;; Names (*.names)",options=QFileDialog.DontUseNativeDialog)
        
        
    def __changeDataset(s):
        
        sep=None
        
        if s.ui.radioButton_Pipe.isChecked():
            sep='|'
        elif s.ui.radioButton_Coma.isChecked():
            sep=','
        elif s.ui.radioButton_Dos_Puntos.isChecked():
            sep=':'
        elif s.ui.radioButton_Hashtag.isChecked():
            sep='#'
        elif s.ui.radioButton_P_Coma.isChecked():
            sep=';'
        
        if sep:
            s.dataset = pd.read_csv(s.str_file_dataset,sep=sep)
            print(s.dataset)
            
        else:
            print("Selecciona el sepatador.")
        
        s.__table()
            
        
    def __table(s):
        _translate = QtCore.QCoreApplication.translate
        
        filas = s.dataset.shape[0]
        columnas = s.dataset.shape[1]
        print(filas,columnas)
        
        # numero de filas y columnas de la tabla
        s.ui.tableWidget_Dataset.setColumnCount(columnas)
        s.ui.tableWidget_Dataset.setRowCount(filas+1) # +1 por los checkbox
        
        s.ui.tableWidget_Dataset.columnCount()
        s.ui.tableWidget_Dataset.rowCount()
        
        #definiendo los numeros de las filas
        for f in range(s.ui.tableWidget_Dataset.rowCount()):
            item = QtWidgets.QTableWidgetItem()
            s.ui.tableWidget_Dataset.setVerticalHeaderItem(f, item)

        #definiendo las columnas
        for c in range(s.ui.tableWidget_Dataset.columnCount()):
            item = QtWidgets.QTableWidgetItem()
            item.setText(_translate("Form", s.dataset.columns.values[c]))
            s.ui.tableWidget_Dataset.setHorizontalHeaderItem(c, item)
        
        ##definiendo los cuadros de las tabla (matriz)
        for f in range(s.ui.tableWidget_Dataset.rowCount()):
            for c in range(s.ui.tableWidget_Dataset.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                s.ui.tableWidget_Dataset.setItem(f, c, item)
        
        #etiquetas del numero de filas
        for f in range(1,s.ui.tableWidget_Dataset.rowCount()):
            item = s.ui.tableWidget_Dataset.verticalHeaderItem(f)
            item.setText(_translate("Form", str(f)))
            
        # primera fila de checkbox
        for c in range(s.ui.tableWidget_Dataset.columnCount()):
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Checked)
            s.ui.tableWidget_Dataset.setItem(0, c, item)
        
        
        for f in range(filas):
            
            # print(dataset[f])
            for c in range(columnas):
                # print(dataset.iloc[f,c], end="\t")
                # print(f,c)
                item = s.ui.tableWidget_Dataset.item(f+1, c)
                item.setText(_translate("Form", str(s.dataset.iloc[f,c])))
        
        __sortingEnabled = s.ui.tableWidget_Dataset.isSortingEnabled()
        s.ui.tableWidget_Dataset.setSortingEnabled(False)
        
        s.ui.tableWidget_Dataset.setSortingEnabled(__sortingEnabled)
        
        
        # Obtén el modelo de selección del QTableView
        s.modelo_seleccion = s.ui.tableWidget_Dataset.selectionModel()
    def __getVector(s):
        
        # Obtén el índice de la fila seleccionada utilizando el cursor del mouse
        indice_seleccionado = s.modelo_seleccion.currentIndex()

        # Obtén el número de fila seleccionada
        fila = indice_seleccionado.row()

        
        print(list(s.dataset.iloc[fila-1,:].tolist()))
        
        s.ui.label_Vector.setText(str(list(s.dataset.iloc[fila-1,:].values)))
        
        

##*****INICIO DE TODO EL PROGRAMA
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    myapp=Ventana()
    myapp.show()
    sys.exit(app.exec_())