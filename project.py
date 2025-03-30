import random
import os
import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

direktorijs = os.getcwd()

#gruopas un to dziesmas
Grupa = {
    1: {"nosaukums": "Muse", "dziesmas": ["Uprising", "Hysteria", "Supermassive Black Hole", "Starlight", "Knights of Cydonia", "Madness"]},
    2: {"nosaukums": "Five Finger Death Punch", "dziesmas": ["Wrong Side of Heaven", "Wash It All Away", "Jekyll and Hyde", "Bad Company", "Gone Away", "Blue on Black"]},
    3: {"nosaukums": "Slipknot", "dziesmas": ["Duality", "Before I Forget", "Psychosocial", "Wait and Bleed", "Unsainted", "Spit It Out"]},
    4: {"nosaukums": "Limp Bizkit", "dziesmas": ["Rollin’", "Break Stuff", "My Way", "Take a Look Around", "Behind Blue Eyes", "Nookie"]},
    5: {"nosaukums": "The Smashing Pumpkins", "dziesmas": ["1979", "Tonight, Tonight", "Bullet with Butterfly Wings", "Disarm", "Today", "Cherub Rock"]},
    6: {"nosaukums": "Pink Floyd", "dziesmas": ["Comfortably Numb", "Wish You Were Here", "Another Brick in the Wall", "Time", "Shine On You Crazy Diamond", "Money"]}
}

def clear_layout(izkartojums):
    while izkartojums.count():
        item = izkartojums.takeAt(0)
        if item.widget():
            item.widget().deleteLater()

def saglabat_statistiku(grupa, dziesma):
    faila_nosaukums = "statistika.txt"
    try:
        
        with open(faila_nosaukums, "a", encoding="utf-8") as fails:
            fails.write(f"Izvēlēta grupa: {grupa} | Dziesma: {dziesma}\n")
            
    except Exception as e:
        print(f"Kļūda ar statistik")

