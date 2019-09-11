import sys
import random
import string
import hangmanqt
from PyQt5.QtWidgets import QMessageBox, QApplication, QSplitter, QWidget, QToolTip, QPushButton, QDesktopWidget, QLabel, QFrame, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont, QPainter, QBrush, QColor, QPixmap, QImage, QPen
from PyQt5.QtCore import Qt, QRect, QLine, QLineF, QPoint

class App(QWidget):
    lbls = []
    letters = []
    pad = 0
    word = ""
    count = 0
    i = 0
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
       self.setFixedSize(800, 600)
       self.centre()
       self.setWindowTitle("Hangman")
       self.setWindowIcon(QIcon("ya.png"))
       self.labels()       
       self.buttons()
       self.show() 
       self.center = QPoint()
       self.rad = 50
      
       self.lines = []

    def paintEvent(self, event):
        lin = [QLineF(400, 150, 770, 150)]
        QWidget.paintEvent(self, event)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.darkYellow, 6))
        painter.drawLines(ln for ln in lin)
        painter.setPen(QPen(Qt.lightGray, 6))
        painter.drawLines(el for el in self.lines)
        if not self.center.isNull():
            painter.drawEllipse(self.center, self.rad, self.rad)

    def labels(self):
        self.word = hangmanqt.getWord()
        length = self.word.__len__()
        self.pad = szh = 120
        sz = 720/length
        if sz > szh:
            sz = szh
        mv = (780 - (sz+3)*length)/2
        mvy = 10
        for i in range(length):
            lbl = QPushButton(self)
            lbl.setDisabled(True)
            #lbl.setFont(QFont("Consolas", 35))
            lbl.setStyleSheet("""QPushButton{
            background-color: white;
            color: darkgray;
            border: 0px outset;
            border-color: black;
            border-radius: 10px;
            font-size: 30pt;
            }""")
            lbl.resize(sz, szh)
            lbl.move(mv, mvy)
            mv+=sz+5
            self.lbls.append(lbl)
            lbl.show()

    def buttons(self):
        letters = list(string.ascii_lowercase + "-")
        sz = 70
        mvy = self.pad + 25
        mv = 5
        for i in range(letters.__len__()):
            btn = QPushButton(letters[i], self)
            btn.resize(sz, sz)
            btn.move(mv, mvy)
            btn.setStyleSheet("""QPushButton{
                background-color: white;
                text-align: center;
                color: darkgray;
                border: 3px solid;
                border-color: lightgray;
                border-radius: 10px;
                font-size: 30px;
                text-align: center;
                }
                QPushButton:hover{
                background-color: lightgray;
                }""")
            mv+=sz+5
            if mv > 350:
                mv = 5
                if mvy > 450:
                    mv=sz+10
                mvy+=sz+5
            btn.show()
            #btn.clicked.connect(self.draw)
            btn.clicked.connect(self.buttonClicked)

    def draw(self):
        lines = [QLineF(600, 160, 600, 200), QLineF(600, 300 ,600, 310), QLineF(600, 310, 600, 450), QLineF(600, 310, 500, 370), QLineF(600, 310, 700, 370), QLineF(600, 450, 510, 550), QLineF(600, 450, 690, 550)]
        if self.i == 1:
            self.center = QPoint(600, 250)
        self.lines.append(lines[self.i])
        self.i+=1
        self.update()
        if self.i == 7:
            num = 0
            for i in self.lbls:
                i.setText(self.word[num])
                num+=1
            buttonReply = QMessageBox.question(self, 'Game over!', "You lose...\nRight answer: {}".format(self.word.upper()), QMessageBox.Ok)
            if buttonReply == QMessageBox.Ok:
                self.close()                

    def buttonClicked(self):
        sender = self.sender()
        sender.setStyleSheet("""QPushButton{
            background-color: darksalmon;
            text-align: center;
            color: darkgray;
            border: 3px solid;
            border-color: lightgray;
            border-radius: 10px;
            font-size: 30px;
            padding: 10%;
            }""")
        sender.setDisabled(True)
        numbers = hangmanqt.play(self.word, sender.text())
        if numbers.__len__() == 0:
            self.draw()
        else:
            for i in numbers:
                self.lbls[i].setText(self.word[i])
                self.letters.append(i)
                self.letters.sort()
                if self.letters.__len__() == self.lbls.__len__():
                    buttonReply = QMessageBox.question(self, 'Game over!', "You win!", QMessageBox.Ok)
                    if buttonReply == QMessageBox.Ok:
                        self.close()
        
        
    def centre(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    

def main():
    app = QApplication(sys.argv)
    ex = App()    
    app.exec_()

if __name__ == "__main__":
    main()
    

    