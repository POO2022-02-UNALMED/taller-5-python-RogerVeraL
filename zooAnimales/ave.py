from animal import Animal
class Ave(Animal):
    #atributos
    _listado=list()
    aves,halcones,aguilas=0,0,0
    
    #constructor
    def __init__(self,nombre,edad,habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        Ave.aves+=1
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)
    
    #getter & setter
    def getListado(self):
        return Ave._listado
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self,colorPlumas):
        self._colorPlumas=colorPlumas
    
    #metodos
    def cantidadAves(self):
        return Ave.aves
    def movimiento(self):
        return "volar"
    def crearHalcon(self,nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero,"cafe glorioso")
    def crearLeon(self,nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")   