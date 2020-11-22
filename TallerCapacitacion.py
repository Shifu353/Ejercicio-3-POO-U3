class TallerCapacitacion (object):
    def __init__ (self, idT, nombre, vacante, monto):
        self.__idTaller = idT
        self.__nombre = nombre
        self.__vacante = vacante
        self.__monto = monto
        self.__listaIncriptos = []

    def addInscripcion (self,insc):
        self.__listaIncriptos.append(insc)
        self.__vacante -= 1
    
    def getLista (self):
        return self.__listaIncriptos
        
    def getIdTaller (self):
        return self.__idTaller

    def getVacante (self):
        return self.__vacante

    def getNombre (self):
        return self.__nombre
    
    def getMonto (self):
        return self.__monto

    def __str__ (self):
        return "   {}               {}             {}          {}".format(str(self.__idTaller),self.__nombre,str(self.__vacante),str(self.__monto))
    
    def setVacante (self):
        self.__vacante = self.__vacante - 1
        
