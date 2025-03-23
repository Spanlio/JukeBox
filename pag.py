import random
import os
import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

dir = os.getcwd()

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
            item.widget().setParent(None)

class SakumaEkrans(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sākums")
        self.setGeometry(100, 100, 400, 300)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.turpinat = QPushButton("Turpināt", self)
        self.turpinat.clicked.connect(self.parada_galveno)
        self.layout.addWidget(self.turpinat)

        self.iziet = QPushButton("Iziet", self)
        self.iziet.clicked.connect(self.close)
        self.layout.addWidget(self.iziet)

        self.galvenais_ekrans = None

    def parada_galveno(self):
        if not self.galvenais_ekrans:
            self.galvenais_ekrans = GalvenaisEkrans()
        self.galvenais_ekrans.show()
        self.hide()

class GalvenaisEkrans(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mūzika")
        self.setGeometry(100, 100, 500, 500)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.tokeni = 3
        self.init_ui()

    def init_ui(self):
        self.tokeni_label = QLabel(f"Atlikušie kredīti: {self.tokeni}")
        self.layout.addWidget(self.tokeni_label)

        self.button = QPushButton("Mest kauliņu", self)
        self.button.clicked.connect(self.mest_kaulinu_grupa)
        self.layout.addWidget(self.button)

    def mest_kaulinu_grupa(self):
        clear_layout(self.layout)
        grupas_indekss = random.randint(1, 6)
        self.izveleta_grupa = Grupa[grupas_indekss]["nosaukums"]
        self.result_label = QLabel(f"Tava izvēlētā grupa: {self.izveleta_grupa}")
        self.layout.addWidget(self.result_label)

        self.button = QPushButton("Mest kauliņu vēlreiz, lai izvēlētos dziesmu")
        self.button.clicked.connect(lambda: self.mest_kaulinu_dziesma(grupas_indekss))
        self.layout.addWidget(self.button)

    def mest_kaulinu_dziesma(self, grupas_indekss):
        clear_layout(self.layout)
        dziesmas_indekss = random.randint(0, 5)
        self.izveleta_dziesma = Grupa[grupas_indekss]["dziesmas"][dziesmas_indekss]
        self.result_label = QLabel(f"Tava izvēlētā dziesma: {self.izveleta_dziesma}")
        self.layout.addWidget(self.result_label)
        self.atskano()

    def atskano(self):
        dziesmas_cels = os.path.join(dir, "Muzika", self.izveleta_grupa, f"{self.izveleta_dziesma}.wav")
        if os.path.exists(dziesmas_cels):
            pygame.mixer.init()
            pygame.mixer.music.load(dziesmas_cels)
            pygame.mixer.music.play()
            self.tokeni -= 1
            self.tokeni_label.setText(f"Atlikušie kredīti: {self.tokeni}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    logs = SakumaEkrans()
    logs.show()
    app.aboutToQuit.connect(pygame.quit)
    sys.exit(app.exec_())
