import random
import os
import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

dir = os.getcwd()  # Atrod pašreizējā skripta mapi


Grupa = {
    1: {"nosaukums": "Muse", "dziesmas": ["Uprising", "Hysteria", "Supermassive Black Hole", "Starlight", "Knights of Cydonia", "Madness"]},
    2: {"nosaukums": "Five Finger Death Punch", "dziesmas": ["Wrong Side of Heaven", "Wash It All Away", "Jekyll and Hyde", "Bad Company", "Gone Away", "Blue on Black"]},
    3: {"nosaukums": "Slipknot", "dziesmas": ["Duality", "Before I Forget", "Psychosocial", "Wait and Bleed", "Unsainted", "Spit It Out"]},
    4: {"nosaukums": "Limp Bizkit", "dziesmas": ["Rollin’", "Break Stuff", "My Way", "Take a Look Around", "Behind Blue Eyes", "Nookie"]},
    5: {"nosaukums": "The Smashing Pumpkins", "dziesmas": ["1979", "Tonight, Tonight", "Bullet with Butterfly Wings", "Disarm", "Today", "Cherub Rock"]},
    6: {"nosaukums": "Pink Floyd", "dziesmas": ["Comfortably Numb", "Wish You Were Here", "Another Brick in the Wall", "Time", "Shine On You Crazy Diamond", "Money"]}
}

def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()


