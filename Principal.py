if __name__ == "__main__":
    from ClasePersona import Persona
    from Incripcion import Incripcion
    from ManejadorIncripcion import ArregloIncripcion
    from ManejadorPersona import ManejadorPersona
    from ManejadorTalleres import Arreglo
    from TallerCapacitacion import TallerCapacitacion
    import csv,os
    archivo = open("Talleres.csv")
    leer = csv.DictReader(archivo, delimiter=";")
    bandera = 0
    for taller in leer:
        if len(taller) != 0:
            if bandera == 0:
                bandera = 1
                ManejaTalleres = Arreglo(int(taller["id"]))
                #ManejaTalleres.Dimencion(int(taller["id"]))
            if taller["id"] != None and taller["vacantes"] != None and taller["montos"] != None:
                talleres = TallerCapacitacion(int(taller["id"]),taller["nombre"],int(taller["vacantes"]),int(taller["montos"]))
                ManejaTalleres.AgregarTaller(talleres)
        else:
            print("Se produjo un error en el archivo CSV")
    archivo.close()
    #print(ManejaTalleres.LenArreglo())
    #ManejaTalleres.Mostrar()
    def op1():
        os.system("cls")
        try:
            print("//Inscribir una persona en un taller//")
            print("Ingrese datos de la persona")
            nombre = input("Nombre: ")
            direccion = input("Direccion: ")
            dni = int(input("Dni: "))
            persona = Persona(nombre,direccion,dni)
            dia = int(input("Ingrese dia de inscripcion: "))
            mes = int(input("Ingrese mes de inscripcion: "))
            anno = int(input("Ingrese año de inscripcion: "))
            fecha_de_incripcion = str(dia)+"/"+str(mes)+"/"+str(anno)
            print("Seleccione un taller")
            ManejaTalleres.Mostrar()
            taller = int(input("Ingrese numero del Taller: "))
            busca = ManejaTalleres.BuscarTallerxID(taller)
            while busca == -1:
                print("El id ingresado no existe, vuelva a intentarlo")
                taller = int(input("Ingrese num de Taller: "))
                busca = ManejaTalleres.BuscarTallerxID(taller)
            inscripcion = ManejaTalleres.InscripcionaTaller(fecha_de_incripcion,persona,busca)
            ManejaPersonas.AgregarPersona(persona)
            ManejaInscripcion.Agregar_Al_Arreglo(inscripcion)
        except TypeError:
            print("Hubo un error de tipeo, vualva a intentarlo")
        input("Toque una tecla para continuar")
        os.system("cls")

    def op2 ():
        os.system("cls")
        try:
            dni = int(input("Ingrese dni de la persona: "))
            ManejaInscripcion.MostrarConsulta(dni)
        except TypeError:
            print("Hubo un error de tipeo")
        input("Toque una tecla para continuar")
        os.system("cls")

    def op3 ():
        os.system("cls")
        try:
            IdTaller = int(input("Ingrese el id del taller: "))
            ManejaTalleres.ConsultarInscriptos(IdTaller)
        except TypeError:
            print("Hubo un error de tipeo")
        input("Toque una tecla para continuar")
        os.system("cls")
    
    def op4 ():
        os.system("cls")
        try:
            dni = int(input("Ingrese dni de la persona: "))
            buscar = ManejaPersonas.BuscarxDni(dni)
            if buscar != -1:
                ManejaInscripcion.RegistrarPago(dni)
            else:
                print("El dni ingresado no es correcto")
        except TypeError:
            print("Hubo un error de tipeo")
        input("Toque una tecla para continuar")
        os.system("cls")

    def op5 ():
        ManejaInscripcion.GuardarArchivo()
        print("Archivo guardado..")

    def op6 ():
        print("Cerrando programa...")
    
    def op99 ():
        ManejaInscripcion.MostrarLen()
    ManejaPersonas = ManejadorPersona()
    ManejaInscripcion = ArregloIncripcion()
    opcion = None
    dicc = {1:op1,2:op2,3:op3,4:op4,5:op5,6:op5,99:op99}
    while opcion != 6:
        print("|---------------------------------------------------|")
        print("| Ingrese 1 para inscribir una persona en un taller |")
        print("| Ingrese 2 para consultar incripcion               |")
        print("| Ingrese 3 para consultar incriptos                |")
        print("| Ingrese 4 para registrar un pago                  |")
        print("| Ingrese 5 para guardar incriptos                  |")
        print("| Ingrese 6 para cerrar el programa                 |")
        print("|---------------------------------------------------|")
        opcion = int(input("Ingrese opcion: "))
        op = dicc.get(opcion,lambda: print("Opcion incorrecta"))
        op()
