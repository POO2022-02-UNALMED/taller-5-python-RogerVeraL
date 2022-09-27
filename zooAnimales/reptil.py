from zooAnimales.animal import Animal
#from animal import Animal
class Reptil(Animal):
    #atributos
    _listado=list()
    reptiles,iguanas,serpientes=0,0,0
    
    #constructor
    def __init__(self,nombre,edad,habitat, genero, colorEscamas,largoCola):
        super().__init__(nombre, edad, habitat, genero)
        Reptil.reptiles+=1
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._listado.append(self)
    
    #getter & setter
    def getListado(self):
        return Reptil._listado

    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas=colorEscamas

    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self,largoCola):
        self._largoCola=largoCola
    
    #metodos
    def cantidadReptiles():
        return Reptil.reptiles
    def movimiento(self):
        return "reptar"
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 4)   