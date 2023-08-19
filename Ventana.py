from tkinter import Tk # se eliminara esta linea una ves terminado el sistema

from tkinter import Frame,Label,Entry,Button,StringVar,END
from tkinter import messagebox as mb
from tkinter.ttk import Treeview
from Lote import Proceso,Lote

from random import randint

class Ventana():
	def __init__(self,ventana):
		self.__ventana = ventana

		self.__procesosLote = 4
		self.__procesos = []
		self.__lotes = []
		self.__operacionSTR = StringVar()
		self.__noProgramaSTR = StringVar()
		self.__lotesPendientesSTR = StringVar()

		self.__noProgramaSTR.set("Número de Programa: 0")
		self.__lotesPendientesSTR.set("Lotes Pendientes: 0")

		""" Frames """
		self.__topFrame = None
		self.__topLeftFrame = None
		self.__topRightFrame = None

		self.__midFrame = None
		self.__midLeftFrame = None
		self.__midRightFrame = None

		self.__botFrame = None
		self.__botLeftFrame = None
		self.__botRightFrame = None

		""" Labels """
		self.__noProgramaLabel = None

		self.__lotesPendientesLabel = None

		self.__peNombreLabel = None
		self.__peOperacionLabel = None
		self.__peTMELabel = None
		self.__peNoProgramaLabel = None

		""" Entrys """
		self.__programadorEntry = None
		self.__operacionEntry = None
		self.__TMEEntry = None

		""" Buttons """
		self.__agregarButton = None
		self.__simulacionButton = None

		""" Treeview (Tablas) """
		self.__todosProcesosTable = None
		self.__loteEjecucionTable = None
		self.__procesosTerminadosTable = None

		""" Inicializaciones """
		self.__initFrames()
		self.__initLabels()
		self.__initEntrys()
		self.__initTreeviews()
		self.__initButtons()

	def __initFrames(self):
		self.__topFrame = Frame(self.__ventana)
		self.__topFrame.grid(row = 0,column = 0,pady = 5,padx = 5)
		self.__topLeftFrame = Frame(self.__topFrame)
		self.__topLeftFrame.grid(row = 0,column = 0,pady = 5,padx = 5)
		self.__topRightFrame = Frame(self.__topFrame)
		self.__topRightFrame.grid(row = 0,column = 1,pady = 5,padx = 5)

		self.__midFrame = Frame(self.__ventana)
		self.__midFrame.grid(row = 1,column = 0,pady = 5,padx = 5)
		self.__midLeftFrame = Frame(self.__midFrame)
		self.__midLeftFrame.grid(row = 0,column = 0,pady = 5,padx = 5)
		self.__midRightFrame = Frame(self.__midFrame)
		self.__midRightFrame.grid(row = 0,column = 1,pady = 5,padx = 5)

		self.__botFrame = Frame(self.__ventana)
		self.__botFrame.grid(row = 2,column = 0,pady = 5,padx = 5)
		self.__botLeftFrame = Frame(self.__botFrame)
		self.__botLeftFrame.grid(row = 0,column = 0,pady = 5,padx = 5)
		self.__botRightFrame = Frame(self.__botFrame)
		self.__botRightFrame.grid(row = 0,column = 1,pady = 5,padx = 5)

	def __initLabels(self):
		""" TopFrameLables """
		Label(self.__topLeftFrame,text = "Programador").grid(row = 0,column = 0,pady = 5,padx = 5,sticky = "E")
		Label(self.__topLeftFrame,text = "Tiempo Maximo Estimado").grid(row = 2,column = 0,pady = 5,
			padx = 5,sticky = "E")
		self.__noProgramaLabel = Label(self.__topLeftFrame,textvariable = self.__noProgramaSTR)
		self.__noProgramaLabel.grid(row = 3,column = 0,pady = 5,padx = 5,sticky = "E")

		""" MidFrameLables """
		self.__lotesPendientesLabel = Label(self.__midLeftFrame,textvariable = self.__lotesPendientesSTR)
		self.__lotesPendientesLabel.grid(row = 0,column = 0,pady = 5,padx = 5)
		Label(self.__midRightFrame,text = "Lote en ejecución").grid(row = 0,column = 0,pady = 5,padx = 5)

		""" BotFrameLabels """
		Label(self.__botLeftFrame,text = "Proceso en ejecución").grid(row = 0,column = 0,pady = 5,padx = 5)
		self.__peNombreLabel = Label(self.__botLeftFrame,text = "Nombre: ")
		self.__peNombreLabel.grid(row = 1,column = 0,padx = 5,sticky = "W")
		self.__peOperacionLabel = Label(self.__botLeftFrame,text = "Operación: ")
		self.__peOperacionLabel.grid(row = 2,column = 0,padx = 5,sticky = "W")
		self.__peTMELabel = Label(self.__botLeftFrame,text = "TME: ")
		self.__peTMELabel.grid(row = 3,column = 0,padx = 5,sticky = "W")
		self.__peNoProgramaLabel = Label(self.__botLeftFrame,text = "NoPrograma: ")
		self.__peNoProgramaLabel.grid(row = 4,column = 0,padx = 5,sticky = "W")
		Label(self.__botRightFrame,text = "Procesos terminados").grid(row = 0,column = 0,pady = 5,padx = 5)

	def __initEntrys(self):
		self.__programadorEntry = Entry(self.__topLeftFrame)
		self.__programadorEntry.grid(row = 0,column = 1,pady = 5,padx = 5)
		self.__operacionEntry = Entry(self.__topLeftFrame,textvariable = self.__operacionSTR)
		self.__operacionEntry.grid(row = 1,column = 1,pady = 5,padx = 5)
		self.__TMEEntry = Entry(self.__topLeftFrame)
		self.__TMEEntry.grid(row = 2,column = 1,pady = 5,padx = 5)

	def __initTreeviews(self):
		self.__todosProcesosTable = Treeview(self.__topRightFrame,
			columns = ("No","Programador","Operación","TME"),height = 5)
		self.__todosProcesosTable.grid(row = 0,column = 0,pady = 5)
		self.__todosProcesosTable.column("#0",width = 1)
		self.__todosProcesosTable.column("No",width = 50)
		self.__todosProcesosTable.heading("No",text = "No")
		self.__todosProcesosTable.column("Programador",width = 100)
		self.__todosProcesosTable.heading("Programador",text = "Programador")
		self.__todosProcesosTable.column("Operación",width = 100)
		self.__todosProcesosTable.heading("Operación",text = "Operación")
		self.__todosProcesosTable.column("TME",width = 50)
		self.__todosProcesosTable.heading("TME",text = "TME")

		self.__loteEjecucionTable = Treeview(self.__midRightFrame,height = 5,
			columns = ("No","Programador","Operación","TME","Lote"))
		self.__loteEjecucionTable.grid(row = 1,column = 0,pady = 5,padx = 5)
		self.__loteEjecucionTable.column("#0",width = 1)
		self.__loteEjecucionTable.column("No",width = 50)
		self.__loteEjecucionTable.heading("No",text = "No")
		self.__loteEjecucionTable.column("Programador",width = 100)
		self.__loteEjecucionTable.heading("Programador",text = "Programador")
		self.__loteEjecucionTable.column("Operación",width = 100)
		self.__loteEjecucionTable.heading("Operación",text = "Operación")
		self.__loteEjecucionTable.column("TME",width = 50)
		self.__loteEjecucionTable.heading("TME",text = "TME")
		self.__loteEjecucionTable.column("Lote",width = 50)
		self.__loteEjecucionTable.heading("Lote",text = "Lote")
		
		self.__procesosTerminadosTable = Treeview(self.__botRightFrame,height = 5,
			columns = ("No","Programador","Operación","Resultado","TME","Lote"))
		self.__procesosTerminadosTable.grid(row = 1,column = 0,pady = 5,padx = 5)
		self.__procesosTerminadosTable.column("#0",width = 1)
		self.__procesosTerminadosTable.column("No",width = 50)
		self.__procesosTerminadosTable.heading("No",text = "No")
		self.__procesosTerminadosTable.column("Programador",width = 100)
		self.__procesosTerminadosTable.heading("Programador",text = "Programador")
		self.__procesosTerminadosTable.column("Operación",width = 100)
		self.__procesosTerminadosTable.heading("Operación",text = "Operación")
		self.__procesosTerminadosTable.column("Resultado",width = 100)
		self.__procesosTerminadosTable.heading("Resultado",text = "Resultado")
		self.__procesosTerminadosTable.column("TME",width = 50)
		self.__procesosTerminadosTable.heading("TME",text = "TME")
		self.__procesosTerminadosTable.column("Lote",width = 50)
		self.__procesosTerminadosTable.heading("Lote",text = "Lote")
		
	def __initButtons(self):
		self.__agregarButton = Button(self.__topLeftFrame,text = "Agregar",command = lambda:self.__agregarProceso())
		self.__agregarButton.grid(row = 3,column = 1,pady = 5,padx = 5)
		self.__simulacionButton = Button(self.__midLeftFrame,text = "Comienza Eimulación",
			command = lambda:self.__simular())
		self.__simulacionButton.grid(row = 1,column = 0,pady = 5,padx = 5)
		Button(self.__topLeftFrame,text = "Operación",command = lambda:self.__generaOperacion()).grid(row = 1,
			column = 0,pady = 5,padx = 5,sticky = "E")

	def __generaOperacion(self):
		operadores = ["+","-","/","*","%","^"]
		operacion = str(randint(0,100)) + operadores[randint(0,5)] + str(randint(0,100))
		self.__operacionSTR.set(operacion)

	def __agregarProceso(self):
		try:
			programador = self.__programadorEntry.get()
			operacion = self.__operacionEntry.get()
			TME = int(self.__TMEEntry.get())
			proceso = Proceso(programador,operacion,TME,len(self.__procesos))
			lenLotes = len(self.__lotes)
			# Se verifica si el lote esta vacio
			if lenLotes == 0 or self.__lotes[-1].lleno():
				self.__lotes.append(Lote(lenLotes+1))
			self.__lotes[-1].agregar(proceso)
			self.__procesos.append(proceso)
			data = [proceso.dameNoPrograma(),proceso.dameProgramador(),
				proceso.dameOperacion(),proceso.dameTiempoEstimadoSegundos()]
			self.__aniadeTabla(self.__todosProcesosTable,data)
			self.__noProgramaSTR.set(f"Número de Programa: {len(self.__procesos)}")
		except ValueError as e:
			mb.showerror(
				"¡¡ERROR!!",
				"Debes ingresar un número en \"Tiempo Maximo Estimado\""
			)

	def __crearProcesos(self,n):
		operadores = ["+","-","/","*","%","^"]
		for i in range(0,n,1):
			operacion = str(randint(0,100)) + operadores[randint(0,5)] + str(randint(0,100))
			proceso = Proceso(i,operacion,randint(1,20))
			self.__procesosList.append(proceso)

	def __simular(self):
		try:
			pass
		except IndexError as e:
			mb.showerror(
				"¡¡ERROR!!",
				"Debes ingresar por lo menos 1 proceso"
			)

	def __vaciarTabla(self,tabla):
		for i in tabla.get_children():
			tabla.delete(i)

	def __aniadeTabla(self,tabla,data):
		tabla.insert('',END,values = data)

	def dibujar(self):
		self.__ventana.mainloop()


if __name__ == "__main__":
	Ventana(Tk()).dibujar()