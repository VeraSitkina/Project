import sys
from random import choice
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QLCDNumber, QMessageBox
from PyQt5 import QtGui


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(200, 200, 900, 600)
        self.setMinimumSize(900, 600)
        self.setMaximumSize(900, 600)
        self.setWindowTitle('Тренажер')
        
        self.title = QLabel(self)
        self.title.setText("Тренажер по математике")
        self.title.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.title.move(330, 30)
        
        self.btn = QPushButton('Начать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(250, 80)
        self.btn.clicked.connect(self.start)
        
        self.rules = QPushButton('Правила', self)
        self.rules.resize(self.rules.sizeHint())
        self.rules.move(540, 80)
        self.rules.clicked.connect(self.info)
        
        self.end = QPushButton('Итог', self)
        self.end.resize(self.rules.sizeHint())
        self.end.move(400, 560)
        self.end.clicked.connect(self.finish)
        
        self.label1 = QLabel(self)
        self.label1.setText("Верные ответы:")
        self.label1.move(700, 250)
        self.ok1 = QLCDNumber(self)
        self.ok1.move(790, 290)
        
        self.label2 = QLabel(self)
        self.label2.setText("Ошибки:")
        self.label2.move(700, 340)
        self.ok2 = QLCDNumber(self)
        self.ok2.move(790, 370)
        
        self.x1 = QLabel(self)
        self.x1.move(40, 165)
        
        self.x2 = QLabel(self)
        self.x2.move(40, 205)
        
        self.x3 = QLabel(self)
        self.x3.move(40, 245)
        
        self.x4 = QLabel(self)
        self.x4.move(40, 285)
        
        self.x5 = QLabel(self)
        self.x5.move(40, 325)
        
        self.x6 = QLabel(self)
        self.x6.move(40, 365)
        
        self.x7 = QLabel(self)
        self.x7.move(40, 405)
        
        self.x8 = QLabel(self)
        self.x8.move(40, 445)
        
        self.x9 = QLabel(self)
        self.x9.move(40, 485)
        
        self.x10 = QLabel(self)
        self.x10.move(40, 525)
        
        self.y1 = QLineEdit(self)
        self.y1.resize(40, 30)
        self.y1.move(170, 160)
        self.xy1 = QPushButton('OK', self)
        self.xy1.resize(40, 30)
        self.xy1.move(240, 160)
        self.xy1.clicked.connect(self.go1)
        
        self.y2 = QLineEdit(self)
        self.y2.resize(40, 30)
        self.y2.move(170, 200)
        self.xy2 = QPushButton('OK', self)
        self.xy2.resize(40, 30)
        self.xy2.move(240, 200)
        self.xy2.clicked.connect(self.go2)
        
        self.y3 = QLineEdit(self)
        self.y3.resize(40, 30)
        self.y3.move(170, 240)
        self.xy3 = QPushButton('OK', self)
        self.xy3.resize(40, 30)
        self.xy3.move(240, 240)
        self.xy3.clicked.connect(self.go3)
        
        self.y4 = QLineEdit(self)
        self.y4.resize(40, 30)
        self.y4.move(170, 280)
        self.xy4 = QPushButton('OK', self)
        self.xy4.resize(40, 30)
        self.xy4.move(240, 280)
        self.xy4.clicked.connect(self.go4)
        
        self.y5 = QLineEdit(self)
        self.y5.resize(40, 30)
        self.y5.move(170, 320)
        self.xy5 = QPushButton('OK', self)
        self.xy5.resize(40, 30)
        self.xy5.move(240, 320)
        self.xy5.clicked.connect(self.go5)
        
        self.y6 = QLineEdit(self)
        self.y6.resize(40, 30)
        self.y6.move(170, 360)
        self.xy6 = QPushButton('OK', self)
        self.xy6.resize(40, 30)
        self.xy6.move(240, 360)
        self.xy6.clicked.connect(self.go6)
        
        self.y7 = QLineEdit(self)
        self.y7.resize(40, 30)
        self.y7.move(170, 400)
        self.xy7 = QPushButton('OK', self)
        self.xy7.resize(40, 30)
        self.xy7.move(240, 400)
        self.xy7.clicked.connect(self.go7)
        
        self.y8 = QLineEdit(self)
        self.y8.resize(40, 30)
        self.y8.move(170, 440)
        self.xy8 = QPushButton('OK', self)
        self.xy8.resize(40, 30)
        self.xy8.move(240, 440)
        self.xy8.clicked.connect(self.go8)
        
        self.y9 = QLineEdit(self)
        self.y9.resize(40, 30)
        self.y9.move(170, 480)
        self.xy9 = QPushButton('OK', self)
        self.xy9.resize(40, 30)
        self.xy9.move(240, 480)
        self.xy9.clicked.connect(self.go9)
        
        self.y10 = QLineEdit(self)
        self.y10.resize(40, 30)
        self.y10.move(170, 520)
        self.xy10 = QPushButton('OK', self)
        self.xy10.resize(40, 30)
        self.xy10.move(240, 520)
        self.xy10.clicked.connect(self.go10)
        
        self.z1 = QLabel(self)
        self.z1.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z1.resize(40, 40)
        self.z1.move(500, 200)
        
        self.z2 = QLabel(self)
        self.z2.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z2.resize(40, 40)
        self.z2.move(580, 240)
        
        self.z3 = QLabel(self)
        self.z3.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z3.resize(40, 40)
        self.z3.move(400, 300)
        
        self.z4 = QLabel(self)
        self.z4.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z4.resize(40, 40)
        self.z4.move(560, 300)
        
        self.z5 = QLabel(self)
        self.z5.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z5.resize(40, 40)
        self.z5.move(440, 420)
        
        self.z6 = QLabel(self)
        self.z6.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z6.resize(40, 40)
        self.z6.move(590, 370)
        
        self.z7 = QLabel(self)
        self.z7.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z7.resize(40, 40)
        self.z7.move(380, 190)
        
        self.z8 = QLabel(self)
        self.z8.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z8.resize(40, 40)
        self.z8.move(470, 320)
        
        self.z9 = QLabel(self)
        self.z9.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z9.resize(40, 40)
        self.z9.move(520, 400)
        
        self.z10 = QLabel(self)
        self.z10.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z10.resize(40, 40)
        self.z10.move(380, 380)
        
        self.z11 = QLabel(self)
        self.z11.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z11.resize(40, 40)
        self.z11.move(550, 460)
        
        self.z12 = QLabel(self)
        self.z12.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z12.resize(40, 40)
        self.z12.move(430, 240)
        
        self.z13 = QLabel(self)
        self.z13.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z13.resize(40, 40)
        self.z13.move(380, 460)
        
        self.z14 = QLabel(self)
        self.z14.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z14.resize(40, 40)
        self.z14.move(560, 150)
        
        self.z15 = QLabel(self)
        self.z15.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.z15.resize(40, 40)
        self.z15.move(440, 150)
        
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.n4 = 0
        self.n5 = 0
        self.n6 = 0
        self.n7 = 0
        self.count1 = 0
        self.count2 = 0
        self.correct = 0
        
    def info(self):
        i1 = "Вам необходимо решить 10 примеров. После решения всех примеров Вы узнаете общее количество набранных баллов."
        i2 = "Вам будут предоставлены возможность решить новые задания, либо возможность выйти из игры."
        msg = QMessageBox()
        msg.move(500, 300)
        msg.setWindowTitle("Правила игры")
        msg.setText(i1 + "\n" + i2)
        msg.exec()
        
    def finish(self):
        msg = QMessageBox()
        msg.move(600, 500)
        msg.setWindowTitle("Итог")
        msg.setText("Количество верных ответов: {}".format(self.correct))
        msg.exec()
        
    def start(self):
        array1 = list(range(2, 10))
        array2 = list(range(2, 10))
        array3 = list(range(2, 10))
        array4 = list(range(2, 10))
        array5 = list(range(0, 20))
        array6 = list(range(0, 20))
        array7 = list(range(0, 20))
        
        self.n1 = choice(array1)
        self.n2 = choice(array2)
        self.n3 = choice(array3)
        self.n4 = choice(array4)
        self.n5 = choice(array5)
        self.n6 = choice(array6)
        self.n7 = choice(array7)
        
        self.count1 = 0
        self.count2 = 0
        self.correct = 0
        self.ok1.display(self.count1)
        self.ok2.display(self.count2)
        
        self.xy1.setEnabled(True)
        self.xy2.setEnabled(True)
        self.xy3.setEnabled(True)
        self.xy4.setEnabled(True)
        self.xy5.setEnabled(True)
        self.xy6.setEnabled(True)
        self.xy7.setEnabled(True)
        self.xy8.setEnabled(True)
        self.xy9.setEnabled(True)
        self.xy10.setEnabled(True)
        
        
        self.y1.setText("")
        self.y2.setText("")
        self.y3.setText("")
        self.y4.setText("")
        self.y5.setText("")
        self.y6.setText("")
        self.y7.setText("")
        self.y8.setText("")
        self.y9.setText("")
        self.y10.setText("")
        
        pal = self.z1.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z1.setPalette(pal)
        
        pal = self.z2.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z2.setPalette(pal)
        
        pal = self.z3.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z3.setPalette(pal)
        
        pal = self.z4.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z4.setPalette(pal)
        
        pal = self.z5.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z5.setPalette(pal)
        
        pal = self.z6.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z6.setPalette(pal)
        
        pal = self.z7.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z7.setPalette(pal)
        
        pal = self.z8.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z8.setPalette(pal)
        
        pal = self.z9.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z9.setPalette(pal)
        
        pal = self.z10.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z10.setPalette(pal)
        
        pal = self.z11.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z11.setPalette(pal)
        
        pal = self.z12.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z12.setPalette(pal)
        
        pal = self.z13.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z13.setPalette(pal)
        
        pal = self.z14.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z14.setPalette(pal)
        
        pal = self.z15.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z15.setPalette(pal)
        
        self.x1.setText("№1:     {} * {} = ".format(self.n1, self.n2))
        self.x1.resize(self.x1.sizeHint())
        
        self.x2.setText("№2:     {} + {} = ".format(self.n3, self.n4))
        self.x2.resize(self.x2.sizeHint())
        
        self.x3.setText("№3:     {} - {} = ".format(self.n5, self.n2))
        self.x3.resize(self.x3.sizeHint())
           
        self.x4.setText("№4:     {} * {} = ".format(self.n3, self.n1))
        self.x4.resize(self.x4.sizeHint())
        
        self.x5.setText("№5:     {} - {} = ".format(self.n6, self.n7))
        self.x5.resize(self.x5.sizeHint())
        
        self.x6.setText("№6:     {} + {} = ".format(self.n4, self.n6))
        self.x6.resize(self.x6.sizeHint())
        
        self.x7.setText("№7:     {} * {} = ".format(self.n3, self.n2))
        self.x7.resize(self.x7.sizeHint())
        
        self.x8.setText("№8:     {} + {} = ".format(self.n5, self.n3))
        self.x8.resize(self.x8.sizeHint())
        
        self.x9.setText("№9:     {} - {} = ".format(self.n6, self.n2))
        self.x9.resize(self.x9.sizeHint())
        
        self.x10.setText("№10:    {} * {} = ".format(self.n4, self.n3))
        self.x10.resize(self.x10.sizeHint())
        
        self.z1.setText("{}".format(self.n1 * self.n2))
        self.z2.setText("{}".format(self.n3 + self.n4))
        self.z3.setText("{}".format(self.n5 - self.n2))
        self.z4.setText("{}".format(self.n1 * self.n3))
        self.z5.setText("{}".format(self.n6 - self.n7))
        self.z6.setText("{}".format(self.n4 + self.n6))
        self.z7.setText("{}".format(self.n3 * self.n2))
        self.z8.setText("{}".format(self.n5 + self.n3))
        self.z9.setText("{}".format(self.n6 - self.n2))
        self.z10.setText("{}".format(self.n3 * self.n4))
        self.z11.setText("{}".format(self.n5 * self.n2))
        self.z12.setText("{}".format(self.n1 + self.n5))
        self.z13.setText("{}".format(self.n2 - self.n4))
        self.z14.setText("{}".format(self.n5 * self.n6))
        self.z15.setText("{}".format(self.n1 - self.n7))
    
    def go1(self):
        k = self.y1.text()
        self.xy1.setEnabled(False)
        if int(k) == self.n1 * self.n2:
            self.correct += 1
            self.count1 += 1
            self.ok1.display(self.count1)
            pal = self.z1.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
            self.z1.setPalette(pal)
        else:
            self.count2 += 1
            self.ok2.display(self.count2)
    
    def go2(self):
        k = self.y2.text()
        self.xy2.setEnabled(False)
        if int(k) == self.n3 + self.n4:
            self.correct += 1
            self.count1 += 1
            self.ok1.display(self.count1)
            pal = self.z2.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"))
            self.z2.setPalette(pal)
        else:
            self.count2 += 1
            self.ok2.display(self.count2)
        
    def go3(self):
        k = self.y3.text()
        self.xy3.setEnabled(False)
        if int(k) == self.n5 - self.n2:
            self.correct += 1
            self.count1 += 1
            self.ok1.display(self.count1)
            pal = self.z3.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("blue"))
            self.z3.setPalette(pal)
        else:
            self.count2 += 1
            self.ok2.display(self.count2)
    
    def go4(self):
        k = self.y4.text()
        self.xy4.setEnabled(False)
        if int(k) == self.n1 * self.n3:
            self.correct += 1
            self.count1 += 1
            self.ok1.display(self.count1)
            pal = self.z4.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("orange"))
            self.z4.setPalette(pal)
        else:
            self.count2 += 1
            self.ok2.display(self.count2)
        
    def go5(self):
        k = self.y5.text()
        self.xy5.setEnabled(False)
        if int(k) == self.n6 - self.n7:
            self.correct += 1
            self.count1 += 1
            self.ok1.display(self.count1)
            pal = self.z5.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("purple"))
            self.z5.setPalette(pal)
        else:
            self.count2 += 1
            self.ok2.display(self.count2)
        
    def go6(self):
        k = self.y6.text()
        self.xy6.setEnabled(False)
        if int(k) == self.n4 + self.n6:
            self.correct += 1
            self.count1 += 1
            self.ok1.display(self.count1)
            pal = self.z6.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("sky blue"))
            self.z6.setPalette(pal)
        else:
            self.count2 += 1
            self.ok2.display(self.count2)
    
    def go7(self):
        k = self.y7.text()
        self.xy7.setEnabled(False)
        if int(k) == self.n3 * self.n2:
            self.correct += 1
            self.count1 += 1
            self.ok1.display(self.count1)
            pal = self.z7.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("pink"))
            self.z7.setPalette(pal)
        else:
            self.count2 += 1
            self.ok2.display(self.count2)
        
    def go8(self):
        k = self.y8.text()
        self.xy8.setEnabled(False)
        if int(k) == self.n5 + self.n3:
            self.correct += 1
            self.count1 += 1
            self.ok1.display(self.count1)
            pal = self.z8.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"))
            self.z8.setPalette(pal)
        else:
            self.count2 += 1
            self.ok2.display(self.count2)
    
    def go9(self):
        k = self.y9.text()
        self.xy9.setEnabled(False)
        if int(k) == self.n6 - self.n2:
            self.correct += 1
            self.count1 += 1
            self.ok1.display(self.count1)
            pal = self.z9.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("yellow"))
            self.z9.setPalette(pal)
        else:
            self.count2 += 1
            self.ok2.display(self.count2)
        
    def go10(self):
        k = self.y10.text()
        self.xy10.setEnabled(False)
        if int(k) == self.n3 * self.n4:
            self.correct += 1
            self.count1 += 1
            self.ok1.display(self.count1)
            pal = self.z10.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("gray"))
            self.z10.setPalette(pal)
        else:
            self.count2 += 1
            self.ok2.display(self.count2)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())