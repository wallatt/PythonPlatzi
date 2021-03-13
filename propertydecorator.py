#EJEMPLO 1

class House:

	def __init__(self, price):
		self._price = price

	@property
	def price(self):
		print('Using getter')
		return self._price
        
	
	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			print('Using setter')

			self._price = new_price
		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self._price

house1 = House(30)
print(house1.price)
house1.price = 35.0

#EJEMPLO 2

class Millas:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	def definir_distancia(self, recorrido):
		print("Llamada al método setter")
		self._distancia = recorrido

	# Función para eliminar el atributo _distancia
	def eliminar_distancia(self):
		del self._distancia

	distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

# Creamos un nuevo objeto 
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos su atributo distancia
print(avion.distancia)
