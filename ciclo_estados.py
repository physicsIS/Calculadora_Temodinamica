import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Definición de la clase estado
class Estado:
	"""
	Representa un estado termodinámico de un sistema.

	Attributes:
		nombre (str): Nombre identificador del estado.
		modelo (ModeloTermodinamico): Modelo termodinámico asociado.
		P (float): Presión en Pa.
		T (float): Temperatura en Kelvin.
		v (float): Volumen específico en m³/kg.
		u (float): Energía interna específica en J/kg.
		h (float): Entalpía específica en J/kg.
		s (float): Entropía específica en J/kg·K.
		x (float): Calidad del fluido, cantidad del fluido que se encuentra en vapor, constante en cada estado.
	"""


	def __init__(self, modelo, nombre=0):
		"""
		Inicializa el estado con un modelo y un nombre.

		Args:
			modelo (ModeloTermodinamico): Modelo para calcular propiedades.
			nombre (str, optional): Nombre del estado. Por defecto "". Corresponde al numero (int) del estado, mas que un nombre es un identificador.
		"""
		self.nombre = nombre
		self.modelo = modelo

		# Propiedades termodinámicas
		self.P = None # Presion Pa
		self.T = None # Temperatura k
		self.v = None # Volumen especifico
		self.u = None # Energia interna especifica
		self.h = None # Entalpia especifica
		self.s = None # Entropia especifica
		self.x = 1 # Calidad, por defecto es un gas

	def actualizar(self, **kwargs):
		"""
		Asigna las propiedades conocidas de un estado a su respectivo objeto.

		Args:
			**kwargs: Propiedades conocidas (por ejemplo, P, T, s, h...).
		"""

		# A continuacion se presentan los casos que va a revisar el programa si se tiene los datos y calcula los datos faltantes si es posible

		atributos_validos = ['P', 'T', 'v', 'u', 'h', 's','x']
		for key, value in kwargs.items():
			if key not in atributos_validos:
				raise AttributeError(f"'{key}' no es una propiedad válida del estado.")
			
			# Validación especial para calidad (x) en gases ideales
			if key == 'x':
				if self.modelo.__class__.__name__ == "ModeloGasIdeal" and value != 1:
					raise AttributeError("Gas ideal no puede tener calidad diferente de 1")
			setattr(self, key, value)
	def calcular_propiedades(self):
		'''
		Calcula las propiedades termodinamicas de los estados del ciclo.
		'''
		self.modelo.calcular_estado(self)

	def resumen(self):
		"""
		Devuelve un resumen legible del self actual.

		Returns:
			str: Descripción con las propiedades termodinámicas.
		"""
		def format_prop(prop, unidad=""):
			return f"{prop:.2f} {unidad}" if prop is not None else "N/A"

		return (f"{self.nombre}: P={format_prop(self.P, 'Pa')}, T={format_prop(self.T, 'K')}, "
				f"v={format_prop(self.v, 'm³/kg')}, u={format_prop(self.u, 'J/kg')}, "
				f"h={format_prop(self.h, 'J/kg')}, s={format_prop(self.s, 'J/kg·K')}")

	def _get_states(self):
		"""
		Devuelve un diccionario con el nombre como llave y un diccionario con los valores de las variables en ese estado

		Returns:
			dict: diccionario con int de llave y diccionario de valor
		"""
		return {self.nombre : {"P" : self.P, "T" : self.T, "v" : self.v, "u" : self.u, "h" : self.h, "s" : self.s}}