class AutoriLogs(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Autori")
        self.setGeometry(150, 150, 300, 200)
        self.setStyleSheet("background-color: #1e1e1e;")


        layout = QVBoxLayout()
        self.setLayout(layout)

        autors_label = QLabel("Autors: Ēriks")
        autors_label.setStyleSheet("background-color: 1e1e1e; color: white;"
                                    "font-size: 18px; font-weight: bold;")
        layout.addWidget(autors_label)

        aizvert_poga = QPushButton("Aizvērt")
        aizvert_poga.setStyleSheet("background-color: BLACK; color: white;")
        aizvert_poga.clicked.connect(self.close)
        layout.addWidget(aizvert_poga)

class Sakuma_ekrans(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sakuma")
        self.setGeometry(100, 100, 400, 300)
        app.setStyleSheet("QMainWindow { background-color: #1e1e1e; }")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()  # Vertikālais izkārtojums
        self.central_widget.setLayout(self.layout)


        # Izveido pogas
        self.turpinat = QPushButton("Turpināt", self)
        self.turpinat.clicked.connect(self.Parada_Galveno)
        self.turpinat.setStyleSheet("background-color: GREEN; color: white;")
        self.layout.addWidget(self.turpinat)

        self.autori = QPushButton("Autori", self)
        self.autori.clicked.connect(self.Parada_autors)
        self.autori.setStyleSheet("background-color: YELLOW; color: black;")
        self.layout.addWidget(self.autori)

        self.iziet = QPushButton("Iziet", self)
        self.iziet.clicked.connect(self.close)
        self.iziet.setStyleSheet("background-color: red; color: white;")
        self.layout.addWidget(self.iziet)

        self.Galvenais_Ekraans = None
        self.AutoruLogs = None

    def Parada_autors(self):
        if self.AutoruLogs is None or not self.AutoruLogs.isVisible():
            self.AutoruLogs = AutoriLogs()
            self.AutoruLogs.show()

    def Parada_Galveno(self):
        if self.Galvenais_Ekraans is None or not self.Galvenais_Ekraans.isVisible():
            self.Galvenais_Ekraans = Galvenais_Ekraans()
            self.Galvenais_Ekraans.show()
            self.hide()
    


class Galvenais_Ekraans(QMainWindow):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Mūzika")
        self.setGeometry(100, 100, 500, 500)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout() 
        self.central_widget.setLayout(self.layout)

        # no sakuma paslepj galveno ekranu
        self.init_ui()
        self.sakuma_ekrans = Sakuma_ekrans()


        # IZVEIDO POGAS TAA LAI NEBUTU KATRU REIZI VINAS JATAISA
        self.PLAYbutton = QPushButton("Atskaņot dziesmu", self)
        self.PLAYbutton.clicked.connect(lambda: self.Atskano())
        self.PLAYbutton.hide()

        self.STOPbutton = QPushButton("Apturēt mūziku", self)
        self.STOPbutton.clicked.connect(lambda: pygame.mixer.music.pause())
        self.STOPbutton.hide()

        self.RESUMEbutton = QPushButton("Turpināt mūziku", self)
        self.RESUMEbutton.clicked.connect(lambda: pygame.mixer.music.unpause())
        self.RESUMEbutton.hide()

        self.EXITbutton = QPushButton("IZLAIST", self)
        self.EXITbutton.clicked.connect(self.back_to_the_lobby)
        self.EXITbutton.hide()

    def back_to_the_lobby(self):
        self.close()
        self.sakuma_ekrans.show()

        
    
    def init_ui(self):
        self.result_label = QLabel("Izvēlies grupu, metot kauliņu!", self)
        self.result_label.setStyleSheet("font-size: 18px; font-weight: bold; color: red;")
        self.layout.addWidget(self.result_label)
        
        for i in range(1, 7):
            grupa_nosaukums = Grupa[i]["nosaukums"]
            grupa_label = QLabel(grupa_nosaukums, self)
            grupa_label.setStyleSheet("color: white;")
            self.layout.addWidget(grupa_label)
            
            attela_cels = os.path.join(dir, f"{grupa_nosaukums}.png")
            if os.path.exists(attela_cels):
                bilde = QPixmap(attela_cels)
                bilde = bilde.scaled(200, 100, Qt.KeepAspectRatio)
                attela_label = QLabel(self)
                attela_label.setPixmap(bilde)
                self.layout.addWidget(attela_label)
        
        self.button = QPushButton("Mest kauliņu", self)
        self.button.clicked.connect(self.mest_kaulinu_grupa)
        self.layout.addWidget(self.button)
    
    def mest_kaulinu_grupa(self):
        clear_layout(self.layout)

        grupas_indekss = random.randint(1, 6)
        self.izveleta_grupa = Grupa[grupas_indekss]["nosaukums"]
        self.result_label = QLabel(f"Tava izvēlētā grupa: {self.izveleta_grupa}", self)
        self.result_label.setStyleSheet("font-size: 18px; font-weight: bold; color: red;")
        self.layout.addWidget(self.result_label)
        
        for dziesma in Grupa[grupas_indekss]["dziesmas"]:
            dziesma_label = QLabel(dziesma, self)
            dziesma_label.setStyleSheet("color: white;")
            self.layout.addWidget(dziesma_label)
            
        attela_cels = os.path.join(dir, f"{self.izveleta_grupa}.png")
        if os.path.exists(attela_cels):
            bilde = QPixmap(attela_cels)
            bilde = bilde.scaled(200, 100, Qt.KeepAspectRatio)
            attela_label = QLabel(self)
            attela_label.setPixmap(bilde)
            self.layout.addWidget(attela_label)
        
        self.button = QPushButton("Mest kauliņu vēlreiz, lai izvēlētos dziesmu", self)
        self.button.clicked.connect(lambda: self.mest_kaulinu_dziesma(grupas_indekss))
        self.layout.addWidget(self.button)
    
    def mest_kaulinu_dziesma(self, grupa_izveleta):

        clear_layout(self.layout)
        
        dziesmas_indekss = random.randint(0, 5)
        self.izveleta_dziesma = Grupa[grupa_izveleta]["dziesmas"][dziesmas_indekss]
        self.result_label = QLabel(f"Tava izvēlētā dziesma: {self.izveleta_dziesma}", self)
        self.layout.addWidget(self.result_label)

        self.muzikas_bilde()
        self.Atskano()
    
    def muzikas_bilde(self):

        if self.layout.count() > 0:
            clear_layout(self.layout)

        attela_cels = os.path.join(dir, f"{self.izveleta_grupa}.png")

        bilde = QPixmap(attela_cels)
        bilde = bilde.scaled(500, 440, Qt.KeepAspectRatio)
        attela_label = QLabel(self)
        attela_label.setPixmap(bilde)
        self.layout.addWidget(attela_label)

        self.EXITbutton.setStyleSheet("background-color: red; color: white;")

        self.PLAYbutton.show()
        self.STOPbutton.show()
        self.RESUMEbutton.show()
        self.EXITbutton.show()

        self.layout.addWidget(self.PLAYbutton)
        self.layout.addWidget(self.STOPbutton)
        self.layout.addWidget(self.RESUMEbutton)
        self.layout.addWidget(self.EXITbutton)

    def Atskano(self):
        dziesmas_cels = os.path.join(dir, "Muzika", f"{self.izveleta_grupa}", f"{self.izveleta_dziesma}.wav")

        if not os.path.exists(dziesmas_cels):
            print(f"Nevar atrast dziesmu: {dziesmas_cels}")
        else:
            pygame.mixer.init()
            pygame.mixer.music.load(dziesmas_cels)
            pygame.mixer.music.play()
            print(f"Atskaņo: {dziesmas_cels}")

            if pygame.mixer.music.get_busy():
                self.PLAYbutton.setEnabled(False)
                self.RESUMEbutton.setEnabled(True)
                self.STOPbutton.setEnabled(True)
            else:
                self.RESUMEbutton.setEnabled(False)
                self.STOPbutton.setEnabled(False)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    logs = Sakuma_ekrans()
    logs.show()
    app.aboutToQuit.connect(pygame.quit)
    sys.exit(app.exec_())
