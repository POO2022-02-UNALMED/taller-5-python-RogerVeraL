from zooAnimales.animal import Animal
#from animal import Animal
class Pez(Animal):
    #atributos
    _listado=list()
    peces,salmones,bacalaos=0,0,0
    
    #constructor
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
        super().__init__(nombre,edad,habitat,genero)
        Pez.peces+=1
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez._listado.append(self)

    #getter & setter
    def getListado(self):
        return Pez._listado

    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas=colorEscamas
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self,cantidadAletas):
        self._cantidadAletas=cantidadAletas
    

    #metodos
    def cantidadPeces():
        return Pez.peces
    def movimiento(self):
        return "nadar"
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 4)   