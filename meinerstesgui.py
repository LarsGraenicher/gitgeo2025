import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        editmenu = menubar.addMenu("Edit")
        viewmenu = menubar.addMenu("View")

        open = QAction("Open", self)
        open.triggered.connect(self.menu_open)
        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)

        quit.setMenuRole(QAction.QuitRole) #für MAC

        filemenu.addAction(open)
        filemenu.addAction(save)
        filemenu.addAction(quit)

    def menu_open(self):
        pass
    def menu_save(self):
        pass
    def menu_quit(self):
        print("Quit")
        self.close()

    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Mein erstes GUI")
        ### LAYOUT WÄHLEN:
        layout = QVBoxLayout()
        #self.setMinimumSize(1200,400)
        #self.setMinimumHeight(1200)
        #self.setMinimumWidth(800)

        button1 = QPushButton("Button1")
        button2= QPushButton("Button2")

        layout.addWidget(button1)
        layout.addWidget(button2)
    





        #Grid Layout
        #nameLabel= QLabel("Name: ")
        #nameLine = QLineEdit()
        #adressLabel = QLabel("Adresse: ")
        #adressText = QTextEdit()
        #layout.addWidget(nameLabel,0,0)
        #layout.addWidget(nameLine,0,1)
        #layout.addWidget(adressLabel,1,0)
        #layout.addWidget(adressText,1,1)

        #Form Layout
        #nameLineEdit= QLineEdit()
        #emailLineEdit= QLineEdit()
        #ageSpinBox= QSpinBox()
        #layout.addRow("Name: ", nameLineEdit)
        #layout.addRow("Email: ", emailLineEdit)
        #layout.addRow("Age: ", ageSpinBox)

        #label = QLabel("Hello")
        #layout.addWidget(label)  #Das sie angezeigt werden
     
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


        button1.clicked.connect(self.button1_clicked)
        button2.clicked.connect(self.button2_clicked)
        


    def createConnects(self):
        pass


    def button1_clicked(self):
        print("Button1 wurde gedrückt")

    def button2_clicked(self):
        print("Button2 wurde gedrückt")

def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()