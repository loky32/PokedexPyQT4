from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import codecs
import os
import sys

#Cargamos el archivo .ui
pokedex_ui = uic.loadUiType("pokedex1.ui")


class Interfaz(pokedex_ui[0], pokedex_ui[1]):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Pokedex')
        fondo = QPixmap('fondo/fondo21.png')
        self.final=list()
        self.cargadatos()
        self.label1.setPixmap(fondo)
        self.label1.setScaledContents(True)
        self.imagen.setPixmap(QPixmap('fondo/000.png'))
        self.salir.clicked.connect(lambda: exit())
        self.buscar.clicked.connect(self.buscador)
        self.lineEdit.returnPressed.connect(self.buscador)

    def buscador(self):
        pos=0
        pokenombre = self.lineEdit.text().capitalize()
        pokenumero= self.lineEdit.text().zfill(3)
        for i in range(0,721):
            if pokenombre == self.final[i][1]:
                pos = i
                posimagen=pos+1
                self.imagen.setPixmap(QPixmap('pokeimagenes/'+str(posimagen).zfill(3)+'.png'))
                self.tabla.setItem(0, 0, QTableWidgetItem(' #'+self.final[i][0]))
                self.tabla.setItem(0, 1, QTableWidgetItem(self.final[i][1]))
                self.t1.setPixmap(QPixmap('tipos/' + str(self.final[i][2] + '.png')).scaled(65, 27))
                if self.final[i][3]=='-':
                    self.tabla2.setItem(0, 1, QTableWidgetItem(self.final[i][3]))
                elif self.final[i][3]!='-':
                    self.t2.setPixmap(QPixmap('tipos/' + str(self.final[i][3] + '.png')).scaled(65, 27))
                self.estado.setText("Estado: Nombre encontrado")
                break

            elif pokenumero == self.final[i][0]:
                pos = i
                posimagen = pos + 1
                self.estado.setText("Estado: Número encontrado")
                self.imagen.setPixmap(QPixmap('pokeimagenes/' + str(posimagen).zfill(3)+'.png'))
                self.tabla.setItem(0, 0, QTableWidgetItem(' #'+self.final[i][0]))
                self.tabla.setItem(0, 1, QTableWidgetItem(self.final[i][1]))
                self.t1.setPixmap(QPixmap('tipos/' + str(self.final[i][2] + '.png')).scaled(65,27))
                if self.final[i][3] == '-':
                    self.tabla2.setItem(0, 1, QTableWidgetItem(self.final[i][3]))
                elif self.final[i][3] != '-':
                    self.t2.setPixmap(QPixmap('tipos/' + str(self.final[i][3] + '.png')).scaled(65, 27))
                break

            else:
                self.estado.setText('Estado: No encontrado')
                self.imagen.setPixmap(QPixmap('pokeimagenes/000.png'))
                self.tabla.setItem(0, 0, QTableWidgetItem(' ' ))
                self.tabla.setItem(0, 1, QTableWidgetItem(' '))
                self.tabla2.setItem(0, 0, QTableWidgetItem(' '))
                self.tabla2.setItem(0, 1, QTableWidgetItem(' '))
                self.t1.setText(' ')
                self.t2.setText(' ')
        self.lineEdit.setText('')


    def cargadatos(self):
        fin = codecs.open('final.txt','r','utf-8')
        for elementos in fin:
            self.final.append(elementos.strip().split(','))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    principal = Interfaz()
    principal.show()
    sys.exit(app.exec_())
