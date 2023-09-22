from PyQt5.QtWidgets import QApplication

from multiprocessing import Process
from threading import Thread
import sys

from GeneracionProcesos import VentanaGeneracionProcesos
from ProcesosTerminados import VentanaProcesosTerminados


def generacion_procesos():
    app = QApplication(sys.argv)
    ventana_generacion_procesos = VentanaGeneracionProcesos()
    sys.exit(app.exec_())

def procesos_terminados():
    app = QApplication(sys.argv)
    ventana_procesos_terminados = VentanaProcesosTerminados()
    sys.exit(app.exec_())


if __name__ == '__main__':
    proceso = Process(target=generacion_procesos)
    terminado = Process(target=procesos_terminados)
    proceso.start()
    terminado.start()

    terminado.join()
    proceso.join()
