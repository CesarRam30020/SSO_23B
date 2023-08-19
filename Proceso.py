import re

class Proceso():
	def __init__(self,programador,id,operacion,tm):
		self.programador = programador
		self.id = id
		self.operacion = operacion
		self.tm = tm
		pos = self.__posOperador()
		self.__n1 = float(self.operacion[:pos[0]])
		self.__n2 = float(self.operacion[pos[1]:])
		self.__tipo = self.operacion[pos[0]:pos[1]]
		

	def getN1(self):
		return self.__n1
	def getN2(self):
		return self.__n2
	def getTipo(self):
		return self.__tipo

	def setN1(self,n1):
		self.__n1 = n1
	def setN2(self,n2):
		self.__n2 = n2
	def setTipo(se,tipo):
		self.__tipo = tipo

	def resolver(self):
		return self.__resolver([self.__n1,self.__n2],self.__tipo)

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
		pos = re.search(r"(\+|\-|/|\*|%|\^)",self.operacion)
		return pos.span()[0],pos.span()[1]

	def __str__(self):
		s = f"ID: {self.id}\n"
		s += f"operacion: {self.operacion}\n"
		s += f"Tiempo Maximo: {self.tm}\n"
		return s