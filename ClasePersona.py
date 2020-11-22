class Persona (object):
    def __init__ (self, nombre, direccion, dni):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni
    
    def getDni (self):
        return self.__dni
    
    def __str__ (self):
        return "Nombre: {} \n Direccion: {} \n Dni: {}".format(self.__nombre,self.__direccion,str(self.__dni))
