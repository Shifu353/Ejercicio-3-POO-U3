class ManejadorPersona ():
    def __init__ (self):
        self.__listaPersona = []
    
    def AgregarPersona (self,persona):
        self.__listaPersona.append(persona)

    def BuscarxDni (self,dni):
        i = 0
        while i<len(self.__listaPersona) and int(self.__listaPersona[i].getDni()) != dni:
            i += 1
        if i<len(self.__listaPersona):
            return self.__listaPersona[i]
        return -1
