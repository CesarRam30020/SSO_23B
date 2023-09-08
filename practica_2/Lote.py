import re

MAX_PROCESOS = 3
LOTE_INICIAL = 0
TIEMPO_ESTIMADO_SEGUNDOS_INICIAL = 0
NO_PROGRAMA_INICIAL = -1


class Lote():
	def __init__(self, numLote: int = LOTE_INICIAL, procesos: list = []) -> None:
		self._num : int = numLote
		self._procesos : list = []
		self._maxProcesos = MAX_PROCESOS

	def agregar(self,proceso) -> bool:
		valido = len(self._procesos) < self._maxProcesos
		if valido:
			self._procesos.append(proceso)
		
		return valido

	def procesos(self) -> list:
		return self._procesos

	def fijaNum(self,num) -> int:
		self._num = num

	def dameNum(self):
		return self._num

	def lleno(self) -> bool:
		return len(self._procesos) >= self._maxProcesos
	
	def mueveProcesos(self):
		self._procesos.append(self.__procesos[0])
		self._procesos.pop(0)

	def __str__(self) -> str:
		s = "Numero de Lote: "+str(self._num)+"\n"
		s += "Procesos: "+str(len(self._procesos))+"\n"
		return s


class Proceso():
	def __init__(self,programador="", operacion="0/0", 
				tiempoMaximoEstimado=TIEMPO_ESTIMADO_SEGUNDOS_INICIAL,
				noPrograma=NO_PROGRAMA_INICIAL) -> None:
		self.__programador = ""
		self._operacion = "0/0"
		self._tiempoEstimadoSegundos = TIEMPO_ESTIMADO_SEGUNDOS_INICIAL
		self._noPrograma = NO_PROGRAMA_INICIAL

		self.fijaProgramador(programador)
		self.fijaOperacion(operacion)
		self.fijaTiempoMaximoEstimado(tiempoMaximoEstimado)
		self.fijaNoPrograma(noPrograma)

	def fijaProgramador(self,programador) -> bool:
		valida = programador != ""
		if valida:
			self.__programador = programador
		return valida

	def fijaOperacion(self,operacion) -> bool:
		rgx = r"^[0-9]+\.?[0-9]*[+-/*%^][0-9]+\.?[0-9]*$"
		valida = bool(re.match(rgx, operacion))
		if valida:
			self._operacion = operacion
		return valida

	def fijaTiempoMaximoEstimado(self,tiempoMaximoEstimado) -> bool:
		valida = tiempoMaximoEstimado != "" and float(tiempoMaximoEstimado) > 0
		if valida:
			self._tiempoEstimadoSegundos = float(tiempoMaximoEstimado)
		return valida

	def fijaNoPrograma(self,noPrograma) -> bool:
		valida = noPrograma != "" and int(noPrograma) >= 0
		if valida:
			self._noPrograma = int(noPrograma)
		return valida

	def dameProgramador(self) -> str:
		return self.__programador

	def dameOperacion(self) -> str:
		return self._operacion

	def dameTiempoEstimadoSegundos(self) -> float:
		return self._tiempoEstimadoSegundos

	def dameNoPrograma(self) -> int:
		return self._noPrograma

	def resolver(self):
		pos = self.__posOperador()
		operandos = [float(self._operacion[:pos[0]]),float(self._operacion[pos[1]:])]
		operador = self._operacion[pos[0]:pos[1]]
		return self.__resolver(operandos,operador)

	def __resolver(self,operandos,operador):
		if operador == "+":
			return operandos[0] + operandos[1]
		if operador == "-":
			return operandos[0] - operandos[1]
		if operador == "/":
			return operandos[0] / operandos[1]
		if operador == "*":
			return operandos[0] * operandos[1]
		if operador == "%":
			return operandos[0] % operandos[1]
		if operador == "^":
			return operandos[0] ** operandos[1]
		return 0

	def __posOperador(self):
		pos = re.search(r"(\+|\-|/|\*|%|\^)",self._operacion)
		return pos.span()[0],pos.span()[1]

	def valido(self):
		errores = ""
		if self.__programador == "" :
			errores += "Nombre del Programador Invalido\n"
		if self._operacion == "0/0" or self._operacion == "":
			errores += "Operacion invalida\n"
		if self._tiempoEstimadoSegundos == 0:
			errores += "Tiempo Estimado Invalido, debe ser mayor a 0\n"
		if self._noPrograma == -1:
			errores += "Numero de Programa Invalido, ya existe"
		return len(errores) == 0,errores

	def __str__(self):
		s = "Proceso:\n"
		s += "Programador: "+self.__programador+"\n"
		s += "Operacion: "+self._operacion+"\n"
		s += "Tiempo Maximo Estimado: "+str(self._tiempoEstimadoSegundos)+"\n"
		s += "# Programa: "+str(self._noPrograma)+"\n"
		return s
