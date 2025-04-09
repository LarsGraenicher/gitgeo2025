import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("QHBoxLayout Demo")

        # Layout erstellen:
        layout = QHBoxLayout()
        
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # 3 Push-Buttons erzeugen:
        button1 = QPushButton("Hallo")
        button2 = QPushButton("Sali")
        button3 = QPushButton("Ciao")
        edit = QLineEdit()
        
        button1.clicked.connect(self.hallo)
        button2.pressed.connect(self.sali)
        button3.released.connect(self.ciao)
        edit.textChanged.connect(self.text)
        
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # Buttons dem Layout hinzufügen
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(edit)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


    def hallo(self):
        print("Hallo!")
        
    def sali(self):
        print("Sali!")
        
    def ciao(self):
        print("Ciao!")
        
    def text(self, txt):
        if txt == "password":
            print("Gewonnen!")
        else:
            print("Leider falsch!")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()