# Definición de la clase CicloTermodinamico
class CicloTermodinamico:
	"""
	Representa un ciclo compuesto por una serie de estados termodinámicos.

	Atributes:
		modelo (ModeloTermodinamico): Modelo termodinámico utilizado.
		n_estados (int): Número de estados que conforman el ciclo.
		n_values (int): Número de estados internos a cada proceso del ciclo, debe ser un número mayor o igual a 0. Default n_values = 35.
		estados (list[Estado]): Lista de estados que componen el ciclo.
		direccion (str): Dirección en la que se recorre el ciclo. Use "horario" o "antihorario".
	"""

	def __init__(self, modelo,n_estados, n_values = 35):
		self.modelo = modelo
		self.n_values = n_values +2
		self.estados = np.empty(n_estados, dtype=object) # Se conocen la cantidad de estados que tiene el ciclo
		self.estados_internos = np.empty((n_estados,n_values), dtype=object) # Se genera una lista para los estados internos entre cada proceso.
		self._indice_estado_actual = 0  # Contador de estado
		self._indice_proceso_actual = 0 # Contador de proceso

	def agregar_estado(self, nombre, **kwargs):
		"""
		Crea y agrega un nuevo estado al ciclo. Se espera que se coloquen en el orden que se va a recorrer el ciclo.

		Args:
			nombre (str): Nombre identificador del estado.
			**kwargs: Propiedades conocidas para calcular el estado.
		"""

		if self._indice_estado_actual >= len(self.estados):
			raise IndexError("Se han agregado más estados de los permitidos.")

		estado = Estado(self.modelo, nombre)
		estado.actualizar(**kwargs)
		self.estados[self._indice_estado_actual] = estado
		self._indice_estado_actual +=1

	def _generar_estado_interno(self, **kwargs):
		"""
		Genera un nuevo estado interno a un proceso del ciclo.

		Args:
			**kwargs: Propiedades conocidas para calcular el estado.
		"""
		estado_interno = Estado(self.modelo)
		estado_interno.actualizar(**kwargs)
		estado_interno.calcular_propiedades()
		return estado_interno

	def proceso_isocorico(self, estado_in, estado_out):
		'''
		Relaciona dos estados de un ciclo termodinámico mediante un proceso isocórico o a volumen constante.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
		'''

		result = self.modelo.resolver_isocorico(estado_in,estado_out)
		P_values = np.linspace(estado_in.P,estado_out.P, self.n_values)[1:-1]
		T_values = result(P_values)
		for i in range(self.n_values-2):
			self.estados_internos[estado_in.nombre-1][i] = self._generar_estado_interno(P = P_values[i], T=T_values[i])


		self._indice_proceso_actual += 1

	def proceso_isotermico(self, estado_in, estado_out):
		'''
		Relaciona dos estados de un ciclo termodinámico mediante un proceso isotérmico o a temperatura constante.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
		'''

		result = self.modelo.resolver_isotermico(estado_in,estado_out)
		v_values = np.linspace(estado_in.v,estado_out.v, self.n_values)[1:-1]

		P_values = result(v_values)
		for i in range(self.n_values-2):
			self.estados_internos[estado_in.nombre-1][i] = self._generar_estado_interno(v = v_values[i], P=P_values[i])

		self._indice_proceso_actual += 1

	def proceso_isobarico(self, estado_in, estado_out):
		'''
		Relaciona dos estados de un ciclo termodinámico mediante un proceso isobárico o a presión constante.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
		'''

		result = self.modelo.resolver_isobarico(estado_in,estado_out)
		v_values = np.linspace(estado_in.v,estado_out.v, self.n_values)[1:-1]
		T_values = result(v_values)
		for i in range(self.n_values-2):
			self.estados_internos[estado_in.nombre-1][i] = self._generar_estado_interno(v = v_values[i], T=T_values[i])

		self._indice_proceso_actual += 1

	def proceso_isoentalipico(self, estado_in, estado_out):
		'''
		Relaciona dos estados de un ciclo termodinámico mediante un proceso isoentálpico o a entalpía constante.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
		'''

		result = self.modelo.resolver_isoentalpico(estado_in,estado_out)
		v_values = np.linspace(estado_in.v,estado_out.v, self.n_values)[1:-1]
		P_values = result(v_values)
		for i in range(self.n_values-2):
			self.estados_internos[estado_in.nombre-1][i] = self._generar_estado_interno(v = v_values[i], P=P_values[i])

		self._indice_proceso_actual += 1

	def proceso_isoentropico(self, estado_in, estado_out):
		'''
		Relaciona dos estados de un ciclo termodinámico mediante un proceso isoentrópico o a entropía constante.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
		'''

		result = self.modelo.resolver_isoentropico(estado_in,estado_out)
		v_values = np.linspace(estado_in.v,estado_out.v, self.n_values)[1:-1]
		P_values = result(v_values)
		for i in range(self.n_values-2):
			self.estados_internos[estado_in.nombre-1][i] = self._generar_estado_interno(v=v_values[i], P = P_values[i])

		self._indice_proceso_actual += 1

	def proceso_in_or_out_calor(self,estado_in, estado_out, calor):
		'''
		Relaciona dos estados de un ciclo termodinámico mediante un proceso de adicion o rechazo de calor a temperatura constante.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
			calor (float): Calor de entrada (positivo) o salida (negativo) del proceso.
		'''
		result = self.modelo.resolver_in_or_out_calor(estado_in, estado_out, calor)
		v_values = np.linspace(estado_in.v,estado_out.v, self.n_values)[1:-1]
		P_values = result(v_values)
		for i in range(self.n_values-2):
			self.estados_internos[estado_in.nombre-1][i] = self._generar_estado_interno(v=v_values[i], P = P_values[i])

		self._indice_proceso_actual += 1

	"""def proceso_interenfriamiento_recalentamiento(self,estado_in, estado_out, delta_T):
		'''
		Relaciona dos estados de un ciclo termodinámico mediante un proceso de adicion o rechazo de calor con un cambio de temperatura determinado.

		Args:
			estado_in (Estado): Estado de entrada en la secuencia del ciclo.
			estado_out (Estado): Estado de salida en la secuencia del ciclo.
			calor (float): Calor de entrada (positivo) o salida (negativo) del proceso.
		'''
		result = self.modelo.resolver_interenfriamiento_recalentamiento(estado_in, estado_out, delta_T)
		v_values = np.linspace(estado_in.v,estado_out.v, self.n_values)
		T_values = result(v_values)
		for i in range(self.n_values):
			self.estados_internos[estado_in.nombre-1][i] = self._generar_estado_interno(v=v_values[i], T = T_values[i])

		self._indice_proceso_actual += 1 """


	def mostrar_ciclo(self):
		"""
		Muestra por pantalla un resumen de todos los estados en el ciclo.
		"""
		for estado in self.estados:
			print(estado.resumen())

	def generar_dataframes(self, opcion=1):
			"""
			Genera DataFrames con los estados del ciclo termodinámico.

			Parameters
			----------
			opcion : int
				- 1: Retorna un DataFrame con los estados principales del ciclo.
				- 2: Retorna una lista con dos DataFrames:
					1. Estados principales
					2. Todos los estados (principales e internos)

			Returns
			-------
			pandas.DataFrame o list[pandas.DataFrame]
			"""
			# Crear DataFrame de estados principales
			df_principal = pd.DataFrame(
				[{
					"nombre": estado.nombre,
					"P [Pa]": estado.P,
					"T [K]": estado.T,
					"v [m³/kg]": estado.v,
					"u [J/kg]": estado.u,
					"h [J/kg]": estado.h,
					"s [J/kg·K]": estado.s
				} for estado in self.estados if estado is not None]
			)

			if opcion == 1:
				return df_principal

			elif opcion == 2:
				lista_estados = []
				for i, estado in enumerate(self.estados):
					if estado is None:
						continue

					# Estado principal
					lista_estados.append({
						"nombre": str(estado.nombre),
						"P [Pa]": estado.P,
						"T [K]": estado.T,
						"v [m³/kg]": estado.v,
						"u [J/kg]": estado.u,
						"h [J/kg]": estado.h,
						"s [J/kg·K]": estado.s
					})

					# Estados internos del tramo correspondiente
					if i < len(self.estados_internos):
						contador_interno = 1
						for estado_int in self.estados_internos[i]:
							if estado_int is not None:
								lista_estados.append({
									"nombre": f"{estado.nombre}.{contador_interno}",
									"P [Pa]": estado_int.P,
									"T [K]": estado_int.T,
									"v [m³/kg]": estado_int.v,
									"u [J/kg]": estado_int.u,
									"h [J/kg]": estado_int.h,
									"s [J/kg·K]": estado_int.s
								})
								contador_interno += 1

				df_completo = pd.DataFrame(lista_estados)
				return [df_principal, df_completo]

			else:
				raise ValueError("Opción inválida. Debe ser 1 o 2.")

	def graficar_diagrama_Pv(self, nombre_ciclo="Ciclo termodinámico", ax=None):
		"""
		Grafica el diagrama P-v del ciclo termodinámico.
		Cada tramo tiene su propio color y etiqueta.
		"""
		import matplotlib.pyplot as plt
		import pandas as pd

		# Obtener DataFrames
		df_principal, df_completo = self.generar_dataframes(opcion=2)

		# Crear columnas auxiliares para ordenar
		df_completo["tramo"] = df_completo["nombre"].apply(lambda x: str(x).split(".")[0])
		df_completo["subindice"] = df_completo["nombre"].apply(
			lambda x: 0 if "." not in str(x) else int(str(x).split(".")[1])
		)
		df_completo.sort_values(by=["tramo", "subindice"], inplace=True)

		colores = plt.cm.tab10.colors
		if ax is None:
			fig, ax = plt.subplots(figsize=(6, 4))
		else:
			fig = ax.figure

		tramos_unicos = df_principal["nombre"].astype(str).tolist()
		n_tramos = len(tramos_unicos)

		# Graficar cada tramo
		for i, tramo in enumerate(tramos_unicos):
			estado_ini = df_principal.iloc[i]
			estado_fin = df_principal.iloc[(i + 1) % n_tramos]

			grupo = df_completo[df_completo["tramo"] == tramo]

			# Secuencia: estado inicial -> internos -> estado final
			v_vals = [estado_ini["v [m³/kg]"]] + grupo["v [m³/kg]"].tolist() + [estado_fin["v [m³/kg]"]]
			P_vals = [estado_ini["P [Pa]"]] + grupo["P [Pa]"].tolist() + [estado_fin["P [Pa]"]]

			ax.plot(v_vals, P_vals, color=colores[i % len(colores)],
					label=f"Tramo {tramo} → {estado_fin['nombre']}")
			ax.scatter(v_vals, P_vals, color=colores[i % len(colores)], s=20)

		# Estados principales
		ax.scatter(df_principal["v [m³/kg]"], df_principal["P [Pa]"],
				color='black', s=60, edgecolor='white', zorder=5, label="Estados principales")

		for _, estado in df_principal.iterrows():
			ax.annotate(estado["nombre"],
						xy=(estado["v [m³/kg]"] * 1.01, estado["P [Pa]"] * 1.01))

		ax.set_xlabel(r'Volumen específico [$m^3$/kg]')
		ax.set_ylabel('Presión [Pa]')
		ax.set_title(f'Diagrama P-v: {nombre_ciclo}')
		ax.grid(True)
		ax.legend()
		fig.tight_layout()

		return fig, ax

	def graficar_diagrama_Ts(self, nombre_ciclo="Ciclo termodinámico", ax=None):
		"""
		Grafica el diagrama T-s del ciclo termodinámico.
		Cada tramo tiene su propio color y etiqueta.
		"""
		import matplotlib.pyplot as plt
		import pandas as pd

		# Obtener DataFrames
		df_principal, df_completo = self.generar_dataframes(opcion=2)

		# Crear columnas auxiliares para ordenar
		df_completo["tramo"] = df_completo["nombre"].apply(lambda x: str(x).split(".")[0])
		df_completo["subindice"] = df_completo["nombre"].apply(
			lambda x: 0 if "." not in str(x) else int(str(x).split(".")[1])
		)
		df_completo.sort_values(by=["tramo", "subindice"], inplace=True)

		colores = plt.cm.tab10.colors
		if ax is None:
			fig, ax = plt.subplots(figsize=(6, 4))
		else:
			fig = ax.figure

		tramos_unicos = df_principal["nombre"].astype(str).tolist()
		n_tramos = len(tramos_unicos)

		# Graficar cada tramo
		for i, tramo in enumerate(tramos_unicos):
			estado_ini = df_principal.iloc[i]
			estado_fin = df_principal.iloc[(i + 1) % n_tramos]

			grupo = df_completo[df_completo["tramo"] == tramo]

			# Secuencia: estado inicial -> internos -> estado final
			s_vals = [estado_ini["s [J/kg·K]"]] + grupo["s [J/kg·K]"].tolist() + [estado_fin["s [J/kg·K]"]]
			T_vals = [estado_ini["T [K]"]] + grupo["T [K]"].tolist() + [estado_fin["T [K]"]]

			ax.plot(s_vals, T_vals, color=colores[i % len(colores)],
					label=f"Tramo {tramo} → {estado_fin['nombre']}")
			ax.scatter(s_vals, T_vals, color=colores[i % len(colores)], s=20)

		# Estados principales
		ax.scatter(df_principal["s [J/kg·K]"], df_principal["T [K]"],
				color='black', s=60, edgecolor='white', zorder=5, label="Estados principales")

		for _, estado in df_principal.iterrows():
			ax.annotate(estado["nombre"],
						xy=(estado["s [J/kg·K]"] * 1.01, estado["T [K]"] * 1.01))

		ax.set_xlabel('Entropía específica [J/kg·K]')
		ax.set_ylabel('Temperatura [K]')
		ax.set_title(f'Diagrama T-s: {nombre_ciclo}')
		ax.grid(True)
		ax.legend()
		fig.tight_layout()

		return fig, ax

	def calcular_eficiencia_num(self):
		"""
		Calcula la eficiencia térmica del ciclo termodinámico por medio de integral trapezoidal
		
		Returns:
		float: Eficiencia térmica del ciclo (0 a 1).
		"""
		n = len(self.estados)
		works = []  # Trabajo en cada proceso
		heats = []  # Calor en cada proceso
		
		for i in range(n):
			# Estados inicial y final del proceso
			estado_in = self.estados[i]
			estado_out = self.estados[(i + 1) % n]
        
			# Calcular ΔU entre estados
			delta_U = estado_out.u - estado_in.u
        
			 # Obtener estados internos del proceso (sin valores nulos)
			internals = [e for e in self.estados_internos[i] if e is not None]
			all_states = [estado_in] + internals + [estado_out]
        
			# Calcular trabajo  usando integral trapezoidal
			W = 0
			for j in range(len(all_states) - 1):
				P_avg = (all_states[j].P + all_states[j + 1].P) / 2
				delta_V = all_states[j + 1].v - all_states[j].v
				W += P_avg * delta_V
        
			# Calcular calor usando Primera Ley (Q = ΔU + W)
			Q = delta_U + W
        
			works.append(W)
			heats.append(Q)

		# Calcular trabajo neto (suma de trabajos positivos - suma de trabajos negativos)
		net_work = sum(W for W in works)
		
		# Calcular calor total de entrada (solo valores positivos)
		heat_input = sum(Q for Q in heats if Q > 0)
		
		# Calcular eficiencia (evitar división por cero)
		if heat_input > 0:
			efficiency = net_work / heat_input
		else:
			efficiency = 0
		print(f"La eficiencia del ciclo por método numérico es: {efficiency:.3f}")
		return efficiency	
        
	def calcular_eficiencia(self,modelo, carnot = False):
		"""
		Calcula la eficiencia térmica del ciclo termodinámico.
		
		Returns:
		float: Eficiencia térmica del ciclo (0 a 1).
		"""
		n = len(self.estados)
		works = []  # Trabajo en cada proceso
		heats = []  # Calor en cada proceso

		if carnot:
			T_values = [state.T for state in self.estados]
			T_values.sort()
			T_High = T_values[n-1]
			T_low = T_values[0]
			efficiency = 1 - T_low/T_High
			print(f"La eficiencia del ciclo de Carnot: {efficiency:.3f}")
			return efficiency
		for i in range(n):
			# Estados inicial y final del proceso
			estado_in = self.estados[i]
			estado_out = self.estados[(i + 1) % n]
        
			# Calcular ΔU entre estados
			delta_U = estado_out.u - estado_in.u
        
			 # Obtener estados internos del proceso (sin valores nulos)
			internals = [e for e in self.estados_internos[i] if e is not None]
			all_states = [estado_in] + internals + [estado_out]
            
			# Calcular trabajo  dependiendo del tipo de modelo
			W = 0
			if modelo.__class__.__name__ == "ModeloGasIdeal":
				if np.allclose(estado_in.P,estado_out.P):
					''' 
                        Proceso Isobárico
                        W = P*(Vf - Vi)
					'''
					W = estado_in.P*(estado_out.v - estado_in.v)
					Q = estado_out.h - estado_in.h
				elif np.allclose(estado_in.T,estado_out.T):
					''' 
                        Proceso Isotérmico
                        W = R*T*ln(Vf/Vi)
					'''
					W = modelo.R_gas*estado_in.T*np.log(estado_out.v/estado_in.v)
					Q = W
				elif np.allclose(estado_in.s, estado_out.s):
					'''
                        Proceso Isoentrópico
                        W = -deltaU
					'''
					W = -delta_U
					Q = 0
				elif np.allclose(estado_in.h, estado_out.h):
					'''
                        Proceso Isoentálpico
                        W = cp*(Tf - Ti)
					'''
					W = 0 #modelo.cp*(estado_out.T - estado_in.T)
					Q = delta_U
				else:
					Q = delta_U + W
                
			elif modelo.__class__.__name__=="ModeloVanDerWaals":
				pass  
        
        
			works.append(W)
			heats.append(Q)

		# Calcular trabajo neto (suma de trabajos positivos - suma de trabajos negativos)
		net_work = sum(W for W in works)
		print(works)
		print(heats)
		# Calcular calor total de entrada (solo valores positivos)
		heat_input = sum(Q for Q in heats if Q > 0)
		# Calcular eficiencia (evitar división por cero)
		if heat_input > 0:
			efficiency = net_work / heat_input
		else:
			efficiency = 0
		print(f"La eficiencia del ciclo: {efficiency:.3f}")
		return efficiency