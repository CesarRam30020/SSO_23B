import re

class Lote():
	def __init__(self, numLote = 0, procesos = []):
		self.__num = numLote
		self.__procesos = []

	def agregar(self,proceso):
		valido = len(self.__procesos) < 4
		if valido:
			self.__procesos.append(proceso)
		return valido

	def procesos(self):
		return self.__procesos

	def fijaNum(self,num):
		self.__num = num

	def dameNum(self):
		return self.__num

	def lleno(self):
		return len(self.__procesos) >= 4

	def __str__(self):
		s = "Numero de Lote: "+str(self.__num)+"\n"
		s += "Procesos: "+str(len(self.__procesos))+"\n"
		return s

class Proceso():
	def __init__(self,programador,operacion,tiempoMaximoEstimado,noPrograma):
		self.__programador = ""
		self.__operacion = "0/0"
		self.__tiempoEstimadoSegundos = 0
		self.__noPrograma = -1

		self.fijaProgramador(programador)
		self.fijaOperacion(operacion)
		self.fijaTiempoMaximoEstimado(tiempoMaximoEstimado)
		self.fijaNoPrograma(noPrograma)

	def fijaProgramador(self,programador):
		valida = programador != ""
		if valida:
			self.__programador = programador
		return valida

	def fijaOperacion(self,operacion):
		valida = bool(re.match(r"^[0-9]+\.?[0-9]*[+-/*%^][0-9]+\.?[0-9]*$",operacion))
		if valida:
			self.__operacion = operacion
		return valida

	def fijaTiempoMaximoEstimado(self,tiempoMaximoEstimado):
		valida = tiempoMaximoEstimado != "" and float(tiempoMaximoEstimado) > 0
		if valida:
			self.__tiempoEstimadoSegundos = float(tiempoMaximoEstimado)
		return valida

	def fijaNoPrograma(self,noPrograma):
		valida = noPrograma != "" and int(noPrograma) >= 0
		if valida:
			self.__noPrograma = int(noPrograma)
		return valida

	def dameProgramador(self):
		return self.__programador

	def dameOperacion(self):
		return self.__operacion

	def dameTiempoEstimadoSegundos(self):
		return self.__tiempoEstimadoSegundos

	def dameNoPrograma(self):
		return self.__noPrograma

	def resolver(self):
		pos = self.__posOperador()
		operandos = [float(self.__operacion[:pos[0]]),float(self.__operacion[pos[1]:])]
		operador = self.__operacion[pos[0]:pos[1]]
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
		pos = re.search(r"(\+|\-|/|\*|%|\^)",self.__operacion)
		return pos.span()[0],pos.span()[1]

	def valido(self):
		errores = ""
		if self.__programador == "" :
			errores += "Nombre del Programador Invalido\n"
		if self.__operacion == "0/0" or self.__operacion == "":
			errores += "Operacion invalida\n"
		if self.__tiempoEstimadoSegundos == 0:
			errores += "Tiempo Estimado Invalido, debe ser mayor a 0\n"
		if self.__noPrograma == -1:
			errores += "Numero de Programa Invalido, ya existe"
		return len(errores) == 0,errores

	def __str__(self):
		s = "Proceso:\n"
		s += "Programador: "+self.__programador+"\n"
		s += "Operacion: "+self.__operacion+"\n"
		s += "Tiempo Maximo Estimado: "+str(self.__tiempoEstimadoSegundos)+"\n"
		s += "# Programa: "+str(self.__noPrograma)+"\n"
		return s