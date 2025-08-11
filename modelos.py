import numpy as np
from scipy.integrate import quad

class ModeloTermodinamico:
	"""
	Clase base abstracta para modelos termodinámicos.

	Métodos:
		resolver_xxxxxx(self, estado_in, estado_out, **kwargs): Resuelve el respectivo proceso, tal que se definan las variables termodinámicas de cada estado.
		calcular_estado(estado, **kwargs): Calcula las propiedades termodinámicas de un estado.
	"""

	def resolver_isocorico(self, estado_in, estado_out):
		'''
		Esta función relaciona dos estados a través de un proceso isocórico o a volumen constante.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
		'''
		# Definir alguno de los estados involucrados si es posible:
		if sum(value is not None for value in vars(estado_in).values()) >= 2:
			if sum(value is not None for value in vars(estado_in).values()) ==6:
				print(f"{estado_in.nombre} esta definido")
			else:
				self.calcular_estado(estado_in)
		elif sum(value is not None for value in vars(estado_out).values()) >= 2:
			if sum(value is not None for value in vars(estado_out).values()) ==6:
				print(f"{estado_out.nombre} esta definido")
			else:
				self.calcular_estado(estado_out)

		# Ambos están definidos
		if estado_in.v is not None and estado_out.v is not None:
			if estado_in.v == estado_out.v:
				print(f"Los volúmenes de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidos y son iguales.")
			else:
				print(f"Los volúmenes de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidos pero no son iguales. Se recomienda revisar.")

		# Solo el estado_in tiene volumen definido
		elif estado_in.v is not None:
			estado_out.v = estado_in.v

		# Solo el estado_out tiene volumen definido
		elif estado_out.v is not None:
			estado_in.v = estado_out.v

		# Ninguno tiene volumen definido
		else:
			print(f"Ninguno de los estados {estado_in.nombre} ni {estado_out.nombre} tiene el volumen definido. Se requiere al menos uno.")

	def resolver_isotermico(self, estado_in, estado_out):
		'''
		Esta función relaciona dos estados a través de un proceso isotermico o a temperatura constante.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
		'''
		# Definir alguno de los estados involucrados si es posible:
		if sum(value is not None for value in vars(estado_in).values()) >= 2:
			if sum(value is not None for value in vars(estado_in).values()) ==6:
				print(f"{estado_in.nombre} esta definido")
			else:
				self.calcular_estado(estado_in)
		elif sum(value is not None for value in vars(estado_out).values()) >= 2:
			if sum(value is not None for value in vars(estado_out).values()) ==6:
				print(f"{estado_out.nombre} esta definido")
			else:
				self.calcular_estado(estado_out)

		# Ambos están definidos
		if estado_in.T is not None and estado_out.T is not None:
			if estado_in.T == estado_out.T:
				print(f"Las temperaturas de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas y son iguales.")
			else:
				print(f"Las temperaturas de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas pero no son iguales. Se recomienda revisar.")

		# Solo el estado_in tiene volumen definido
		elif estado_in.T is not None:
			estado_out.T = estado_in.T

		# Solo el estado_out tiene volumen definido
		elif estado_out.T is not None:
			estado_in.T = estado_out.T

		# Ninguno tiene volumen definido
		else:
			print(f"Ninguno de los estados {estado_in.nombre} ni {estado_out.nombre} tiene la temperatura definida. Se requiere al menos una.")

	def resolver_isobarico(self,estado_in, estado_out):
		'''
		Esta función relaciona dos estados a través de un proceso isobarico o a presión constante.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
		'''
		# Definir alguno de los estados involucrados si es posible:
		if sum(value is not None for value in vars(estado_in).values()) >= 2:
			if sum(value is not None for value in vars(estado_in).values()) ==6:
				print(f"{estado_in.nombre} esta definido")
			else:
				self.calcular_estado(estado_in)
		elif sum(value is not None for value in vars(estado_out).values()) >= 2:
			if sum(value is not None for value in vars(estado_out).values()) ==6:
				print(f"{estado_out.nombre} esta definido")
			else:
				self.calcular_estado(estado_out)

		if estado_in.P is not None and estado_out.P is not None:
			if estado_in.P == estado_out.P:
				print(f"Las presiones de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas y son iguales.")
			else:
				print(f"Las presiones de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas pero no son iguales. Se recomienda revisar.")

		# Solo el estado_in tiene volumen definido
		elif estado_in.P is not None:
			estado_out.P = estado_in.P

		# Solo el estado_out tiene volumen definido
		elif estado_out.P is not None:
			estado_in.P = estado_out.P

		# Ninguno tiene volumen definido
		else:
			print(f"Ninguno de los estados {estado_in.nombre} ni {estado_out.nombre} tiene la presión definida. Se requiere al menos una.")

	def resolver_isoentalpico(self, estado_in, estado_out):
		'''
		Esta función relaciona dos estados a través de un proceso isoentalpico o a entalpía constante.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
		'''
		# Definir alguno de los estados involucrados si es posible:
		if sum(value is not None for value in vars(estado_in).values()) >= 2:
			if sum(value is not None for value in vars(estado_in).values()) ==6:
				print(f"{estado_in.nombre} esta definido")
			else:
				self.calcular_estado(estado_in)
		elif sum(value is not None for value in vars(estado_out).values()) >= 2:
			if sum(value is not None for value in vars(estado_out).values()) ==6:
				print(f"{estado_out.nombre} esta definido")
			else:
				self.calcular_estado(estado_out)

		# Ambos están definidos
		if estado_in.h is not None and estado_out.h is not None:
			if estado_in.h == estado_out.h:
				print(f"Las entalpias de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas y son iguales.")
			else:
				print(f"Las entalpias de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas pero no son iguales. Se recomienda revisar.")

		# Solo el estado_in tiene volumen definido
		elif estado_in.h is not None:
			estado_out.h = estado_in.h

		# Solo el estado_out tiene volumen definido
		elif estado_out.h is not None:
			estado_in.h = estado_out.h

		# Ninguno tiene volumen definido
		else:
			print(f"Ninguno de los estados {estado_in.nombre} ni {estado_out.nombre} tiene la entalpía definida. Se requiere al menos una.")

	def resolver_isoentropico(self, estado_in, estado_out):
		'''
		Esta función relaciona dos estados a través de un proceso isoentropico o a entropía constante.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
		'''
		# Definir alguno de los estados involucrados si es posible:
		if sum(value is not None for value in vars(estado_in).values()) >= 2:
			if sum(value is not None for value in vars(estado_in).values()) ==6:
				print(f"{estado_in.nombre} esta definido")
			else:
				self.calcular_estado(estado_in)
		elif sum(value is not None for value in vars(estado_out).values()) >= 2:
			if sum(value is not None for value in vars(estado_out).values()) ==6:
				print(f"{estado_out.nombre} esta definido")
			else:
				self.calcular_estado(estado_out)

		# Ambos están definidos
		if estado_in.s is not None and estado_out.s is not None:
			if estado_in.s == estado_out.s:
				print(f"Las entropías de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas y son iguales.")
			else:
				print(f"Las entropías de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas pero no son iguales. Se recomienda revisar.")

		# Solo el estado_in tiene volumen definido
		elif estado_in.s is not None:
			estado_out.s = estado_in.s

		# Solo el estado_out tiene volumen definido
		elif estado_out.s is not None:
			estado_in.s = estado_out.s

		# Ninguno tiene volumen definido
		else:
			print(f"Ninguno de los estados {estado_in.nombre} ni {estado_out.nombre} tiene la entropía definida. Se requiere al menos una.")

	def resolver_politropico(self, estado_in, estado_out, n):
		raise NotImplementedError()

	def resolver_in_or_out_calor(self, estado_in, estado_out, calor):
		'''
		Esta función relaciona dos estados a través de agregar o sacar calor a temperatura constante.

		La funcion maneja la convencion de que el calor entrante es positivo y el calor saliente es negativo.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
		'''
		# Definir alguno de los estados involucrados si es posible:
		if sum(value is not None for value in vars(estado_in).values()) >= 2:
			if sum(value is not None for value in vars(estado_in).values()) ==6:
				print(f"{estado_in.nombre} esta definido")
			else:
				self.calcular_estado(estado_in)
		elif sum(value is not None for value in vars(estado_out).values()) >= 2:
			if sum(value is not None for value in vars(estado_out).values()) ==6:
				print(f"{estado_out.nombre} esta definido")
			else:
				self.calcular_estado(estado_out)

		# Revisar que las temperatura de los estados sean la misma

		# Ambos están definidos
		if estado_in.T is not None and estado_out.T is not None:
			if estado_in.T == estado_out.T:
				print(f"Las temperaturas de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas y son iguales.")
			else:
				print(f"Las temperaturas de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas pero no son iguales. Se recomienda revisar.")

		# Solo el estado_in tiene temperatura definido
		elif estado_in.T is not None:
			estado_out.T = estado_in.T

		# Solo el estado_out tiene temperatura definido
		elif estado_out.T is not None:
			estado_in.T = estado_out.T

		# Ninguno tiene volumen definido
		else:
			print(f"Ninguno de los estados {estado_in.nombre} ni {estado_out.nombre} tiene la temperatura definida. Se requiere al menos una.")

	""" def resolver_interenfriamiento_recalentamiento(self, estado_in, estado_out, delta_T):
		'''
		Esta función relaciona dos estados a través de agregar o sacar calor con un cambio conocido de T.

		La funcion maneja la convencion de que el calor entrante es positivo y el calor saliente es negativo.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
			delta_T (float): Cambio de temperatura estado_out.T - estado_in.T.
		'''
		# Definir alguno de los estados involucrados si es posible:
		if sum(value is not None for value in vars(estado_in).values()) >= 2:
			if sum(value is not None for value in vars(estado_in).values()) ==6:
				print(f"{estado_in.nombre} esta definido")
			else:
				self.calcular_estado(estado_in)
		elif sum(value is not None for value in vars(estado_out).values()) >= 2:
			if sum(value is not None for value in vars(estado_out).values()) ==6:
				print(f"{estado_out.nombre} esta definido")
			else:
				self.calcular_estado(estado_out)

		# Revisar que las temperatura de los estados sean la misma

		# Ambos están definidos
		if estado_in.T is not None and estado_out.T is not None:
			if (estado_in.T - estado_out.T) < 1e-6:
				print(f"Las temperaturas de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas y son iguales. Se recomienda revisar, no es el comportamiento esperado para este proceso.")
				if estado_in.P is not None and estado_out.P is not None:
					if (estado_in.P - estado_out.P)<1e-6:
						print(f"Las presiones de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidos y son iguales. Correcto para un proceso de interenfriamiento o recalentamiento")
						print("No es posible calcular el proceso ni definir los estados.")
					else:
						print(f"Las presiones de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidos y NO SON IGUALES. NO ES congruente con el proceso de interenfriamiento o recalentamiento")
						print("No es posible calcular el proceso ni definir los estados.")
			else:
				print(f"Las temperaturas de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas pero no son iguales. Es un comportamiento esperado.")
				if estado_in.P is not None and estado_out.P is not None:
					if (estado_in.P - estado_out.P)<1e-6:
						print(f"Las presiones de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidos y son iguales. Correcto para un proceso de interenfriamiento o recalentamiento")
					else:
						print(f"Las presiones de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidos y NO SON IGUALES. NO ES congruente con el proceso de interenfriamiento o recalentamiento")
				elif estado_in.P is not None:
					estado_out.P = estado_in.P
					self.calcular_estado(estado_in)
					self.calcular_estado(estado_out)
				elif estado_out.P is not None:
					estado_in.P = estado_out.P
					self.calcular_estado(estado_in)
					self.calcular_estado(estado_out)

		# Solo el estado_in tiene temperatura definido
		elif estado_in.T is not None:
			estado_out.T = estado_in.T + delta_T
			if estado_in.P is not None and estado_out.P is not None:
					if (estado_in.P - estado_out.P)<1e-6:
						self.calcular_estado(estado_in)
						self.calcular_estado(estado_out)
			elif estado_in.P is not None:
					estado_out.P = estado_in.P
					self.calcular_estado(estado_in)
					self.calcular_estado(estado_out)
			elif estado_out.P is not None:
					estado_in.P = estado_out.P
					self.calcular_estado(estado_in)
					self.calcular_estado(estado_out)

		# Solo el estado_out tiene temperatura definido
		elif estado_out.T is not None:
			estado_in.T = estado_out.T - delta_T
			if estado_in.P is not None and estado_out.P is not None:
					if (estado_in.P - estado_out.P)<1e-6:
						self.calcular_estado(estado_in)
						self.calcular_estado(estado_out)
			elif estado_in.P is not None:
					estado_out.P = estado_in.P
					self.calcular_estado(estado_in)
					self.calcular_estado(estado_out)
			elif estado_out.P is not None:
					estado_in.P = estado_out.P
					self.calcular_estado(estado_in)
					self.calcular_estado(estado_out)

		# Ninguno tiene volumen definido
		else:
			print(f"Ninguno de los estados {estado_in.nombre} ni {estado_out.nombre} tiene la temperatura y la presion definida. Se requiere al menos una de cada una.")
"""


	def calcular_estado(self, estado, **kwargs):
		"""
		Método abstracto para calcular las propiedades de un estado.

		Args:
			estado (Estado): Objeto Estado a actualizar.
			**kwargs: Propiedades conocidas del estado (por ejemplo, P, T, v...).

		Raises:
			NotImplementedError: Si no se implementa en una subclase.
		"""
		raise NotImplementedError("Este método debe ser implementado en una subclase.")



