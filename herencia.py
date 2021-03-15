class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)

#####################HERENCIA MULTIPLE##################################
class Terrestre:

    def desplazar(self):
        print('El animal anda')


class Acuatico:

    def desplazar(self):
        print('El animal nada')

#Herencia Multiple
class Cocodrilo(Terrestre, Acuatico):
    """Abstracción de cocodrilo. Herencia multiple.
    
    Como Terrestre se encuentra más a la izquierda,
    sería la definición de desplazar de esta clase la
    que prevalecería.
    """
    pass

if __name__ == '__main__':
    rectangulo = Rectangulo(base = 3, altura = 4)
    print(rectangulo.area())

    cuadrado = Cuadrado(5)
    print(cuadrado.area())