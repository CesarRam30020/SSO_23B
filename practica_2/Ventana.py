from tkinter import Frame,Label,Entry,Button,StringVar,END
from tkinter import messagebox as mb
from tkinter.ttk import Treeview
from Lote import Proceso,Lote
from random import randint
from time import sleep

class Ventana():
	def __init__(self,ventana,titulo = "Emulador de Procesamiento por Lotes"):
		self.__ventana = ventana
		self.__ventana.title(titulo)

		self.__procesos: list = []
		self.__lotes: list = []

		self.__noProgramaSTR = StringVar()
		self.__lotesPendientesSTR = StringVar()
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
		self.__lotesPendientesSTR.set("Lotes Pendientes: 0")
		self.__peNombreSTR.set("Nombre: ")
		self.__peOperacionSTR.set("Operación: ")
		self.__peTMESTR.set("TME: ")
		self.__peTTESTR.set("TTE: ")
		self.__peTRESTR.set("TRE: ")
		self.__peNoProgramaSTR.set("NoPrograma: ")
		self.__relojStr.set("00:00")

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

		self.__lotesPendientesLabel = None

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

		self.__relojFrame = Frame(self.__botFrame)
		self.__relojFrame.grid(row = 1,column = 0,padx = 5, pady = 5)

	def __initLabels(self):
		""" TopFrameLables """
		self.__noProgramaLabel = Label(self.__topLeftFrame, text = "Numero de Programas")
		self.__noProgramaLabel.grid(row = 0,column = 0)

		""" MidFrameLables """
		self.__lotesPendientesLabel = Label(self.__midLeftFrame,textvariable = self.__lotesPendientesSTR)
		self.__lotesPendientesLabel.grid(row = 0,column = 0,pady = 5,padx = 5)
		Label(self.__midRightFrame,text = "Lote en ejecución").grid(row = 0,column = 0,pady = 5,padx = 5)

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
		Button(self.__topLeftFrame,text = "Agregar",command = lambda:self.__crearProcesos(self.__noProgramasEntry.get())).grid(row = 3,column = 1,pady = 5,padx = 5)
		Button(self.__midLeftFrame,text = "Comienza Eimulación",command = lambda:self.__simular()).grid(row = 1,column = 0,pady = 5,padx = 5)
		Button(self.__botRightFrame,text = "Reiniciar",command = lambda:self.__reiniciar()).grid(row = 2,
			column = 0,pady = 5,padx = 5,sticky = "E")

	def __crearProcesos(self,n: str):
		try:
			# Vacia la lista de procesos
			self.__procesos = []
			# Vacia la tabla de "Todos los Procesos"
			self.__vaciarTabla(self.__todosProcesosTable)
			# Convierte a "n" en un entero (Se hizo la conversion aquí para evitar errores en tiempo de ejecucion)
			n = int(n)
			# Lista de Operadres validos
			operadores = ["+","-","/","*","%","^"]
			for i in range(0,n,1):
				# Genera una operacion aleatoria, ejemplo: "25 ^ 2"
				operacion = str(randint(0,100)) + operadores[randint(0,5)] + str(randint(0,100))
				# Crea el proceso con los datos validos
				proceso = Proceso("C&E",operacion,randint(7,18),i)
				lenLotes = len(self.__lotes)
				# Se verifica si el lote esta lleno
				if lenLotes == 0 or self.__lotes[-1].lleno():
					self.__lotes.append(Lote(lenLotes+1))
				# Agrega el proceso al ultimo lote
				self.__lotes[-1].agregar(proceso)
				# Agrega el proceso a la lista de procesos
				self.__procesos.append(proceso)
				# Obtenemos los datos para agregarlo a la tabla de "Todos los Procesos"
				data = [proceso.dameNoPrograma(),proceso.dameProgramador(),proceso.dameOperacion(),proceso.dameTiempoEstimadoSegundos()]
				# Añadimos los datos a la tabla
				self.__aniadeTabla(self.__todosProcesosTable,data)
		except ValueError as e:
			mb.showerror(
				"¡¡ERROR!!",
				"Debes ingresar un número en \"Numero de Programas\""
			)

	def __simular(self):
		try:
			self.__vaciarTabla(self.__loteEjecucionTable)
			loteEjecucion = 1
			for lote in self.__lotes:
				self.__lotesPendientesSTR.set(f"Lotes Pendientes: {len(self.__lotes) - loteEjecucion}")
				loteEjecucion += 1
				# agrega todos los procesos a la tabla del "Lote en Ejecucion"
				for proceso in lote.procesos():
					# Obtiene los datos del Proceso necesarios para agregarlos a la tabla "Lote en Ejecucion"
					data = [proceso.dameNoPrograma(),proceso.dameProgramador(),proceso.dameOperacion(),
						proceso.dameTiempoEstimadoSegundos(),lote.dameNum()]
					# Agrega los datos a la tabla
					self.__aniadeTabla(self.__loteEjecucionTable,data)
				
				for proceso in lote.procesos():
					# Tiempo Total Ejecutado, comienza en cero por cada proceso que se ejecuta
					TTE = 0
					# Si el TTE es igual al tiempo estimado de ejecucion del proceso, termina el while
					while TTE <= proceso.dameTiempoEstimadoSegundos():
						# Añade los datos del proceso en ejecucion en el apartado de "Proceso en Ejecucion"
						self.__aniadeProcesoEjecucion(proceso,TTE)
						# Actualiza el contenido de la ventana
						self.__ventana.update()
						TTE += 1
						# Mueve el reloj
						self.__reloj()
						sleep(1)
					# Obtiene los datos del Proceso que se "acaba de ejecutar" para despues agregarlo a la table de "Procesos Terminados"
					data = [proceso.dameNoPrograma(),proceso.dameProgramador(),proceso.dameOperacion(),
						proceso.resolver(),proceso.dameTiempoEstimadoSegundos(),lote.dameNum()]
					# Añade el proceso a la tabla de "Procesos Terminados"
					self.__aniadeTabla(self.__procesosTerminadosTable,data)

                # Una vez ya no haya mas procesos para ejecutar, vacia la tabla de "Lote en Ejecucion"
				self.__vaciarTabla(self.__loteEjecucionTable)
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

	def __aniadeProcesoEjecucion(self,proceso,TTE):
		self.__peNombreSTR.set(f"Nombre: {proceso.dameProgramador()}")
		self.__peOperacionSTR.set(f"Operación: {proceso.dameOperacion()}")
		self.__peTMESTR.set(f"TME: {proceso.dameTiempoEstimadoSegundos()}")
		self.__peTTESTR.set(f"TTE: {TTE}")
		self.__peTRESTR.set(f"TRE: {proceso.dameTiempoEstimadoSegundos() - TTE}")
		self.__peNoProgramaSTR.set(f"NoPrograma: {proceso.dameNoPrograma()}")

	def __reiniciar(self):
		self.__vaciarTabla(self.__todosProcesosTable)
		self.__vaciarTabla(self.__loteEjecucionTable)
		self.__vaciarTabla(self.__procesosTerminadosTable)
		self.__procesos = []
		self.__lotes = []
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
		else:
			pass

		self.__seg += 1

		horaImp = "0" if self.__min < 10 else ""
		horaImp += str(self.__min)+":"
		horaImp += "0" if self.__seg < 10 else ""
		horaImp += str(self.__seg)

		self.__relojStr.set(horaImp)

	def dibujar(self):
		self.__ventana.mainloop()