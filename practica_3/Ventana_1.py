from tkinter import Frame,Label,Entry,Button,StringVar,END,Tk
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
		# self.__lotes: list = []
		self._tecla_estado = ""
		self._interrupcionProceso = ""
		self._tte = 0
		self._tre = 0
		self._loteEjecucion = 0
		self._procesoCompleto = 0
		self._procesosPendientes = False
		self._procesoEnEjecucion = False

		self.__noProgramaSTR = StringVar()
		#self.__lotesPendientesSTR = StringVar()
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
		#self.__lotesPendientesSTR.set("Lotes Pendientes: 0")
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
		# self.__procesosBloqueadosTable = None

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

		# self.__procesosBloqueadosTable = Treeview(self.__midRightFrame,height = 5,columns = ("No","Operación","Tiempo"))
		# self.__procesosBloqueadosTable.grid(row = 3,column = 0,pady = 5,padx = 5)
		# self.__procesosBloqueadosTable.column("#0",width = 1)
		# self.__procesosBloqueadosTable.column("No",width = 50)
		# self.__procesosBloqueadosTable.heading("No",text = "No")
		# self.__procesosBloqueadosTable.column("Operación",width = 100)
		# self.__procesosBloqueadosTable.heading("Operación",text = "Operación")
		# self.__procesosBloqueadosTable.column("Tiempo",width = 100)
		# self.__procesosBloqueadosTable.heading("Tiempo",text = "Tiempo")
		
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
		Button(self.__midLeftFrame,text = "Comienza Emulación",command = lambda:self.__simular_2()).grid(row = 1,column = 0,pady = 5,padx = 5)
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
				print(f"Data {i}: {data} {len(self.__procesosNuevosList)}")
		except ValueError as e:
			mb.showerror("¡¡ERROR!!","Debes ingresar un número en \"Numero de Programas\"")

	# def __simular(self):
	# 	try:
	# 		self.__vaciarTabla(self.__procesosListosTable)
	# 		loteEjecucion = 1
	# 		for lote in self.__lotes:
	# 			#self.__lotesPendientesSTR.set(f"Lotes Pendientes: {len(self.__lotes) - loteEjecucion}")
	# 			loteEjecucion += 1
	# 			# agrega todos los procesos a la tabla del "Lote en Ejecucion"
	# 			for proceso in lote.procesos():
	# 				# Obtiene los datos del Proceso necesarios para agregarlos a la tabla "Lote en Ejecucion"
	# 				data = [proceso.dameNoPrograma(),proceso.dameProgramador(),proceso.dameOperacion(),
	# 					proceso.dameTiempoEstimadoSegundos(),lote.dameNum()]
	# 				# Agrega los datos a la tabla
	# 				self.__aniadeTabla(self.__procesosListosTable,data)
				
	# 			for proceso in lote.procesos():
	# 				# Tiempo Total Ejecutado, comienza en cero por cada proceso que se ejecuta
	# 				TTE = 0
	# 				# Si el TTE es igual al tiempo estimado de ejecucion del proceso, termina el while
	# 				while TTE <= proceso.dameTiempoEstimadoSegundos():
	# 					# Añade los datos del proceso en ejecucion en el apartado de "Proceso en Ejecucion"
	# 					self.__aniadeProcesoEjecucion(proceso,TTE)
	# 					# Actualiza el contenido de la ventana
	# 					self.__ventana.update()
	# 					TTE += 1
	# 					# Mueve el reloj
	# 					self.__reloj()
	# 					sleep(1)
	# 				# Obtiene los datos del Proceso que se "acaba de ejecutar" para despues agregarlo a la table de "Procesos Terminados"
	# 				data = [proceso.dameNoPrograma(),proceso.dameProgramador(),proceso.dameOperacion(),
	# 					proceso.resolver(),proceso.dameTiempoEstimadoSegundos(),lote.dameNum()]
	# 				# Añade el proceso a la tabla de "Procesos Terminados"
	# 				self.__aniadeTabla(self.__procesosTerminadosTable,data)

	# 			# Una vez ya no haya mas procesos para ejecutar, vacia la tabla de "Lote en Ejecucion"
	# 			self.__vaciarTabla(self.__procesosListosTable)
	# 	except IndexError as e:
	# 		mb.showerror(
	# 			"¡¡ERROR!!",
	# 			"Debes ingresar por lo menos 1 proceso"
	# 		)

	def __simular_2(self):
		# self.__vaciarTabla(self.__procesosNuevosTable)
		self.__vaciarTabla(self.__procesosListosTable)
		self._tecla_estado = "c"

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

	""" Este metodo se encargara de actualizar los procesos bloqueados, se realizo de esta forma ya que es mas sencillo actualizar labels que tablas """
	def __actualizaProcesosBloqueados(self):
		for i in range(0,len(self.__procesosBloqueadosList),1):
			proceso = self.__procesosBloqueadosList[i]
			self.__procesosBloqueadosSTR[i].set(f"ID: {proceso.dameNoPrograma()} | Tiempo Bloqueado: {proceso.dameTiempoBloqueado()}")
			self.__ventana.update()

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

	def __obtenerLote(self) -> None:
		if len(self.__lotes) != 0:
			#self.__lotesPendientesSTR.set(f"Lotes Pendientes: {len(self.__lotes) - self._loteEjecucion}")
			self._loteEjecucion += 1
			self._loteTemporal = self.__lotes[0]
			self.__lotes.pop(0)
			for proceso in self._loteTemporal._procesos:
				data = [
					proceso.dameNoPrograma(),
					proceso.dameProgramador(),
					proceso.dameOperacion(),
					proceso.dameTiempoEstimadoSegundos(),
					self._loteTemporal.dameNum()
				]
				self.__aniadeTabla(self.__procesosListosTable, data)
				print(data)
			self.__ventana.update()
			self._procesosPendientes = True
		else:
			#self.__lotesPendientesSTR.set("Lotes Pendientes: 0")
			self._loteEjecucion += 1
			pass
	
	def __obtenerProceso(self) -> None:
		if len(self._loteTemporal._procesos) != 0:
			self._procesoTemporal = self._loteTemporal._procesos[0]
			self._loteTemporal._procesos.pop(0)
			self._procesoEnEjecucion = True
			self._tre = self._procesoTemporal.dameTiempoEstimadoSegundos()
			self._procesoCompleto = int(self._procesoTemporal.dameTiempoEstimadoSegundos()) - 1
		else:
			self._procesosPendientes = False
			pass
	
	def __actualizarVistaProceso(self) -> None:
		if self._tte <= self._procesoTemporal.dameTiempoEstimadoSegundos():
			self.__aniadeProcesoEjecucion(self._procesoTemporal,self._tte)
			self.__ventana.update()
			self._tte += 1
			self._tre -= 1
			self.__reloj()
	
	def __actualizarVistaProcesoTerminado(self) -> None:
		if self._interrupcionProceso == TECLA_ERROR:
			self.__reinicioInterrupcionProceso()
			resultado = "ERROR"
		else:
			resultado = self._procesoTemporal.resolver()

		data = [
			self._procesoTemporal.dameNoPrograma(),
			self._procesoTemporal.dameProgramador(),
			self._procesoTemporal.dameOperacion(),
			resultado,
			self._procesoTemporal.dameTiempoEstimadoSegundos(),
			self._loteTemporal.dameNum()
		]
		self.__aniadeTabla(self.__procesosTerminadosTable, data)
		self._procesoEnEjecucion = False
		self._tte = 0
	
	def __reinicioInterrupcionProceso(self) -> None:
		self._interrupcionProceso = ""
	
	def __reintegracionProcesoInterrumpido(self) -> None:
		self._procesoTemporal._tiempoEstimadoSegundos = self._tre
		self._loteTemporal._procesos.append(self._procesoTemporal)
		data = [
			self._procesoTemporal.dameNoPrograma(),
			self._procesoTemporal.dameProgramador(),
			self._procesoTemporal.dameOperacion(),
			self._procesoTemporal.dameTiempoEstimadoSegundos(),
			self._loteTemporal.dameNum()
		]
		self.__aniadeTabla(self.__procesosListosTable, data)
		self.__ventana.update()

	def __ejecutarProceso(self) -> None:
		# print(self._tte, type(self._tte))
		# print(procesoCompleto, type((procesoCompleto)))
		# print(self._tte != procesoCompleto)
		if self._tte != self._procesoCompleto:
			self.__actualizarVistaProceso()
			if self._interrupcionProceso == TECLA_ERROR:
				self._tte = self._procesoCompleto
			if self._interrupcionProceso == TECLA_INTERRUPCION:
				self.__reintegracionProcesoInterrumpido()
				self.__reinicioInterrupcionProceso()
				self._procesoEnEjecucion = False
		else:
			self.__actualizarVistaProcesoTerminado()

	def __validarEstadoTeclaPrograma(self) -> None:
		try:
			if self._tecla_estado == TECLA_CONTINUAR:
				print("Programa corriendo")
				if self._procesosPendientes:
					if self._tecla_estado == TECLA_INTERRUPCION:
						self._interrupcionProceso = "i"
					elif self._tecla_estado == TECLA_ERROR:
						self._interrupcionProceso = "e"
					
					if self._procesoEnEjecucion:
						self.__ejecutarProceso()
					else:
						self.__obtenerProceso()
					
				else:
					self.__vaciarTabla(self.__procesosListosTable)
					self.__obtenerLote()
			else:
				if self._tecla_estado == TECLA_PAUSAR:
					print("Programa pausado")
					pass
		except Exception as e:
			pass
		finally:
			self.__ventana.after(950, self.__validarEstadoTeclaPrograma)
	
	def key_press(self, event) -> None:
		if event.keysym == TECLA_CONTINUAR:
			self._tecla_estado = TECLA_CONTINUAR
			# print("Key press:", self._tecla_estado)
		elif event.keysym == TECLA_PAUSAR:
			self._tecla_estado = TECLA_PAUSAR
			# print("Key press:", self._tecla_estado)
		elif event.keysym == TECLA_INTERRUPCION:
			self._interrupcionProceso = TECLA_INTERRUPCION
		elif event.keysym == TECLA_ERROR:
			self._interrupcionProceso = TECLA_ERROR
		else:
			# print("Error")
			pass

	def dibujar(self):
		self.__ventana.bind("<KeyPress>", self.key_press)
		self.__ventana.after(100, self.__validarEstadoTeclaPrograma)
		self.__ventana.mainloop()

if __name__ == "__main__":
	ventana = Ventana(Tk())
	ventana.dibujar()