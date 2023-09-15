from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

import sys
import pathlib

from WatingSpinner import WaitingSpinner

UI_PATH = pathlib.Path("ui/waitting_spinner_window.ui")


class WaitingSpinnerWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__load_ui_file(pathlib.Path(__file__).parent)
        self.start_spinner()

    def __load_ui_file(self, path: pathlib.Path) -> None:
        uic.loadUi(path / UI_PATH, self)

    def start_spinner(self) -> None:
        spinner = WaitingSpinner(self)
        spinner.start()
        spinner.show()


def define_waiting_spinner() -> None:
    app = QApplication(sys.argv)
    spinner_window = WaitingSpinnerWidget()
    spinner_window.show()
    sys.exit(app.exec_())
