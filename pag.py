import random
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow, QLabel

from PyQt5.QtGui import QPixmap

Grupa = {
    1: {
        "nosaukums": "Muse",
        "dziesmas": ["Uprising", "Hysteria", "Supermassive Black Hole", "Starlight", "Knights of Cydonia", "Madness"]
    },
    2: {
        "nosaukums": "Five Finger Death Punch",
        "dziesmas": ["Wrong Side of Heaven", "Wash It All Away", "Jekyll and Hyde", "Bad Company", "Gone Away", "Blue on Black"]
    },
    3: {
        "nosaukums": "Slipknot",
        "dziesmas": ["Duality", "Before I Forget", "Psychosocial", "Wait and Bleed", "Unsainted", "Spit It Out"]
    },
    4: {
        "nosaukums": "Limp Bizkit",
        "dziesmas": ["Rollin’", "Break Stuff", "My Way", "Take a Look Around", "Behind Blue Eyes", "Nookie"]
    },
    5: {
        "nosaukums": "The Smashing Pumpkins",
        "dziesmas": ["1979", "Tonight, Tonight", "Bullet with Butterfly Wings", "Disarm", "Today", "Cherub Rock"]
    },
    6: {
        "nosaukums": "Pink Floyd",
        "dziesmas": ["Comfortably Numb", "Wish You Were Here", "Another Brick in the Wall", "Time", "Shine On You Crazy Diamond", "Money"]
    }
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Muzika")
        self.setGeometry(100, 100, 600, 400)
        self.bildes()
    
    def bildes(self):
        for i in range(1, 7):
            if(i<=3):
                nosaukums = Grupa[i]["nosaukums"]
                grupa = QLabel(self)
                grupa.setGeometry(10, (i-1)* 100, 200, 100)  # Pielāgots novietojums
                cels = os.path.join("/Users/danielseriks/Documents/Skolas darbi/VC CODE/PYTHON/PYTHON_PROJECT", f"{nosaukums}.png")
                
                if os.path.exists(cels):
                    bilde = QPixmap(cels)
                    grupa.setPixmap(bilde)
                    grupa.setScaledContents(True)
                else:
                    grupa.setText(nosaukums)
                
                grupa.show()
                # parada kura grupa tika izvēlēta
                checkbox = QLabel(self)
                checkbox.setGeometry(220,(i-1)* 100,100,100)
                checkbox_cels = os.path.join("/Users/danielseriks/Documents/Skolas darbi/VC CODE/PYTHON/PYTHON_PROJECT/kaulins",f"{i}.jpg")
                checkbox_bilde = QPixmap(checkbox_cels)
                checkbox.setPixmap(checkbox_bilde)
                grupa.setScaledContents(True)

            else:
                nosaukums = Grupa[i]["nosaukums"]
                grupa = QLabel(self)
                grupa.setGeometry(300, (i-4)* 100, 200, 100)  # Pielāgots novietojums
                cels = os.path.join("/Users/danielseriks/Documents/Skolas darbi/VC CODE/PYTHON/PYTHON_PROJECT", f"{nosaukums}.png")
                
                if os.path.exists(cels):
                    bilde = QPixmap(cels)
                    grupa.setPixmap(bilde)
                    grupa.setScaledContents(True)
                else:
                    grupa.setText(nosaukums)
                
                grupa.show()

                checkbox = QLabel(self)
                checkbox.setGeometry(500,(i-4)* 100,100,100)
                checkbox_cels = "/Users/danielseriks/Documents/Skolas darbi/VC CODE/PYTHON/PYTHON_PROJECT/zalais.png"
                checkbox_bilde = QPixmap(checkbox_cels)
                checkbox.setPixmap(checkbox_bilde)
                grupa.setScaledContents(True)
     # Create a button
        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(10,300,100,100)
        # Connect button to a function
        self.button.clicked.connect(self.on_button_click)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_button_click(self):
        print("Button clicked!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# Mūzikas izvēle
random.seed()
grupa_izveleta = random.randint(1, 6)
dziesma_izveleta = random.randint(0, 5)

izveleta_nosaukums = Grupa[grupa_izveleta]["nosaukums"]
izveleta_dziesma = Grupa[grupa_izveleta]["dziesmas"][dziesma_izveleta]

print(f"Tava izvēlētā grupa: {izveleta_nosaukums}")
print(f"Tava izvēlētā dziesma: {izveleta_dziesma}")

jau = os.getcwd()
PATH = os.path.join(jau, "PYTHON_PROJECT", "Muzika", izveleta_nosaukums)
os.chdir(PATH)
print(os.getcwd())