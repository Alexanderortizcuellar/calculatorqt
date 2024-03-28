from PyQt5 import QtCore, QtGui, QtWidgets
from calculator_ui import Ui_MainWindow


class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_1.clicked.connect(lambda: self.press(1))
        self.button_2.clicked.connect(lambda: self.press(2))
        self.button_3.clicked.connect(lambda: self.press(3))
        self.button_4.clicked.connect(lambda: self.press(4))
        self.button_5.clicked.connect(lambda: self.press(5))
        self.button_6.clicked.connect(lambda: self.press(6))
        self.button_7.clicked.connect(lambda: self.press(7))
        self.button_8.clicked.connect(lambda: self.press(8))
        self.button_9.clicked.connect(lambda: self.press(9))
        self.button_1.setShortcut("1")
        self.button_2.setShortcut("2")
        self.button_3.setShortcut("3")
        self.button_4.setShortcut("4")
        self.button_5.setShortcut("5")
        self.button_6.setShortcut("6")
        self.button_7.setShortcut("7")
        self.button_8.setShortcut("8")
        self.button_9.setShortcut("9")
        self.button_0.clicked.connect(lambda: self.press("0"))
        self.button_plus.setShortcut("+")
        self.button_minus.setShortcut("-")
        self.button_mult.setShortcut("*")
        self.button_div.setShortcut("/")
        self.button_equal.setShortcut("=")
        self.button_dot.setShortcut(".")
        self.clear_screen_button.clicked.connect(self.clear)
        self.button_plus.clicked.connect(lambda: self.press_symbol('+'))
        self.button_minus.clicked.connect(lambda: self.press_symbol('-'))
        self.button_mult.clicked.connect(lambda: self.press_symbol('*'))
        self.button_div.clicked.connect(lambda: self.press_symbol('/'))
        self.button_equal.clicked.connect(self.press_equal)
        self.button_dot.clicked.connect(lambda: self.press_dot('.'))

        
    
    def press(self, pressed):
        if pressed == "0" and self.screen.text() == "0":
            return
        self.screen : QtWidgets.QLabel
        if self.screen.text() == "0":
            self.screen.setText("")
        if self.upper_screen.text() != "":
            if not self.upper_screen.text()[-1].isalnum():
                self.screen.setText(str(pressed))
                self.upper_screen.setText( self.upper_screen.text() + str(pressed))
                return
            if self.upper_screen.text()[-1].isalnum():
                self.screen.setText(self.screen.text() + str(pressed))
                self.upper_screen.setText(self.upper_screen.text() + str(pressed))
                return
        else:
            self.screen.setText(self.screen.text() + str(pressed))
    
    def press_symbol(self, pressed):
        self.upper_screen.setText(self.screen.text() + str(pressed))
    
    def press_dot(self, pressed):
        if self.screen.text() == "0":
            self.screen.setText("0.")
        else:
            if self.screen.text()[-1] == ".":
                return
            self.screen.setText(self.screen.text() + str(pressed))
    

    def press_equal(self):
        if self.upper_screen.text() == "":
            return
        try:
            result = eval(self.upper_screen.text())
            self.screen.setText(str(result))
        except:
            QtWidgets.QMessageBox.about(None, "Error", "Syntax Error")

    def clear(self):
        self.screen.setText("0")
        self.upper_screen.setText("")
    


app = QtWidgets.QApplication([])
window = Calculator()
window.show()
app.exec_()