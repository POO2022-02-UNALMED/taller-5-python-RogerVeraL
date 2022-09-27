class Animal():
    #atributo
    _totalAnimales=0
    
    #constructor
    def __init__(self,nombre,edad,habitat,genero):
        Animal._totalAnimales += 1
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=None
        
    #getter & setter
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre=nombre

    def getEdad(self):
        return self._edad
    def setEdad(self,edad):
        self._edad=edad

    def getHabitat(self):
        return self._habitat
    def setHabitat(self,habitat):
        self._habitat=habitat

    def getGenero(self):
        return self._genero
    def setGenero(self,genero):
        self._genero=genero

    def getZona(self):
        return self._zona
    def setZona(self,zona):
        self._zona=zona
    
    #Metodos
    def movimiento(self):
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        from mamifero import Mamifero as m
        from ave import Ave as a
        from reptil import Reptil as r
        from pez import Pez as p
        from anfibio import Anfibio as an
        print("Mamiferos :",m.cantidadMamiferos(),
        "\nAves :",a.cantidadAves(),
        "\nReptiles :",r.cantidadReptiles(),
        "\nPeces :",p.cantidadPeces(),
        "\nAnfibios :",an.cantidadAnfibios()
        )
    
    def toString(self):
        if self._zona == None:
            return f"Mi nombre es {self.getNombre()} tengo una edad de {self.getEdad()} habito en {self.getHabitat()} y mi genero es {self.getGenero()}"         
        else:
            return f"Mi nombre es {self.getNombre()} tengo una edad de {self.getEdad()} habito en {self.getHabitat()} y mi genero es {self.getGenero()} la zona en la que me ubico es {self.getZona.getNombre()} en el {self.getZona.getZoo().getNombre()}"
            
        




    