import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import datetime
import os

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        save = QAction("Save", self)
        save.triggered.connect(self.savebutton_clicked)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)

        quit.setMenuRole(QAction.QuitRole) #für MAC

        filemenu.addAction(save)
        filemenu.addAction(quit)



    def menu_quit(self):
        print("Quit")
        self.close()

    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("GUI Programmierung")
        ### LAYOUT WÄHLEN:
        layout = QFormLayout()
        
        self.vornameLineEdit= QLineEdit()
        self.nameLineEdit= QLineEdit()
        self.datumLineEdit= QDateEdit()
        self.adresseLineEdit= QLineEdit()
        self.plzLineEdit=QLineEdit()
        self.ortLineEdit=QLineEdit()
        self.countries = QComboBox() 
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"]) 

        layout.addRow("Vorname: ", self.vornameLineEdit)
        layout.addRow("Name: ", self.nameLineEdit)
        layout.addRow("Geburtstag: ", self.datumLineEdit)
        layout.addRow("Adresse: ", self.adresseLineEdit)
        layout.addRow("PLZ: ", self.plzLineEdit)
        layout.addRow("Ort: ", self.ortLineEdit)
        layout.addRow("Land: ", self.countries)
        
        
        self.savebutton = QPushButton("Save")
        self.savebutton.clicked.connect(self.savebutton_clicked)

        layout.addRow(self.savebutton)
        
    

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        
        ## Widgets erstellen
        # ...

        ## Layout füllen
        # ...

        ## Fenster anzeigen
        self.show()


    def createConnects(self):
        pass


    def savebutton_clicked(self):
        vorname = self.vornameLineEdit.text()
        name = self.nameLineEdit.text()
        geburtsdatum = self.datumLineEdit.date().toPyDate()
        adresse= self.adresseLineEdit.text()
        plz= self.plzLineEdit.text()
        ort= self.ortLineEdit.text()
        land= self.countries.currentText()
        f = open("output.txt","w",encoding="utf-8")
        f.write(f"{vorname},{name},{geburtsdatum.day}/{geburtsdatum.month}/{geburtsdatum.year},{adresse},{plz},{ort},{land}")
        f.close()


def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()