class ModeloGasIdeal(ModeloTermodinamico):
	r"""
	Modelo de gas ideal con capacidades caloríficas constantes. Configurado por defecto para el aire.

	La ecuación del gas ideal usada es: $P\upsilon = R_{gas}T$ con $R_{gas} = \frac{R}{M_{gas}}$.

	$R$: Constante universal de gases.

	$M_{gas}$: Masa molar del gas.

	Args:
		calores_constantes (bool): `True` si se desea usar calores constantes, `False` si se desean utilizar variables respecto a T.
		R_gas (float): Constante del gas usado [J/kg·K].
		cp (float | callable | sympy.Expr): Capacidad calorífica específica a presión constante. 
			Puede ser:
				- Un valor constante (`float`) [J/kg·K].
				- Una expresión matemática (ej. `sympy.Expr`) que dependa de variables como `T`.
				- Una función (`callable`) que reciba la temperatura y devuelva el valor numérico.
		cv (float | callable | sympy.Expr): Capacidad calorífica específica a volumen constante. 
			Puede ser:
				- Un valor constante (`float`) [J/kg·K].
				- Una expresión matemática (ej. `sympy.Expr`) que dependa de variables como `T`.
				- Una función (`callable`) que reciba la temperatura y devuelva el valor numérico.
		T0 (float): Temperatura de referencia [K].
		P0 (float): Presión de referencia [Pa].

	Métodos:
		calcular_estado(estado, **kwargs): Calcula propiedades del estado con base en combinaciones de propiedades conocidas.
	"""

	def __init__(self, calores_constantes = True, R_gas=287, cp=1005, cv = 0.718, T0=298.15, P0=101325):
		self.calores_constantes = calores_constantes
		self.R_gas = float(R_gas)
		if self.calores_constantes == True:
			self.cp = float(cp)
			self.cv = float(cv) if cv is not None else self.cp - self.R_gas
		elif self.calores_constantes == False:
			self.cp = cp
			self.cv = cv
		else:
			print("Se debe asignar si se desea trabajar con calores específicos constantes o variables dependientes de T")
		self.T0 = float(T0)
		self.P0 = float(P0)
		self.v0 = self.R_gas*self.T0/self.P0  # volumen específico de referencia



	def resolver_isocorico(self, estado_in, estado_out):
		super().resolver_isocorico(estado_in, estado_out)
		# Gas ideal
		self.calcular_estado(estado_in)
		self.calcular_estado(estado_out)
		def isocorico_ModeloGasIdeal(P):
			"""
			Retorna la temperatura T para un gas ideal en un proceso isocórico, dado P.
			"""
			P = np.asarray(P)  # Asegura que P se pueda vectorizar
			return estado_in.v*P/self.R_gas
		return isocorico_ModeloGasIdeal

	def resolver_isotermico(self, estado_in, estado_out, **kwargs):
		super().resolver_isotermico(estado_in, estado_out)
		# Gas ideal
		self.calcular_estado(estado_in)
		self.calcular_estado(estado_out)
		def isotermico_ModeloGasIdeal(v):
			"""
			Retorna la presión P para un gas ideal en un proceso isotermico, dado v.
			"""
			v = np.asarray(v)
			return (self.R_gas*estado_in.T)/v
		return isotermico_ModeloGasIdeal

	def resolver_isobarico(self, estado_in, estado_out):
		super().resolver_isobarico(estado_in, estado_out)
		# Gas ideal
		self.calcular_estado(estado_in)
		self.calcular_estado(estado_out)
		def isobarico_ModeloGasIdeal(v):
			"""
			Retorna la temperatura T para un gas ideal en un proceso isobarico, dado v.
			"""
			v = np.asarray(v)
			return (estado_in.P/self.R_gas)*v
		return isobarico_ModeloGasIdeal


	def resolver_isoentalpico(self, estado_in, estado_out):
		super().resolver_isoentalpico(estado_in, estado_out)
		# Gas ideal
		self.calcular_estado(estado_in)
		self.calcular_estado(estado_out)
		# En gases ideales, los procesos isoentalpicos siguen isotermas

		# Ambos están definidos
		if estado_in.T is not None and estado_out.T is not None:
			if estado_in.T == estado_out.T:
				print(f"Las temperaturas de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas y son iguales.")
			else:
				print(f"Las temperaturas de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidas pero no son iguales. Se recomienda revisar.")

		# Solo el estado_in tiene volumen definido
		elif estado_in.T is not None:
			estado_out.T = estado_in.T

		# Solo el estado_out tiene volumen definido
		elif estado_out.T is not None:
			estado_in.T = estado_out.T

		# Ninguno tiene volumen definido
		else:
			print(f"Ninguno de los estados {estado_in.nombre} ni {estado_out.nombre} tiene la temperatura definida. Se requiere al menos una.")

		def isoentalpico_ModeloGasIdeal(v):
			"""
			Retorna la presión P para un gas ideal en un proceso isoentalpico -> isotermico, dado v.
			"""
			v = np.asarray(v)
			return (self.R_gas*estado_in.T)/v
		return isoentalpico_ModeloGasIdeal

	def resolver_isoentropico(self, estado_in, estado_out):
		super().resolver_isoentropico(estado_in, estado_out)
		# Gas ideal
		self.calcular_estado(estado_in)
		self.calcular_estado(estado_out)
		def isoentropico_ModeloGasIdeal(v):
			"""
			Retorna la presión P para un gas ideal en un proceso isoentropico, dado v.
			"""
			# Ambos están definidos
			v = np.asarray(v)
			if estado_in.v is not None:
				if estado_in.P is not None:
					return estado_in.P*(estado_in.v/v)**(self.cp/self.cv)
				else:
					print("ERROR: No estan definida la presion en el estado de entrada")
					return None
			elif estado_out.v is not None:
				if estado_out.P is not None:
					return  estado_out.P*(estado_out.v/v)**(self.cp/self.cv)
				else:
					print("ERROR: No estan definida la presion en el estado de salida")
					return None
			else:
				print("ERROR: No estan definidos los volumenes")
				return None
		return isoentropico_ModeloGasIdeal


	def resolver_in_or_out_calor(self, estado_in, estado_out, calor):
		super().resolver_in_or_out_calor(estado_in, estado_out, calor)
		# Gas ideal
		# La entropia
		if estado_in.s is not None and estado_out.s is not None:
			if estado_in.s == estado_out.s:
				print(f"Las entropias de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidos y son iguales. Esto es un error, agragar o sacar calor cambia la entropia.")
			else:
				if (estado_in.s -(estado_out.s + calor/estado_out.T)< 1e-6):
					print(f"Las entropias de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidos pero no son iguales. Son congruentes con el cambio esperado")
				else:
					print(f"Las entropias de los estados {estado_in.nombre} y {estado_out.nombre} fueron definidos pero no son iguales. NO SON congruentes con el cambio esperado " + r"$\Delta$ s =" + f"{estado_in.s - estado_out.s}" + r"Q/T =" +f"{calor/estado_out.T}")

		# Solo el estado_in tiene volumen definido
		elif estado_in.s is not None:
			estado_out.s =  estado_in.s + calor/estado_out.T
			self.calcular_estado(estado_in)
			self.calcular_estado(estado_out)

		# Solo el estado_out tiene volumen definido
		elif estado_out.s is not None:
			estado_in.s = estado_out.s - calor/estado_out.T
			self.calcular_estado(estado_in)
			self.calcular_estado(estado_out)

		# Ninguno tiene volumen definido
		else:
			print(f"Ninguno de los estados {estado_in.nombre} ni {estado_out.nombre} puede ser definido.")

		def in_or_out_calor_ModeloGasIdeal(v):
			"""
			Retorna la presión P para un gas ideal en un proceso de adicion o rechazo de calor -> isotermico, dado v.
			"""
			v = np.asarray(v)
			return (self.R_gas*estado_in.T)/v
		return in_or_out_calor_ModeloGasIdeal

	""" def resolver_interenfriamiento_recalentamiento(self, estado_in, estado_out, delta_T):
		super().resolver_interenfriamiento_recalentamiento(estado_in, estado_out, delta_T)
		# Gas ideal

		def interenfriamiento_recalentamiento_ModeloGasIdeal(v):
			'''
			Retorna la presión T para un gas ideal en un proceso de adicion o rechazo de calor, dado v.
			'''
			v = np.asarray(v)
			return (estado_in.P/self.R_gas)*v
		return interenfriamiento_recalentamiento_ModeloGasIdeal """

	def resolver_politropico(self, estado_in, estado_out, n, **kwargs):
		super().resolver_politropico(estado_in, estado_out)
		# Gas ideal

	def calcular_estado(self, estado):
		"""
		Calcula las propiedades del estado en función de combinaciones de propiedades conocidas.

		Combinaciones aceptables:
		- (P, T)
		- (P, v)
		- (T, v)
		- (P, h)
		- (s,v)
		- (s,P)
		- (T, s)

		Args:
			estado (Estado): Instancia del estado a calcular.
			**kwargs: Combinaciones posibles de propiedades como 'P', 'T', 'v', 'h', 's'.

		Raises:
			ValueError: Si la combinación de propiedades no es soportada.
		"""

		# A continuacion se presentan los casos que va a revisar el programa si se tiene los datos y calcula los datos faltantes si es posible

		# Solucionador para calores especificos constantes
		if self.calores_constantes == True:

			# Caso 1: Conozco Presión (P) y Temperatura (T)
			if (estado.P is not None) and (estado.T is not None):
				estado.v = self.R_gas * estado.T / estado.P
				estado.u = self.cv*(estado.T - self.T0)
				estado.h = self.cp * (estado.T - self.T0)
				estado.s = self.cp * np.log(estado.T / self.T0) - self.R_gas * np.log(estado.P / self.P0)

			# Caso 2: Conozco Presión (P) y Volumen (v)
			elif (estado.P is not None) and (estado.v is not None):
				estado.T = estado.P * estado.v / self.R_gas
				estado.u = self.cv*(estado.T - self.T0)
				estado.h = self.cp * (estado.T - self.T0)
				estado.s = self.cp * np.log(estado.T / self.T0) - self.R_gas * np.log(estado.P / self.P0)

			# Caso 3: Conozco Temperatura (T) y Volumen (v)
			elif (estado.T is not None) and (estado.v is not None):
				estado.P = self.R_gas * estado.T / estado.v
				estado.u = self.cv*(estado.T - self.T0)
				estado.h = self.cp * (estado.T - self.T0)
				estado.s = self.cp * np.log(estado.T / self.T0) - self.R_gas * np.log(estado.P / self.P0)

			# Caso 4: Conozco Presión (P) y Entalpía (h)
			elif (estado.P is not None) and (estado.h is not None):
				estado.T = estado.h / self.cp
				estado.u = self.cv*(estado.T - self.T0)
				estado.v = self.R_gas * estado.T / estado.P
				estado.s = self.cp * np.log(estado.T / self.T0) - self.R_gas * np.log(estado.P / self.P0)

			# Caso 5: Conozco Entropía (s) y Volumen (v)
			elif (estado.s is not None) and (estado.v is not None):
				estado.T = self.T0*np.exp((1/self.cv)*(estado.s-self.R_gas*np.log(estado.v/self.v0)))
				estado.P = self.R_gas * estado.T / estado.v
				estado.u = self.cv*(estado.T - self.T0)
				estado.h = self.cp * (estado.T - self.T0)

			# Caso 6: Conozco Entropía (s) y Presion (P)
			elif (estado.s is not None) and (estado.P is not None):
				estado.T = self.T0*np.exp((1/self.cp)*(estado.s+self.R_gas*np.log(estado.P/self.P0)))
				estado.v = self.R_gas * estado.T / estado.P
				estado.u = self.cv*(estado.T - self.T0)
				estado.h = self.cp * (estado.T - self.T0)

			# Caso 7: Conozco Entropía (s) y Temperatura (T)
			elif (estado.s is not None) and (estado.T is not None):
				estado.P = self.P0*np.exp((1/self.R_gas)*(self.cp*np.log(estado.T/self.T0)-estado.s))
				estado.v = self.R_gas * estado.T / estado.P
				estado.u = self.cv*(estado.T - self.T0)
				estado.h = self.cp * (estado.T - self.T0)

			else:
				print(f"Combinación de propiedades no soportada o insuficiente.")

		# Solucionador para calores especificos variables dependientes de la temperatura
		elif self.calores_constantes == False:

			# Caso 1: Conozco Presión (P) y Temperatura (T)
			if (estado.P is not None) and (estado.T is not None):
				estado.v = self.R_gas * estado.T / estado.P
				estado.u = quad(self.cv, self.T0, estado.T)
				estado.h = quad(self.cp, self.T0, estado.T)
				estado.s = quad(self.cp,self.T0,estado.T) - self.R_gas * np.log(estado.P / self.P0)

			# Caso 2: Conozco Presión (P) y Volumen (v)
			elif (estado.P is not None) and (estado.v is not None):
				estado.T = estado.P * estado.v / self.R_gas
				estado.u = quad(self.cv, self.T0, estado.T)
				estado.h = quad(self.cp, self.T0, estado.T)
				estado.s = quad(self.cp,self.T0,estado.T) - self.R_gas * np.log(estado.P / self.P0)

			# Caso 3: Conozco Temperatura (T) y Volumen (v)
			elif (estado.T is not None) and (estado.v is not None):
				estado.P = self.R_gas * estado.T / estado.v
				estado.u = quad(self.cv, self.T0, estado.T)
				estado.h = quad(self.cp, self.T0, estado.T)
				estado.s = quad(self.cp,self.T0,estado.T) - self.R_gas * np.log(estado.P / self.P0)

			# Caso 4: Conozco Presión (P) y Entalpía (h)
			elif (estado.P is not None) and (estado.h is not None):
				estado.T = estado.h / self.cp
				estado.u = quad(self.cv, self.T0, estado.T)
				estado.v = self.R_gas * estado.T / estado.P
				estado.s = quad(self.cp,self.T0,estado.T) - self.R_gas * np.log(estado.P / self.P0)

			# Caso 5: Conozco Entropía (s) y Volumen (v)
			elif (estado.s is not None) and (estado.v is not None):
				estado.T = self.T0*np.exp((1/self.cv)*(estado.s-self.R_gas*np.log(estado.v/self.v0)))
				estado.P = self.R_gas * estado.T / estado.v
				estado.u = quad(self.cv, self.T0, estado.T)
				estado.h = quad(self.cp, self.T0, estado.T)

			# Caso 6: Conozco Entropía (s) y Presion (P)
			elif (estado.s is not None) and (estado.P is not None):
				estado.T = self.T0*np.exp((1/self.cp)*(estado.s+self.R_gas*np.log(estado.P/self.P0)))
				estado.v = self.R_gas * estado.T / estado.P
				estado.u = quad(self.cv, self.T0, estado.T)
				estado.h = quad(self.cp, self.T0, estado.T)

			# Caso 7: Conozco Entropía (s) y Temperatura (T)
			elif (estado.s is not None) and (estado.T is not None):
				estado.P = self.P0*np.exp((1/self.R_gas)*(self.cp*np.log(estado.T/self.T0)-estado.s))
				estado.v = self.R_gas * estado.T / estado.P
				estado.u = quad(self.cv, self.T0, estado.T)
				estado.h = quad(self.cp, self.T0, estado.T)

			else:
				print(f"Combinación de propiedades no soportada o insuficiente.")

			

