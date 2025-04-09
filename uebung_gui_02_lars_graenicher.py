import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import datetime
import os
import urllib.parse 
import csv

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        save = QAction("Save", self)
        save.triggered.connect(self.savebutton_clicked)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)
        load= QAction("Load", self)
        load.triggered.connect(self.loadbutton_clicked)
        filemenu2 = menubar.addMenu("View")
        view = QAction("View", self)
        view.triggered.connect(self.showoncardbutton_clicked)

        quit.setMenuRole(QAction.QuitRole) #für MAC

        filemenu.addAction(save)
        filemenu.addAction(quit)
        filemenu.addAction(load)
        filemenu2.addAction(view)



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
        self.showoncardbutton = QPushButton("Auf Karte zeigen")
        self.showoncardbutton.clicked.connect(self.showoncardbutton_clicked)
        self.loadbutton = QPushButton("Laden")
        self.loadbutton.clicked.connect(self.loadbutton_clicked)

        
        layout.addRow(self.showoncardbutton)
        layout.addRow(self.loadbutton)
        layout.addRow(self.savebutton)
        
    

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        

        self.show()



    def savebutton_clicked(self):
        filename, filter = QFileDialog.getSaveFileName(self, 
                                                        "Datei speichern", 
                                                        "", 
                                                        "Text (*.txt)") 
        print(filename, filter)
        vorname = self.vornameLineEdit.text()
        name = self.nameLineEdit.text()
        geburtsdatum = self.datumLineEdit.text()
        adresse= self.adresseLineEdit.text()
        plz= self.plzLineEdit.text()
        ort= self.ortLineEdit.text()
        land= self.countries.currentText()
        f = open(f"{filename}","w",encoding="utf-8")
        f.write(f"{vorname},{name},{geburtsdatum},{adresse},{plz},{ort},{land}")
        f.close()

    def showoncardbutton_clicked(self):
        adresse= urllib.parse.quote(self.adresseLineEdit.text())
        plz= urllib.parse.quote(self.plzLineEdit.text())
        ort= urllib.parse.quote(self.ortLineEdit.text())  
        land= urllib.parse.quote(self.countries.currentText()) 

        
        link = f"https://www.google.ch/maps/place/{adresse}+{plz}+{ort}+{land}" 

        QDesktopServices.openUrl(QUrl(link))

    def loadbutton_clicked(self):
        filename, filter = QFileDialog.getOpenFileName(self, 
                                                        "Datei öffnen", 
                                                        "C:/data/", 
                                                        "Text (*.txt *.csv)") 

        f= open(f"{filename}", "r",encoding="utf-8")
        for line in f:
            self.personendaten= line.split(",")
            print(self.personendaten[2])
        self.vornameLineEdit.setText(self.personendaten[0])
        self.nameLineEdit.setText(self.personendaten[1])
        dformat = QLocale().dateFormat(format=QLocale.FormatType.ShortFormat)
        self.datumLineEdit.setDate(QDate.fromString(self.personendaten[2], dformat))
        self.adresseLineEdit.setText(self.personendaten[3])
        self.plzLineEdit.setText(self.personendaten[4])
        self.ortLineEdit.setText(self.personendaten[5])
        self.countries.setCurrentText(self.personendaten[6])
        
        f.close()


def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()