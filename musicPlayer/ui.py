from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from playsound import playsound

class musicPlayer(QMainWindow):
       
   def __init__(self):
    super(musicPlayer, self).__init__()
    self.setGeometry(50,50,500,100)
    self.setWindowTitle("QtMuse")
    #self.setWindowIcon(QtGui.QIcon)

    playBtn = QPushButton("Play",self)
    playBtn.resize(60,30)
    playBtn.move(210,50)
    playBtn.clicked.connect(self.play)

    backwardBtn = QPushButton("Backward",self)
    backwardBtn.resize(60,30)
    backwardBtn.move(120,50)
    backwardBtn.clicked.connect(self.back)

    forwardBtn = QPushButton("Forward",self)
    forwardBtn.resize(60,30)
    forwardBtn.move(300,50)
    forwardBtn.clicked.connect(self.forward)

    shuffleBtn = QPushButton("Shuffle",self)
    shuffleBtn.resize(60,30)
    shuffleBtn.move(30,50)
    shuffleBtn.clicked.connect(self.shuffle)

    loopBtn = QPushButton("Loop",self)
    loopBtn.resize(60,30)
    loopBtn.move(390,50)
    loopBtn.clicked.connect(self.loop)

    self.label = QLabel("Choose File",self)
    self.label.resize(450,30)
    self.label.move(30,10)

    self.show()

   def play(self):
       name,dummy = QFileDialog.getOpenFileName(self,'Open File',
       options = QFileDialog.DontUseNativeDialog)
       self.label.setText("Playing "+str(name))
       playsound(str(name))

   def back(self):
    pass

   def forward(self):
    pass
    
   def shuffle(self):
    pass

   def loop(self):
    pass

app = QApplication(sys.argv)
gui = musicPlayer()
sys.exit(app.exec_())
