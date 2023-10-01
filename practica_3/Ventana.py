from tkinter import Frame,Label,Entry,Button,StringVar,END
from tkinter import messagebox as mb
from tkinter.ttk import Treeview
from Lote import Proceso,Lote
from random import randint
from time import sleep

TECLA_INTERRUPCION = "i"
TECLA_ERROR = "e"
TECLA_CONTINUAR = "c"
TECLA_PAUSAR = "p"

class Ventana():
	def __init__(self,ventana,titulo = "Emulador de Procesamiento por Lotes"):
		self.__ventana = ventana
		self.__ventana.title(titulo)
		self._loteTemporal = Lote()
		self._procesoTemporal = Proceso()

		self.__procesosNuevosList: list = []
		self.__procesosListosList: list = []
		self.__procesosBloqueadosList: list = []
		self._tecla_estado = ""
		self._interrupcionProceso = ""
		self._tte = 0
		self._tre = 0
		self._loteEjecucion = 0
		self._procesoCompleto = 0
		self._procesosMemoria = 0
		self._procesosPendientes = False
		self._procesoEnEjecucion = None

		self.__noProgramaSTR = StringVar()
		self.__procesosBloqueadosSTR: list = [StringVar(),StringVar(),StringVar()]
		self.__peNombreSTR = StringVar()
		self.__peOperacionSTR = StringVar()
		self.__peTMESTR = StringVar()
		self.__peTTESTR = StringVar()
		self.__peTRESTR = StringVar()
		self.__peNoProgramaSTR = StringVar()
		self.__relojStr = StringVar()
		self.__seg: int = 0
		self.__min: int = 0

		self.__noProgramaSTR.set("Número de Programa: 0")
		self.__peNombreSTR.set("Nombre: ")
		self.__peOperacionSTR.set("Operación: ")
		self.__peTMESTR.set("TME: ")
		self.__peTTESTR.set("TTE: ")
		self.__peTRESTR.set("TRE: ")
		self.__peNoProgramaSTR.set("NoPrograma: ")
		self.__relojStr.set("00:00")
		for i in range(0,3,1):
			self.__procesosBloqueadosSTR[i].set("")

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
		self.__relojFrame = None

		""" Labels """
		self.__noProgramaLabel = None
		self.__procesosBloqueadosLabels: list = []*3

		self.__peNombreLabel = None
		self.__peOperacionLabel = None
		self.__peTMELabel = None
		self.__peTTELabel = None
		self.__peTRELabel = None
		self.__peNoProgramaLabel = None

		self.__relojLabel = None

		""" Entrys """
		self.__noProgramasEntry = None

		""" Treeview (Tablas) """
		self.__procesosNuevosTable = None
		self.__procesosListosTable = None
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

		self.__relojFrame = Frame(self.__botFrame)
		self.__relojFrame.grid(row = 1,column = 0,padx = 5, pady = 5)

	def __initLabels(self):
		""" TopFrameLables """
		self.__noProgramaLabel = Label(self.__topLeftFrame, text = "Numero de Programas")
		self.__noProgramaLabel.grid(row = 0,column = 0)

		""" MidFrameLables """
		Label(self.__midRightFrame,text = "Procesos Listos").grid(row = 0,column = 0,pady = 5,padx = 5)
		Label(self.__midRightFrame,text = "Procesos Bloqueados").grid(row = 2,column = 0,pady = 5,padx = 5)
		for i in range(0,3,1):
			self.__procesosBloqueadosLabels.append(Label(self.__midRightFrame,textvariable = self.__procesosBloqueadosSTR[i]))
			self.__procesosBloqueadosLabels[-1].grid(row = (3+i),column = 0,pady = 5,padx = 5)

		""" BotFrameLabels """
		Label(self.__botLeftFrame,text = "Proceso en ejecución").grid(row = 0,column = 0,pady = 5,padx = 5)
		self.__peNombreLabel = Label(self.__botLeftFrame,textvariable = self.__peNombreSTR)
		self.__peNombreLabel.grid(row = 1,column = 0,padx = 5,sticky = "W")
		self.__peOperacionLabel = Label(self.__botLeftFrame,textvariable = self.__peOperacionSTR)
		self.__peOperacionLabel.grid(row = 2,column = 0,padx = 5,sticky = "W")
		self.__peTMELabel = Label(self.__botLeftFrame,textvariable = self.__peTMESTR)
		self.__peTMELabel.grid(row = 3,column = 0,padx = 5,sticky = "W")
		self.__peTTELabel = Label(self.__botLeftFrame,textvariable = self.__peTTESTR)
		self.__peTTELabel.grid(row = 4,column = 0,padx = 5,sticky = "W")
		self.__peTRELabel = Label(self.__botLeftFrame,textvariable = self.__peTRESTR)
		self.__peTRELabel.grid(row = 5,column = 0,padx = 5,sticky = "W")
		self.__peNoProgramaLabel = Label(self.__botLeftFrame,textvariable = self.__peNoProgramaSTR)
		self.__peNoProgramaLabel.grid(row = 6,column = 0,padx = 5,sticky = "W")
		Label(self.__botRightFrame,text = "Procesos terminados").grid(row = 0,column = 0,pady = 5,padx = 5)

		self.__relojLabel = Label(self.__relojFrame,textvariable = self.__relojStr)
		self.__relojLabel.grid(row = 0,column = 0)

	def __initEntrys(self):
		self.__noProgramasEntry = Entry(self.__topLeftFrame)
		self.__noProgramasEntry.grid(row = 0,column = 1)

	def __initTreeviews(self):
		self.__procesosNuevosTable = Treeview(self.__topRightFrame,columns = ("No","Programador","Operación","TME"),height = 5)
		self.__procesosNuevosTable.grid(row = 0,column = 0,pady = 5)
		self.__procesosNuevosTable.column("#0",width = 1)
		self.__procesosNuevosTable.column("No",width = 50)
		self.__procesosNuevosTable.heading("No",text = "No")
		self.__procesosNuevosTable.column("Programador",width = 100)
		self.__procesosNuevosTable.heading("Programador",text = "Programador")
		self.__procesosNuevosTable.column("Operación",width = 100)
		self.__procesosNuevosTable.heading("Operación",text = "Operación")
		self.__procesosNuevosTable.column("TME",width = 50)
		self.__procesosNuevosTable.heading("TME",text = "TME")

		self.__procesosListosTable = Treeview(self.__midRightFrame,height = 5,
			columns = ("No","Programador","Operación","TME"))
		self.__procesosListosTable.grid(row = 1,column = 0,pady = 5,padx = 5)
		self.__procesosListosTable.column("#0",width = 1)
		self.__procesosListosTable.column("No",width = 50)
		self.__procesosListosTable.heading("No",text = "No")
		self.__procesosListosTable.column("Programador",width = 100)
		self.__procesosListosTable.heading("Programador",text = "Programador")
		self.__procesosListosTable.column("Operación",width = 100)
		self.__procesosListosTable.heading("Operación",text = "Operación")
		self.__procesosListosTable.column("TME",width = 50)
		self.__procesosListosTable.heading("TME",text = "TME")

		self.__procesosTerminadosTable = Treeview(self.__botRightFrame,height = 5,columns = ("No","Programador","Operación","Resultado","TME"))
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

	def __initButtons(self):
		Button(self.__topLeftFrame,text = "Agregar",command = lambda:self.__crearProcesos(self.__noProgramasEntry.get())).grid(row = 3,column = 1,pady = 5,padx = 5)
		Button(self.__midLeftFrame,text = "Comienza Emulación",command = lambda:self.__simular()).grid(row = 1,column = 0,pady = 5,padx = 5)
		#Button(self.__midLeftFrame,text = "Comienza Emulación",command = lambda:self.__simular()).grid(row = 1,column = 0,pady = 5,padx = 5)
		Button(self.__botRightFrame,text = "Reiniciar",command = lambda:self.__reiniciar()).grid(row = 3, column = 0,pady = 5,padx = 5,sticky = "E")

	def __crearProcesos(self,n: str):
		try:
			# Vacia la lista de procesos
			self.__procesosNuevosList = []
			# Vacia la tabla de "Procesos Nuevos"
			self.__vaciarTabla(self.__procesosNuevosTable)
			# Convierte a "n" en un entero (Se hizo la conversion aquí para evitar errores en tiempo de ejecucion)
			n = int(n)
			# Lista de Operadres validos
			operadores = ["+","-","/","*","%","^"]
			for i in range(0,n,1):
				# Genera una operacion aleatoria, ejemplo: "25 ^ 2"
				operacion = str(randint(0,100)) + operadores[randint(0,5)] + str(randint(0,100))
				# Crea el proceso con los datos validos
				proceso = Proceso("C&E",operacion,randint(7,18),i)
				# Se agrega el proceso a la lista
				self.__procesosNuevosList.append(proceso)
				# Obtenemos los datos para agregarlo a la tabla de "Todos los Procesos"
				data = [proceso.dameNoPrograma(),proceso.dameProgramador(),proceso.dameOperacion(),proceso.dameTiempoEstimadoSegundos()]
				# Añadimos los datos a la tabla
				self.__aniadeTabla(self.__procesosNuevosTable,data)
		except ValueError as e:
			mb.showerror("¡¡ERROR!!","Debes ingresar un número en \"Numero de Programas\"")

	def __simular(self):
		try:
			self.__vaciarTabla(self.__procesosListosTable)
			bloq = False
			relojAnt = ""
			while True:
				data: list = []
				# Obtenemos la lista de los procesos listos
				self.__obtenProcesosListos()
				
				# Actualiza el tiempo bloqueado
				if len(self.__procesosBloqueadosList) > 0 and not bloq:
					self.__peNombreSTR.set("Nombre: ")
					self.__peOperacionSTR.set("Operación: ")
					self.__peTMESTR.set("TME: ")
					self.__peTTESTR.set("TTE: ")
					self.__peTRESTR.set("TRE: ")
					self.__peNoProgramaSTR.set("NoPrograma: ")
					for proceso in self.__procesosBloqueadosList:
						if relojAnt != self.__relojStr.get():
							proceso.fijaTiempoBloqueado(proceso.dameTiempoBloqueado() - 1)
						
						if proceso.dameTiempoBloqueado() == 0:
							self.__procesosListosList.append(proceso)
							self.__procesosBloqueadosList.pop(0)

					self.__actualizaProcesosBloqueados()
					relojAnt = self.__relojStr.get()
					self.__reloj()
					self.__ventana.update()
					sleep(1)
				if bloq:
					bloq = False

				if len(self.__procesosListosList) > 0:
					# obtenemos los datos de los procesos nuevos y actualizamos la tabla
					for proceso in self.__procesosNuevosList:
						data.append([proceso.dameNoPrograma(),proceso.dameProgramador(),proceso.dameOperacion(),proceso.dameTiempoEstimadoSegundos()])
					self.__actualizaTabla(self.__procesosNuevosTable,data)

					# obtenemos los datos de los procesos listos y actualizamos la tabla
					data = []
					for proceso in self.__procesosListosList:
						data.append([proceso.dameNoPrograma(),proceso.dameProgramador(),proceso.dameOperacion(),proceso.dameTiempoEstimadoSegundos()])
						self.__aniadeTabla(self.__procesosListosTable,data)
					self.__actualizaTabla(self.__procesosListosTable,data)

					self._procesoEnEjecucion = None
					# Verificamos que podamos sacar el primer elemento de la lista de procesos listos
					if len(self.__procesosListosList) > 0:
					# Sacamos de la lista de procesos listos el primer elemento para comenzar a ejecutarlo
						self._procesoEnEjecucion = self.__procesosListosList.pop(0)
					TTE = 0

					while TTE < self._procesoEnEjecucion.dameTiempoEstimadoSegundos():
						self.__actualizaProcesosBloqueados()
						# obtenemos los datos de los procesos listos y actualizamos la tabla
						data = []
						for proceso in self.__procesosListosList:
							data.append([proceso.dameNoPrograma(),proceso.dameProgramador(),proceso.dameOperacion(),proceso.dameTiempoEstimadoSegundos()])
							self.__aniadeTabla(self.__procesosListosTable,data)
						self.__actualizaTabla(self.__procesosListosTable,data)

						self.__aniadeProcesoEjecucion(self._procesoEnEjecucion,TTE)
						# Verificamos si el programa esta en pausa, si lo esta, entonces se añade 0 a TTE de otro modo, se añade 1
						TTE += 1 if self._tecla_estado != TECLA_PAUSAR else 0
						self.__ventana.update()

						# salimos del bucle si la tecla es la de error
						if self._tecla_estado == TECLA_ERROR:
							TTE = self._procesoEnEjecucion.dameTiempoEstimadoSegundos()

						relojAnt = self.__relojStr.get()
						self.__reloj()

						if self._tecla_estado == TECLA_INTERRUPCION:
							TTE = self._procesoEnEjecucion.dameTiempoEstimadoSegundos()
							self._procesoEnEjecucion.fijaTiempoBloqueado(10)
							self.__procesosBloqueadosList.append(self._procesoEnEjecucion)
							self.__actualizaProcesosBloqueados()
							bloq = True

						# Actualiza el tiempo bloqueado
						if len(self.__procesosBloqueadosList) > 0 and not bloq:
							for proceso in self.__procesosBloqueadosList:
								if relojAnt != self.__relojStr.get():
									proceso.fijaTiempoBloqueado(proceso.dameTiempoBloqueado() - 1)

								if proceso.dameTiempoBloqueado() == 0:
									self.__procesosListosList.append(proceso)
									self.__procesosBloqueadosList.pop(0)

							self.__actualizaProcesosBloqueados()
							relojAnt = self.__relojStr.get()
							self.__reloj()
							self.__ventana.update()
						if bloq:
							bloq = False
						sleep(1)
					
					if self._tecla_estado != TECLA_INTERRUPCION:
						# Si la tecla fue la de error, en la DATA que se le enviara a la tabla de terminados vendra un mensaje de "ERROR"
						# En otro caso, se enviara el resultado junto con el resto de datos
						if self._tecla_estado == TECLA_ERROR:
							data = [self._procesoEnEjecucion.dameNoPrograma(),self._procesoEnEjecucion.dameProgramador(),self._procesoEnEjecucion.dameOperacion(),"ERROR",self._procesoEnEjecucion.dameTiempoEstimadoSegundos()]
							self._tecla_estado = TECLA_CONTINUAR
						else:
							data = [self._procesoEnEjecucion.dameNoPrograma(),self._procesoEnEjecucion.dameProgramador(),self._procesoEnEjecucion.dameOperacion(),self._procesoEnEjecucion.resolver(),self._procesoEnEjecucion.dameTiempoEstimadoSegundos()]

						self.__aniadeTabla(self.__procesosTerminadosTable,data)
						self._procesosMemoria -= 1
					else:
						self._tecla_estado = TECLA_CONTINUAR

					if len(self.__procesosNuevosList) <= 0 and self._procesosMemoria == 0:
						break
		except IndexError as e:
			mb.showerror(
				"¡¡ERROR!!",
				f"Debes ingresar por lo menos 1 proceso {e}"
			)

	def __obtenProcesosListos(self):
		while len(self.__procesosNuevosList) > 0 and self._procesosMemoria < 3:
			self._procesosMemoria += 1
			self.__procesosListosList.append(self.__procesosNuevosList.pop(0))

	def __actualizaProcesosBloqueados(self):
		# self.__peNombreSTR.set("Nombre: ")
		# self.__peOperacionSTR.set("Operación: ")
		# self.__peTMESTR.set("TME: ")
		# self.__peTTESTR.set("TTE: ")
		# self.__peTRESTR.set("TRE: ")
		# self.__peNoProgramaSTR.set("NoPrograma: ")

		for i in range(0,3,1):
			self.__procesosBloqueadosSTR[i].set("")

		for i in range(0,len(self.__procesosBloqueadosList),1):
			proceso = self.__procesosBloqueadosList[i]
			self.__procesosBloqueadosSTR[i].set(f"ID: {proceso.dameNoPrograma()} | Tiempo Bloqueado: {proceso.dameTiempoBloqueado()}")
			self.__ventana.update()

	def __vaciarTabla(self,tabla):
		for i in tabla.get_children():
			tabla.delete(i)

	def __aniadeTabla(self,tabla,data):
		tabla.insert('',END,values = data)

	def __actualizaTabla(self,tabla,data):
		self.__vaciarTabla(tabla)
		for i in data:
			self.__aniadeTabla(tabla,i)

	def __aniadeProcesoEjecucion(self,proceso,TTE):
		self.__peNombreSTR.set(f"Nombre: {proceso.dameProgramador()}")
		self.__peOperacionSTR.set(f"Operación: {proceso.dameOperacion()}")
		self.__peTMESTR.set(f"TME: {proceso.dameTiempoEstimadoSegundos()}")
		self.__peTTESTR.set(f"TTE: {TTE}")
		self.__peTRESTR.set(f"TRE: {proceso.dameTiempoEstimadoSegundos() - TTE}")
		self.__peNoProgramaSTR.set(f"NoPrograma: {proceso.dameNoPrograma()}")

	def __reiniciar(self):
		self.__vaciarTabla(self.__procesosNuevosTable)
		self.__vaciarTabla(self.__procesosListosTable)
		self.__vaciarTabla(self.__procesosTerminadosTable)
		self.__noProgramaSTR.set("Número de Programa: 0")
		self.__peNombreSTR.set("Nombre: ")
		self.__peOperacionSTR.set("Operación: ")
		self.__peTMESTR.set("TME: ")
		self.__peTTESTR.set("TTE: ")
		self.__peTRESTR.set("TRE: ")
		self.__peNoProgramaSTR.set("NoPrograma: ")
		self.__relojStr.set("00:00")
		self.__min = self.__seg = 0

	def __reloj(self):
		if self.__seg == 59:
			self.__seg = 0
			self.__min += 1

		self.__seg += 1
		horaImp = "0" if self.__min < 10 else ""
		horaImp += str(self.__min)+":"
		horaImp += "0" if self.__seg < 10 else ""
		horaImp += str(self.__seg)
		self.__relojStr.set(horaImp)

	def key_press(self, event) -> None:
		if event.char == TECLA_CONTINUAR:
			self._tecla_estado = TECLA_CONTINUAR
		elif event.char == TECLA_PAUSAR:
			self._tecla_estado = TECLA_PAUSAR
		elif event.char == TECLA_INTERRUPCION:
			self._tecla_estado = TECLA_INTERRUPCION
		elif event.char == TECLA_ERROR:
			self._tecla_estado = TECLA_ERROR
		else:
			pass

	def dibujar(self):
		self.__ventana.bind("<Key>", self.key_press)
		self.__ventana.mainloop()