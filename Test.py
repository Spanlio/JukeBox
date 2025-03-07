import random
import os
import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

default_directory = os.path.dirname(os.path.abspath(__file__))  # Atrod pašreizējā skripta mapi

Grupa = {
    1: {"nosaukums": "Muse", "dziesmas": ["Uprising", "Hysteria", "Supermassive Black Hole", "Starlight", "Knights of Cydonia", "Madness"]},
    2: {"nosaukums": "Five Finger Death Punch", "dziesmas": ["Wrong Side of Heaven", "Wash It All Away", "Jekyll and Hyde", "Bad Company", "Gone Away", "Blue on Black"]},
    3: {"nosaukums": "Slipknot", "dziesmas": ["Duality", "Before I Forget", "Psychosocial", "Wait and Bleed", "Unsainted", "Spit It Out"]},
    4: {"nosaukums": "Limp Bizkit", "dziesmas": ["Rollin’", "Break Stuff", "My Way", "Take a Look Around", "Behind Blue Eyes", "Nookie"]},
    5: {"nosaukums": "The Smashing Pumpkins", "dziesmas": ["1979", "Tonight, Tonight", "Bullet with Butterfly Wings", "Disarm", "Today", "Cherub Rock"]},
    6: {"nosaukums": "Pink Floyd", "dziesmas": ["Comfortably Numb", "Wish You Were Here", "Another Brick in the Wall", "Time", "Shine On You Crazy Diamond", "Money"]}
}

def clear_layout(layout):
    """Clear all widgets in a layout."""
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            item.widget().setParent(None)  # Remove widget from layout
            del item

class Galvenais_Ekraans(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mūzika")
        self.setGeometry(100, 100, 500, 500)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout() 
        self.central_widget.setLayout(self.layout)

        self.PLAYbutton = QPushButton("Atskaņot dziesmu", self)
        self.PLAYbutton.clicked.connect(self.Atskano)
        self.PLAYbutton.hide()

        self.STOPbutton = QPushButton("Apturēt mūziku", self)
        self.STOPbutton.clicked.connect(lambda: pygame.mixer.music.pause())
        self.STOPbutton.hide()

        self.RESUMEbutton = QPushButton("Turpināt mūziku", self)
        self.RESUMEbutton.clicked.connect(lambda: pygame.mixer.music.unpause())
        self.RESUMEbutton.hide()

        self.init_ui()

    def init_ui(self):
        """Set up UI with labels for groups and their songs."""
        self.result_label = QLabel("Izvēlies grupu, metot kauliņu!", self)
        self.layout.addWidget(self.result_label)

        for i in range(1, 7):
            grupa_nosaukums = Grupa[i]["nosaukums"]
            grupa_label = QLabel(grupa_nosaukums, self)
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
        """Choose a random group and display songs."""
        clear_layout(self.layout)

        grupas_indekss = random.randint(1, 6)
        self.izveleta_grupa = Grupa[grupas_indekss]["nosaukums"]
        self.result_label = QLabel(f"Tava izvēlētā grupa: {self.izveleta_grupa}", self)
        self.layout.addWidget(self.result_label)

        for dziesma in Grupa[grupas_indekss]["dziesmas"]:
            dziesma_label = QLabel(dziesma, self)
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
        """Choose a random song for the selected group."""
        clear_layout(self.layout)

        dziesmas_indekss = random.randint(0, 5)
        self.izveleta_dziesma = Grupa[grupa_izveleta]["dziesmas"][dziesmas_indekss]
        self.result_label = QLabel(f"Tava izvēlētā dziesma: {self.izveleta_dziesma}", self)
        self.layout.addWidget(self.result_label)

        self.muzikas_bilde()
        self.Atskano()

    def muzikas_bilde(self):
        """Show image and music controls."""
        attela_cels = os.path.join(dir, f"{self.izveleta_grupa}.png")

        bilde = QPixmap(attela_cels)
        bilde = bilde.scaled(500, 440, Qt.KeepAspectRatio)
        attela_label = QLabel(self)
        attela_label.setPixmap(bilde)
        self.layout.addWidget(attela_label)

        self.layout.addWidget(self.PLAYbutton)
        self.layout.addWidget(self.STOPbutton)
        self.layout.addWidget(self.RESUMEbutton)

        self.PLAYbutton.show()
        self.STOPbutton.show()
        self.RESUMEbutton.show()

    def Atskano(self):
        """Play the chosen song."""
        dziesmas_cels = os.path.join(dir, "Muzika", f"{self.izveleta_grupa}", f"{self.izveleta_dziesma}.wav")

        if os.path.exists(dziesmas_cels):
            pygame.mixer.init()
            pygame.mixer.music.load(dziesmas_cels)
            pygame.mixer.music.play()
            print(f"Atskaņo: {dziesmas_cels}")
            pygame.time.delay(500)

            if pygame.mixer.music.get_busy():
                self.RESUMEbutton.setEnabled(True)
                self.STOPbutton.setEnabled(True)
            else:
                self.RESUMEbutton.setEnabled(False)
                self.STOPbutton.setEnabled(False)
