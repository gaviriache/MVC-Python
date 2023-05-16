# -*- coding: utf-8 -*-
"""
Project_One Sistema con arquitectura MVC para Surveys de servicio en centros de salud.

Luis Miguel Gaviria C. - 1035916086

"""

import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog


class MainWindow(QMainWindow):
    
    def __init__(self, ppal=None):
        
        super(MainWindow, self).__init__(ppal)  #Herencia en el constructor de la clase QMainWindow()
        loadUi("survey.ui", self)  #cargar interfaz grafica.
        
                
    #def setup(self): 
               
        # Establece un texto informativo
        # txt_name.setPlaceholderText('Nombre de Usuario'), txt_age.setPlaceholderText('Edad'), txt_identity.setPlaceholderText('Número documento')
        # txt_eps.setPlaceholderText('Eps salud'), txt_estrato.setPlaceholderText('Estrato económico')
        # txt_ciudad.setPlaceholderText('Ciudad'), txt_phone.setPlaceholderText('Número de Contacto')
        # evento producido cada vez que cambia el texto
        #txt.textChanged.connect(self.textChange)
        # establece el foco en el widget
        # txt_name.setFocus(), txt_age.setFocus() , txt_identity.setFocus(), txt_eps.setFocus() 
        # txt_estrato.setFocus() , txt_ciudad.setFocus() , txt_phone.setFocus()
        
        #
        # obtiene el texto escrito
        #nombre = txt.text()

#------------------------------------------------------

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 

#·-------------------------------------------------------------------




# class CustomTableWidgetItem(QtWidgets.QTableWidgetItem):
#     def __init__ (self, value):
#         super(CustomTableWidgetItem, self).__init__(str(value))

#     def __lt__ (self, other):
#         if (isinstance(other, CustomTableWidgetItem)):
#             try:
#                 value  = float(self.data(QtCore.Qt.EditRole))
#                 other_value = float(other.data(QtCore.Qt.EditRole))
#                 return value < other_value
#             except ValueError:
#                 pass
#         return super().__lt__(other)


# class Example(QtWidgets.QDialog):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.mainLayout = QtWidgets.QGridLayout()
#         self.setLayout(self.mainLayout)
#         self.columnas = ["Familia", "PVP", "PUC", "Margen", "Stock",
#                          "Media uds vendidas últimos tres meses"
#                          ]
#         self.listaDatos = [["Salsas y vinagres", 3.04, 2.29, 0.25, 11.0, 4.47],
#                            ["Especias y sal", 1.22, 0.9, 0.26, 38.0, 30.33],
#                            ["Platos Prep.", 2.7, 1.9, 0.3, 0.0, 0]
#                           ]  
#         self.tabla()        


#     def tabla(self):
#         #Tabla
#         self.table = QtWidgets.QTableView()
#         self.table.setObjectName("table")

#         self.tableWidget = QtWidgets.QTableWidget()
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setColumnCount(len(self.columnas))
#         self.tableWidget.setRowCount(len(self.listaDatos))

#         #Colocamos la cabecera
#         self.tableWidget.setHorizontalHeaderLabels(self.columnas)
#         header_view = self.tableWidget.horizontalHeader()
#         idx = header_view.count() - 1
#         header_view.setSectionResizeMode(idx, QtWidgets.QHeaderView.ResizeToContents)

#         #Colocamos los datos
#         for fila, lista in enumerate(self.listaDatos):
#             for columna, elemento in enumerate(lista):
#                 self.tableWidget.setItem(fila, columna,
#                                          CustomTableWidgetItem(elemento)
#                                          )
#         self.tableWidget.setSortingEnabled(True) 
#         self.mainLayout.addWidget(self.tableWidget, 6, 0, 5, 7)
