class AutoriLogs(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Autori")
        self.setGeometry(150, 150, 300, 200)
        self.setStyleSheet("background-color: #1e1e1e;")


        izkartojums = QVBoxLayout()
        self.setLayout(izkartojums)
        
#autors
        autors = QLabel("Autors: Ēriks")
        autors.setStyleSheet("background-color: 1e1e1e; color: white;"
                                    "font-size: 18px; font-weight: bold;")
        izkartojums.addWidget(autors)

        aizvert_poga = QPushButton("Aizvērt")
        aizvert_poga.setStyleSheet("background-color: red; color: white;text-weight: bold")
        aizvert_poga.clicked.connect(self.close)
        izkartojums.addWidget(aizvert_poga)

class izvele(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Izvele")
        self.setGeometry(150, 150, 300, 200)
        self.setStyleSheet("background-color: #1e1e1e;")

        self.izkartojums = QHBoxLayout()  # Use a vertical layout
        self.setLayout(self.izkartojums)

        self.ja_poga = QPushButton("Iet uz galveno ekrānu", self)
        self.ja_poga.setStyleSheet("background-color: GREEN; color: white;")
        self.ja_poga.clicked.connect(self.iet_uz_galveno_ekranu)  # Connect to go to main screen
        self.ja_poga.setFixedHeight(50)

        self.ne_poga = QPushButton("Atgriezties sākuma ekrānā", self)
        self.ne_poga.setStyleSheet("background-color: RED; color: white;")
        self.ne_poga.clicked.connect(self.iet_uz_sakuma_ekranu)  # Connect to go to Sakuma_ekrans
        self.ne_poga.setFixedHeight(50)

        self.izkartojums.addWidget(self.ja_poga)
        self.izkartojums.addWidget(self.ne_poga)

    def iet_uz_galveno_ekranu(self):
        self.close()
        self.galvenais_ekrans = Galvenais_Ekraans()
        self.galvenais_ekrans.show()
    def iet_uz_sakuma_ekranu(self):
        self.close()
        self.sakuma_ekrans = Sakuma_ekrans()
        self.sakuma_ekrans.show()


class NoteikumuLogs(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Noteikumi")
        self.setGeometry(150, 150, 600, 500)
        self.setStyleSheet("background-color: #1e1e1e;")


        izkartojums = QVBoxLayout()
        self.setLayout(izkartojums)

        Noteikumi = QLabel("""<font color="red">Spēles noteikumi :</font>
                <br><font color="yellow">1.</font> Sākumā spied "Turpināt", lai nonāktu spēles galvenajā ekrānā.
                <br><font color="yellow">2.</font> Spied pogu "Mest kauliņu", lai nejauši izvēlētos kādu no sešām grupām.
                <br><font color="yellow">3.</font> Kad grupa ir izvēlēta, spied pogu Mest kauliņu vēlreiz, lai nejauši izvēlētos vienu no sešām dziesmām šajā grupā.
                <br><font color="yellow">4.</font> Kad dziesma ir izvēlēta, tā tiek parādīta ekrānā, un tu vari to atskaņot, nospiežot pogu Atskaņot dziesmu.
                <br><font color="yellow">5.</font> Ja vēlies, vari apturēt vai turpināt mūzikas atskaņošanu ar atbilstošajām pogām.
                <br><font color="yellow">6.</font> Ja gribi izvēlēties jaunu dziesmu, spied "IZLAIST", lai atgrieztos sākumā un sāktu no jauna.
                <br><font color="yellow">7.</font> Visa tava izvēlētā mūzika tiek saglabāta statistikā, lai vēlāk varētu redzēt, ko esi klausījies!""")


        Noteikumi.setStyleSheet("background-color: 1e1e1e; color: white;"
                                    "font-size: 18px; font-weight: bold;")
        izkartojums.addWidget(Noteikumi)

        aizvert_poga = QPushButton("Aizvērt")
        aizvert_poga.setStyleSheet("background-color: red; color: white; text-weight: bold")
        aizvert_poga.clicked.connect(self.close)
        izkartojums.addWidget(aizvert_poga)


class Sakuma_ekrans(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sakuma")
        self.setGeometry(100, 100, 400, 300)
        app.setStyleSheet("QMainWindow { background-color: #1e1e1e; }")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.izkartojums = QVBoxLayout()  # Vertikālais izkārtojums
        self.central_widget.setLayout(self.izkartojums)


        # Izveido pogas
        self.turpinat = QPushButton("Turpināt", self)
        self.turpinat.clicked.connect(self.Parada_Galveno)
        self.turpinat.setStyleSheet("background-color: GREEN; color: white;")
        self.izkartojums.addWidget(self.turpinat)

        self.autori = QPushButton("Autori", self)
        self.autori.clicked.connect(self.Parada_autorus)
        self.autori.setStyleSheet("background-color: YELLOW; color: black;")
        self.izkartojums.addWidget(self.autori)


        self.Noteikumi = QPushButton("Noteikumi", self)
        self.Noteikumi.clicked.connect(self.Parada_noteikumus)
        self.Noteikumi.setStyleSheet("background-color: blue; color: white;")
        self.izkartojums.addWidget(self.Noteikumi)

        self.iziet = QPushButton("Iziet", self)
        self.iziet.clicked.connect(self.close)
        self.iziet.setStyleSheet("background-color: red; color: white;")
        self.izkartojums.addWidget(self.iziet)

        self.Galvenais_Ekraans = None
        self.AutoruLogs = None
        self.NoteikumuLogs = None
        
#funkcijas, kas parada noteikumu, autoru logus un galveno ekranu
    def Parada_autorus(self):
        if self.AutoruLogs is None or not self.AutoruLogs.isVisible():
            self.AutoruLogs = AutoriLogs()
            self.AutoruLogs.show()

    def Parada_noteikumus(self):
        if self.NoteikumuLogs is None or not self.NoteikumuLogs.isVisible():
            self.NoteikumuLogs = NoteikumuLogs()
            self.NoteikumuLogs.show()

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
        self.izkartojums = QVBoxLayout() 
        self.central_widget.setLayout(self.izkartojums)

        self.setStyleSheet("background-color: #1e1e1e;")

        self.izveleta_grupa = None
        self.izveleta_dziesma = None
        self.izvele = None

        # no sakuma paslepj galveno ekranu
        self.init_ui()
        self.sakuma_ekrans = Sakuma_ekrans()


        # IZVEIDO POGAS TAA LAI NEBUTU KATRU REIZI VINAS JATAISA

        self.stop_poga = QPushButton("Apturēt mūziku", self)
        self.stop_poga.setStyleSheet("background-color: yellow;")
        self.stop_poga.clicked.connect(lambda: pygame.mixer.music.pause())
        self.stop_poga.hide()

        self.poga_atsaakt = QPushButton("Turpināt mūziku", self)
        self.poga_atsaakt.setStyleSheet("background-color: green;")
        self.poga_atsaakt.clicked.connect(lambda: pygame.mixer.music.unpause())
        self.poga_atsaakt.hide()

        self.iziesanas_poga = QPushButton("IZLAIST", self)
        self.iziesanas_poga.setStyleSheet("background-color: red; color: white;")
        self.iziesanas_poga.clicked.connect(self.parada_izveli)
        self.iziesanas_poga.hide()
#nesies atpakall
    def back_to_the_lobby(self):
        self.close()
        self.sakuma_ekrans.show()
    def parada_izveli(self):
            if self.izvele is None or not self.izvele.isVisible():
                self.close()
                self.izvele = izvele()
                self.izvele.show()

        
    
    def init_ui(self):
        self.kaulin_poga = QLabel("Izvēlies grupu, metot kauliņu!", self)
        self.kaulin_poga.setStyleSheet("font-size: 18px; font-weight: bold; color: red;")
        self.izkartojums.addWidget(self.kaulin_poga)

        for i in range(1, 7):
            #saliek bild un nosaukumus viertikal viens pec otra
            grupa_nosaukums = Grupa[i]["nosaukums"]
            grupa_labels = QLabel(grupa_nosaukums, self)
            grupa_labels.setStyleSheet("color: white;")
            self.izkartojums.addWidget(grupa_labels)
            
            attela_cels = os.path.join(direktorijs, f"{grupa_nosaukums}.png")
            if os.path.exists(attela_cels):
                bilde = QPixmap(attela_cels)
                bilde = bilde.scaled(200, 75, Qt.KeepAspectRatio)
                attela_labels = QLabel(self)
                attela_labels.setPixmap(bilde)
                self.izkartojums.addWidget(attela_labels)
        
        self.button = QPushButton("Mest kauliņu", self)
        self.button.setStyleSheet("background-color: GREEN; color: white;font-weight: bold;")
        self.button.clicked.connect(self.mest_kaulinu_grupa)
        self.izkartojums.addWidget(self.button)
    
    def mest_kaulinu_grupa(self):
        clear_layout(self.izkartojums)

        grupas_indekss = random.randint(1, 6)
        self.izveleta_grupa = Grupa[grupas_indekss]["nosaukums"]
        self.kaulin_poga = QLabel(f"Tava izvēlētā grupa: {self.izveleta_grupa}", self)
        self.kaulin_poga.setStyleSheet("font-size: 18px; font-weight: bold; color: red;")
        self.izkartojums.addWidget(self.kaulin_poga)
        
        for dziesma in Grupa[grupas_indekss]["dziesmas"]:
            dziesma_label = QLabel(dziesma, self)
            dziesma_label.setStyleSheet("color: white; font-size: 25px;font-weight: bold;")
            self.izkartojums.addWidget(dziesma_label)
        
        self.button = QPushButton("Mest kauliņu vēlreiz, lai izvēlētos dziesmu", self)
        self.button.setStyleSheet("background-color: GREEN; color: white;font-weight: bold;")
        self.button.clicked.connect(lambda: self.mest_kaulinu_dziesma(grupas_indekss))
        self.izkartojums.addWidget(self.button)
    
    def mest_kaulinu_dziesma(self, grupa_izveleta):

        clear_layout(self.izkartojums)
        
        dziesmas_indekss = random.randint(0, 5)
        self.izveleta_dziesma = Grupa[grupa_izveleta]["dziesmas"][dziesmas_indekss]
        self.kaulin_poga = QLabel(f"Tava izvēlētā dziesma: {self.izveleta_dziesma}", self)
        self.izkartojums.addWidget(self.kaulin_poga)
        
        saglabat_statistiku(self.izveleta_grupa, self.izveleta_dziesma)

        self.muzikas_bilde()
        self.Atskano()
    
    def muzikas_bilde(self):

        if self.izkartojums.count() > 0:
            clear_layout(self.izkartojums)

        attela_cels = os.path.join(direktorijs, f"{self.izveleta_grupa}.png")
        
        self.izveleta_dziesma_labels = QLabel(f"Tava izvēlētā dziesma: {self.izveleta_dziesma}", self)
        self.izveleta_dziesma_labels.setAlignment(Qt.AlignCenter)
        self.izveleta_dziesma_labels.setStyleSheet("""
            color: white;font-size: 25px;font-weight: bold;
            border: 3px solid yellow;background-color: black;""")
        self.izkartojums.addWidget(self.izveleta_dziesma_labels)


        bilde = QPixmap(attela_cels)
        bilde = bilde.scaled(500, 440, Qt.KeepAspectRatio)
        attela_labels = QLabel(self)
        attela_labels.setPixmap(bilde)
        self.izkartojums.addWidget(attela_labels)

        

        self.stop_poga.show()
        self.poga_atsaakt.show()
        self.iziesanas_poga.show()

        self.izkartojums.addWidget(self.poga_atsaakt)
        self.izkartojums.addWidget(self.stop_poga)
        self.izkartojums.addWidget(self.iziesanas_poga)

    def Atskano(self):
        dziesmas_cels = os.path.join(direktorijs, "Muzika", f"{self.izveleta_grupa}", f"{self.izveleta_dziesma}.wav")
        
        import unicodedata
        dziesmas_cels = unicodedata.normalize('NFC', dziesmas_cels)
        #full on chat gpt, jo izradas bija dazadi kodejumi

        if not os.path.exists(dziesmas_cels):
            print(f"Nevar atrast dziesmu: {dziesmas_cels}")
            self.poga_atsaakt.setEnabled(False)
            self.stop_poga.setEnabled(False)
            return
        
        try:
            pygame.mixer.init()
        except pygame.error as e:
            print(f"Kļūda inicializējot pygame.mixer: {e}")

        if pygame.mixer.get_init():
            pygame.mixer.music.load(dziesmas_cels)
            print(f"Atskaņo: {dziesmas_cels}")
            pygame.mixer.music.play()

            self.iziesanas_poga.clicked.connect(pygame.mixer.music.stop)
            #nomaina pogu statusu
            self.poga_atsaakt.setEnabled(False)
            self.stop_poga.setEnabled(True)

            if not hasattr(self, 'exit_connected'):
                self.iziesanas_poga.clicked.connect(pygame.mixer.music.stop)
                self.exit_connected = True  # Marķē, ka piesaiste veikta


            def updatot_pogas():
                if pygame.mixer.music.get_busy():
                    self.poga_atsaakt.setEnabled(True)
                    self.stop_poga.setEnabled(True)
                else:
                    self.poga_atsaakt.setEnabled(False)
                    self.stop_poga.setEnabled(False)
                    self.parada_izveli()

            QTimer.singleShot(200, updatot_pogas)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    logs = Sakuma_ekrans()
    logs.show()
    app.aboutToQuit.connect(pygame.quit)
    sys.exit(app.exec_())