from scipy.optimize import fsolve

######################################
######################################
######################################
#           Cocinando
######################################
######################################
######################################

class ModeloVanDerWaals(ModeloTermodinamico):
	"""
	Modelo termodinámico basado en la ecuación de Van der Waals.

	Parámetros
	----------
	a : float
		Constante de atracción (Pa·m⁶/kg²).
	b : float
		Volumen excluido por mol (m³/kg).
	R_gas : float, opcional
		Constante del gas 
	cp (float | callable | sympy.Expr): Capacidad calorífica específica a presión constante. 
			Puede ser:
				- Un valor constante (`float`) [J/kg·K].
				- Una expresión matemática (ej. `sympy.Expr`) que dependa de variables como `T`.
				- Una función (`callable`) que reciba la temperatura y devuelva el valor numérico.
	cv (float | callable | sympy.Expr): Capacidad calorífica específica a volumen constante. 
			Puede ser:
				- Un valor constante (`float`) [J/kg·K].
				- Una expresión matemática (ej. `sympy.Expr`) que dependa de variables como `T`.
				- Una función (`callable`) que reciba la temperatura y devuelva el valor numérico.
	T0 : float, opcional
		Temperatura de referencia (K).
	P0 : float, opcional
		Presión de referencia (Pa).
	MM : float, opcional
		Masa Molar de la sustancia
	"""

	def __init__(self, a, b, R_gas=8.314, cp, cv, T0=298.15, P0=101325, MM = 0.018):
		self.a = a
		self.b = b
		self.R_gas = R_gas
		self.cp = cp
		self.cv = cv
		self.T0 = T0
		self.P0 = P0
		self.v0 = self.R_gas * self.T0 / self.P0  # volumen molar de referencia (ideal)
		self.MM = MM

	def calcular_estado(self, estado):
		"""
		Calcula las propiedades del estado para un gas de Van der Waals
		en función de combinaciones de propiedades conocidas.

		Combinaciones aceptables:
		- (P, T)
		- (P, v)
		- (T, v)
		- (P, h)
		- (s, v)
		- (s, P)
		- (T, s)
		- (P, x)  # Calidad
		- (T, x)  # Calidad

		Args:
			estado (Estado): Instancia del estado a calcular.

		Raises:
			ValueError: Si la combinación de propiedades no es soportada o insuficiente.
		"""

	

		# Función auxiliar para resolver T desde P y v usando Van der Waals
		def calcular_T(P, v):
			return (P + self.a / v**2) * (v - self.b) / self.R_gas

		# Función auxiliar para resolver P desde T y v
		def calcular_P(T, v):
			return self.R_gas * T / (v - self.b) - self.a / v**2
		
		def resolver_volumen(self,estado, T, P):
			"""
			args : T,P
				Temperatura y Presión en ese punto
			returns: v_solution
				(np Array) Si es solo gas, devuelve el volumen del gas
				Si es una mezcla líquido/gas devuelve una lista, de la forma
				[v_líquido,v_gas.v_total]
			"""
			if self.x == 1:
			# Resuelve numéricamente el volumen molar usando fsolve
			#Esto es para casos que no tienen estados mixtos
				def f(v):
					return P - self._presion(T, v)
				v_guess = self.R_gas * T / P  # estimación inicial (gas ideal)
				v_solution = fsolve(f, v_guess)
			else:
			#La ecuación de Van der Waals puede ser expresada de esta forma:
			#PV**3 - (Pb+RT)*V**2 + a*V - a*b = 0.
			#Al resolver para el volumen se tienen tres soluciones:
			#La solución más grande corresponde al volumen del gas
			#La solución más pequeña corresponde al volumen del líquido
			#La solución del intermedio no tiene significado físico
				sol = np.roots([P,-(P*self.b+self.R_gas*T), self.a, -self.a*self.b])
				sol.sort()
				if self.MM == 0.018:
					print(f"Usando Masa Molar del agua: {self.MM}")
				v_liquid = sol[0]/self.MM
				v_gas = sol[-1]/self.MM
				v_solution = [v_liquid, v_gas, v_liquid + estado.x*(v_gas - v_liquid)]

			return v_solution

		
		# Ahora los casos:
		if self.calores_constantes == True:

			# Caso 1: (P, T)
			if (estado.P is not None) and (estado.T is not None):
				estado.v = calcular_v(estado.P, estado.T)
				estado.u = self.cv * (estado.T - self.T0) - self.a / estado.v
				estado.h = estado.u + estado.P * estado.v
				estado.s = self.cp * np.log(estado.T / self.T0) - self.R_gas * np.log((estado.v - self.b) / (self.v0 - self.b))

			# Caso 2: (P, v)
			elif (estado.P is not None) and (estado.v is not None):
				estado.T = calcular_T(estado.P, estado.v)
				estado.u = self.cv * (estado.T - self.T0) - self.a / estado.v
				estado.h = estado.u + estado.P * estado.v
				estado.s = self.cp * np.log(estado.T / self.T0) - self.R_gas * np.log((estado.v - self.b) / (self.v0 - self.b))

			# Caso 3: (T, v)
			elif (estado.T is not None) and (estado.v is not None):
				estado.P = calcular_P(estado.T, estado.v)
				estado.u = self.cv * (estado.T - self.T0) - self.a / estado.v
				estado.h = estado.u + estado.P * estado.v
				estado.s = self.cp * np.log(estado.T / self.T0) - self.R_gas * np.log((estado.v - self.b) / (self.v0 - self.b))

			# Caso 4: (P, h)
			elif (estado.P is not None) and (estado.h is not None):
				# Para este caso es necesario un método iterativo para encontrar T:
				from scipy.optimize import root_scalar

				def f(T):
					v = calcular_v(estado.P, T)
					u = self.cv * (T - self.T0) - self.a / v
					h_calc = u + estado.P * v
					return h_calc - estado.h

				sol = root_scalar(f, bracket=[self.T0, 2000], method='brentq')
				if not sol.converged:
					raise ValueError("No se pudo encontrar temperatura para P y h dados.")
				estado.T = sol.root
				estado.v = calcular_v(estado.P, estado.T)
				estado.u = self.cv * (estado.T - self.T0) - self.a / estado.v
				estado.s = self.cp * np.log(estado.T / self.T0) - self.R_gas * np.log((estado.v - self.b) / (self.v0 - self.b))

			# Caso 5: (s, v)
			elif (estado.s is not None) and (estado.v is not None):
				# Se debe encontrar T que satisface s:
				from scipy.optimize import root_scalar

				def f(T):
					s_calc = self.cp * np.log(T / self.T0) - self.R_gas * np.log((estado.v - self.b) / (self.v0 - self.b))
					return s_calc - estado.s

				sol = root_scalar(f, bracket=[self.T0*0.1, self.T0*10], method='brentq')
				if not sol.converged:
					raise ValueError("No se pudo encontrar temperatura para s y v dados.")
				estado.T = sol.root
				estado.P = calcular_P(estado.T, estado.v)
				estado.u = self.cv * (estado.T - self.T0) - self.a / estado.v
				estado.h = estado.u + estado.P * estado.v

			# Caso 6: (s, P)
			elif (estado.s is not None) and (estado.P is not None):
				from scipy.optimize import root_scalar

				def f(T):
					v = calcular_v(estado.P, T)
					s_calc = self.cp * np.log(T / self.T0) - self.R * np.log((v - self.b) / (self.v0 - self.b))
					return s_calc - estado.s

				sol = root_scalar(f, bracket=[self.T0*0.1, self.T0*10], method='brentq')
				if not sol.converged:
					raise ValueError("No se pudo encontrar temperatura para s y P dados.")
				estado.T = sol.root
				estado.v = calcular_v(estado.P, estado.T)
				estado.u = self.cv * (estado.T - self.T0) - self.a / estado.v
				estado.h = estado.u + estado.P * estado.v

			# Caso 7: (T, s)
			elif (estado.T is not None) and (estado.s is not None):
				from scipy.optimize import root_scalar

				def f(P):
					v = calcular_v(P, estado.T)
					s_calc = self.cp * np.log(estado.T / self.T0) - self.R_gas * np.log((v - self.b) / (self.v0 - self.b))
					return s_calc - estado.s

				# Buscamos P en un rango razonable
				sol = root_scalar(f, bracket=[1e3, 1e8], method='brentq')
				if not sol.converged:
					raise ValueError("No se pudo encontrar presión para T y s dados.")
				estado.P = sol.root
				estado.v = calcular_v(estado.P, estado.T)
				estado.u = self.cv * (estado.T - self.T0) - self.a / estado.v
				estado.h = estado.u + estado.P * estado.v

			else:
				raise ValueError("Combinación de propiedades no soportada o insuficiente.")


		elif self.calores_constantes == False:
			print("No se ha implementado")

	def _presion(self, T, v):
		"""Devuelve la presión (Pa) usando la ecuación de Van der Waals."""
		return (self.R_gas * T) / (v - self.b) - self.a / v**2

	def _temperatura(self, P, v):
		"""Devuelve la temperatura (K) a partir de presión y volumen."""
		return ((P + self.a / v**2) * (v - self.b)) / self.R_gas

	
	def _resolver_temperatura_desde_sv(self, s, v):
		"""Calcula T desde entropía y volumen."""
		T_guess = self.T0
		def f(T):
			s_calc = self.R_gas * np.log((T / self.T0) * ((v - self.b) / self.v0))
			return s_calc - s
		T_solution, = fsolve(f, T_guess)
		return T_solution

	def _calcular_propiedades(self, estado):
		"""
		Calcula u, h, s a partir de P, T y v. Se asume gas monoatómico (Cv = 3/2 R).
		"""
		Cv = 1.5 * self.R_gas
		Cp = Cv + self.R_gas

		estado.u = Cv * estado.T - self.a / estado.v
		estado.h = estado.u + estado.P * estado.v
		estado.s = self.R_gas * np.log((estado.T / self.T0) * ((estado.v - self.b) / self.v0))
