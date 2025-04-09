from qtpy.QtWidgets import QMainWindow
from qtpy.QtWidgets import QApplication

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Das ist ein Fenster")
        self.show()
        
app = QApplication([])
w = Fenster()
app.exec()