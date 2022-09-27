from zooAnimales.animal import Animal
#from animal import Animal
class Anfibio(Animal):
    #atributos
    _listado=list()
    anfibios,ranas,salamandras=0,0,0
    
    #constructor
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        Anfibio.anfibios+=1
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)
    
    
    #getter & setter
    def getListado(self):
        return Anfibio._listado
    
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self,colorPiel):
        self._colorPiel=colorPiel
    
    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self,venenoso):
        self._venenoso=venenoso
    

    #metodos
    def CantidadAnfibios():
        return Anfibio.anfibios
    def movimiento(self):
        return "saltar"
    def crearRana(nombre, edad, genero):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)   
