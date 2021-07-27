from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from untitled import Ui_Dialog
import sys


app = QApplication(sys.argv)
Dialog = QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
