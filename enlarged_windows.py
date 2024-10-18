from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
import os 
from dotenv import load_dotenv,find_dotenv

DOT_ENV_PATH = "C:/codes/GUIs/Scriptx"


load_dotenv(os.path.join(DOT_ENV_PATH,".env"))







class EnlargedWindow(QMainWindow):
    def __init__(self,parent=None,text=None):
        super(EnlargedWindow,self).__init__(parent)
        
        loadUi(os.path.join(os.getenv("assets_path"),"enlarged.ui"),self)

        self.setWindowTitle("Enlarged View")


        