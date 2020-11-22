from Incripcion import Incripcion
import numpy as np 

class ArregloIncripcion ():
    def __init__ (self, dimencion=4,incremento=4):
        self.__array = np.empty(dimencion, dtype=Incripcion)
        self.__cantidad = 0
        self.__dimencion = dimencion
        self.__incremento = incremento

    def Agregar_Al_Arreglo (self,inscripcion):
        if self.__cantidad == self.__dimencion:
            self.__dimencion += self.__incremento
            self.__array.resize(self.__dimencion)
        self.__array[self.__cantidad] = inscripcion
        self.__cantidad += 1

    def Mostrar (self):
        print(len(self.__array))
        for inscripcion in self.__array:
            print(inscripcion.getPersona())
    
    def BuscarDni (self,dni):
        i = 0
        while i<len(self.__array) and int(self.__array[i].getPersona().getDni()) != dni:
            i += 1
        if i<len(self.__array):
            return i
        return -1

    def RegistrarPago (self,dni):
        posision = self.BuscarDni(dni)
        if posision != -1:
            self.__array[posision].setPago()
        

    def MostrarConsulta (self,dni):
        buscar = self.BuscarDni(dni)
        if buscar != -1:
            print("Se inscribio en el taller {} y adeuda ${}".format(self.__array[buscar].getTaller().getNombre(),self.__array[buscar].getTaller().getMonto()))
        else:
            print("El dni ingresado no es correcto")
    
    def GuardarArchivo (self):
        import csv
        data = {}
        lista = []
        for inscripto in self.__array:
            if inscripto != None:
                taller=inscripto.getTaller()
                persona=inscripto.getPersona()
                fecha=inscripto.getFecha()
                pago=inscripto.getPago()
                data={"dni":persona.getDni(),"IdTaller":taller.getIdTaller(),
                "FechaInscripcion":fecha,"Pago":pago}
                lista.append(data)
        print(lista)
        #archivo=open("inscripciones.csv","w")
        with open("inscripciones.csv","w") as archivo:
            nombres = ["dni","IdTaller","FechaInscripcion","Pago"]
            escribir = csv.DictWriter(archivo,fieldnames=nombres)
            escribir.writeheader()
            for datas in lista:
                escribir.writerow(datas)
    
    def MostrarLen (self):
        print(len(self.__array))
        print(self.__array)
