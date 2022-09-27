class Zoologico():
    #constructor
    def __init__(self,nombre,ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=list()
    
    #getter & setter
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre=nombre

    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion

    def getZona(self):
        return self._zonas

    #metodos
    def agregarzonas(self,zona):
        self._zonas.append(zona)
    def cantidadTotalAnimales(self):
        return sum([a.cantidadAnimales() for a  in self._zonas])
