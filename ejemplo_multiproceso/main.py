from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5 import uic

import sys
import pathlib
from multiprocessing import Process, Queue
from time import sleep

from waiting_spinner import define_waiting_spinner

UI_PATH = pathlib.Path("ui/main_widget.ui")


def start_waitting_spinner() -> None:
    define_waiting_spinner()
    sleep(5.0)

# def reverse_fibonacci_serie(fibonacci_queue) -> int:


def reverse_fibonacci_serie(queue) -> int:
    current_value = queue.get()
    print("Recv Value:", current_value)
    next_value = current_value + (current_value + 1)
    print("Send New Value:", next_value)
    queue.put(next_value)


class MainTestWindow(QMainWindow):
    def __init__(self):
        super(MainTestWindow, self).__init__()

        self.__load_ui_file(pathlib.Path(__file__).parent)
        self.__define_widgets()
        self.__button_triggers()

    def __load_ui_file(self, path: pathlib.Path) -> None:
        uic.loadUi(path / UI_PATH, self)

    def __define_widgets(self) -> None:
        self.waitting_time = self.findChild(QLineEdit, "witting_time")
        self.trigger_button = self.findChild(QPushButton, "trigger_button")
        self.fibonacci_serie_view = self.findChild(
            QLabel, "fibonnaci_serie_view")

    def __button_triggers(self) -> None:
        self.trigger_button.clicked.connect(self.__thread_operations)

    def __thread_operations(self) -> None:
        waitting_time = int(self.waitting_time.text())
        self.fibonacci_serie_view.setText("0")

        fibonacci_queue = Queue()
        fibonacci_queue.put(waitting_time)
        self.__update_fibonacci_label_multiprocess(waitting_time)

    def __update_fibonacci_label_multiprocess(self, waiting_time: int) -> None:
        # Delacración de un proceso (programación multiprocesos)
        spinner_process = Process(target=start_waitting_spinner)
        # Inicio de proceso
        spinner_process.start()
        # Operación funcionando simultaneamente con el otro proceso
        for value in range(waiting_time):
            print("Next Value:", value)
            next_value = str(value + (value + 1))
            self.fibonacci_serie_view.setText(next_value)
        # Fin del proceso
        spinner_process.kill()


def main():
    app = QApplication(sys.argv)
    window = MainTestWindow()
    # login = WaitingSpinnerWidget()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
