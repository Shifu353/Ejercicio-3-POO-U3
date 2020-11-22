from TallerCapacitacion import TallerCapacitacion
from ClasePersona import Persona
class Incripcion (object):
    def __init__ (self, fecha,persona, taller,pago=False):
        self.__fechaincripcion = fecha
        self.__pago = pago
        self.__persona = persona
        self.__Taller = taller
    
    def getPersona (self):
        return self.__persona
    
    def getTaller (self):
        return self.__Taller
    
    def setPago (self):
        self.__pago = True
    
    def getPago (self):
        return self.__pago

    def getFecha (self):
        return self.__fechaincripcion
