from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, QtWidgets , uic

qtCreatorFile = "tax_calc.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_tax_button.clicked.connect(self.CalculateTax)
    
    def CalculateTax(self):
        price = int(self.price_box.toPlainText())
        tax = (self.tax_rate.value())
        total_price = price  + ((tax / 100) * price)
        total_price_string = "o valor total do salario e: " + str(total_price)
        self.results_window.setText(total_price_string)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())