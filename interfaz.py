import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

class demowind(QWidget):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setGeometry(300,300,200,200)
        self.setWindowTitle('Ventana de Ejemplo')
        quit = QPushButton('Close',self)
        quit.setGeometry(10,10,70,40)
        
        #self.connect(quit,QtCore.SIGNAL('clicked()'),QtGui.qApp,QtCore.SLOT('quit()'))

app = QApplication(sys.argv)
dw = demowind()
dw.show()
sys.exit(app.exec_())