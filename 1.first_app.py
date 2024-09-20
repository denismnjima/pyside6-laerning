# importing required classes, 
from PySide6.QtWidgets import QApplication,QWidget
#importing sys used in processing cli rguments
import sys

# the QApplication is the main wrapper
app = QApplication(sys.argv)

window = QWidget()
window.show()


app.exec()