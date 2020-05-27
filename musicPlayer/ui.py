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

    

    self.label = QLabel("Choose File",self)
    self.label.resize(450,30)
    self.label.move(30,10)

    self.show()

   def play(self):
       name,dummy = QFileDialog.getOpenFileName(self,'Open File',
       options = QFileDialog.DontUseNativeDialog)
       self.label.setText("Playing "+str(name))
       playsound(str(name))

  

app = QApplication(sys.argv)
gui = musicPlayer()
sys.exit(app.exec_())
