from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel, QPushButton

import pathlib
from random import randint

UI_PATH = r"ui/GeneracionProcesos.ui"


class VentanaGeneracionProcesos(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__load_ui_file(pathlib.Path(__file__).parent)
        self.__define_widgets()
        self.__manage_buttons()

        self.show()
        
    def __load_ui_file(self, path) -> None:
        uic.loadUi(path / UI_PATH, self)
    
    def __define_widgets(self):
        self._btn = self.findChild(QPushButton, "pushButton")
        self._lb = self.findChild(QLabel, "label")
    
    def __manage_buttons(self):
        self._btn.clicked.connect(self.__print_random_number)
    
    def __print_random_number(self):
        num = str(randint(0,1000))
        self._lb.setText(num)
