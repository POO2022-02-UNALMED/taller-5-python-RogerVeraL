from zooAnimales.animal import Animal
#from animal import Animal
class Mamifero(Animal):
    #atributos
    _listado=list()
    mamiferos,caballos,leones=0,0,0
    #constructor
    def __init__(self,nombre,edad,habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        Mamifero.mamiferos += 1
        self._pelaje =pelaje
        self._patas =patas
        Mamifero._listado.append(self)
    
    #getter & setter
    def getListado(self):
        return Mamifero._listado

    def isPelaje(self):
        return self._pelaje    
    def setPelaje(self,pelaje):
        self._pelaje =pelaje
        
    def getPatas(self):
        return self._patas   
    def setPatas(self,patas):
        self._patas =patas
    
    #metodos
    def cantidadMamiferos():
        return Mamifero.mamiferos
    def crearCaballo(self,nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)
    def crearLeon(self,nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)   