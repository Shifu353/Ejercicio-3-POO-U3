import numpy as np
from TallerCapacitacion import TallerCapacitacion
from Incripcion import Incripcion
from ManejadorIncripcion import ArregloIncripcion
class Arreglo ():
    def __init__ (self,dimencion=1,incremento=4):
        self.__array = np.empty(dimencion,dtype=TallerCapacitacion)
        self.__cantidad = 0
        self.__dimencion = dimencion
        self.__incremento = incremento

    def AgregarTaller (self,taller):
        if self.__cantidad == self.__dimencion:
            self.__dimencion += self.__incremento
            self.__array.resize(self.__dimencion)
        self.__array[self.__cantidad]=taller
        self.__cantidad += 1
    
    def BuscarTallerxID (self,idtaller):
        i = 0
        while i<len(self.__array) and int(self.__array[i].getIdTaller()) != idtaller:
            i += 1
        if i<len(self.__array):
            return i
        return -1
    
    def InscripcionaTaller (self,fecha,persona,taller):
        if int(self.__array[taller].getIdTaller()) > 0:
            inscripcion = Incripcion(fecha,persona,self.__array[taller])
            self.__array[taller].addInscripcion(inscripcion)
            return inscripcion
        else:
            print("No se puede inscribir en este taller porque no hay vacantes")
    
    def ConsultarInscriptos (self, idTaller):
        buscar = self.BuscarTallerxID(idTaller)
        if buscar != -1:
            inscriptos_a_este_taller = self.__array[buscar].getLista()
            for incripto in inscriptos_a_este_taller:
                persona = incripto.getPersona()
                print(persona)
        else:
            print("El id del taller es incorrecto")

    def Mostrar(self):
        print("{}       {}       {}       {}".format("NumTaller","Nombre del taller","Vacantes","Monto"))
        for taller in self.__array:
            print(taller)
