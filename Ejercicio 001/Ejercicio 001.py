#espacio de importación de módulos
import json
import pickle
import os





#espacio para definición de funcionalidades del programa principal
def DetectarSerializacion() -> list:
    if os.path.exists('Ejercicio 001/tareas.pckl') and os.path.exists('Ejercicio 001/tareas.json'):
        while True:
            print("Dos archivos detectados 'tareas.pckl' y 'tareas.json'.")
            print("Solo se pueden cargar uno de estos ficheros en el programa principal.\n1. Cargar archivo.pckl\n2. Cargar archivo.json")
            try:
                cargar=int(input("Introduzca el nº correspondiente a la opción deseada >>> "))
            except:
                print("Error. Solamente es admisible entradas numéricas.")
            else:
                if cargar == 1:
                    ruta_actual=os.getcwd()
                    ruta_absoluta=os.path.join(ruta_actual, 'Ejercicio 001/tareas.pckl')
                    print(f"Cargando datos del fichero pckl guardado en la ruta {ruta_absoluta}.")
                    fichero = open(ruta_absoluta, 'rb')
                    datos=pickle.load(fichero)
                    fichero.close()
                    print("Fichero cargado con éxito. Transfiriendo datos al núcleo de la aplicación.")
                    return datos
                elif cargar == 2:
                    ruta_actual=os.getcwd()
                    ruta_absoluta=os.path.join(ruta_actual, 'Ejercicio 001/tareas.json')
                    print(f"Cargando datos del fichero json guardado en la ruta {ruta_absoluta}.")
                    with open (ruta_absoluta, "r") as jsonfile:
                        datos = json.load(jsonfile)
                    print("Fichero cargado con éxito. Transfiriendo datos al núcleo de la aplicación.")
                    return datos
                else:
                    print("Error. Escoja entre la carga de los dos archivos disponibles escribiendo el formato numérico y su identificación correctamente.")


    elif os.path.exists('Ejercicio 001/tareas.json'):
        print("Punto de carga detectado para archivo .json")
        while True:
            cargar=input("¿Desea cargar los datos guardados? s/n >>> ").lower()
            if cargar == 's':
                ruta_actual=os.getcwd()
                ruta_absoluta=os.path.join(ruta_actual, 'Ejercicio 001/tareas.json')
                print(f"Cargando datos del fichero json guardado en la ruta {ruta_absoluta}.")
                with open (ruta_absoluta, "r") as jsonfile:
                    datos = json.load(jsonfile)
                print("Fichero cargado con éxito. Transfiriendo datos al núcleo de la aplicación.")
                return datos    
            elif cargar == 'n':
                lista=[]
                print("Continuando a la aplicación principal sin datos cargados.")
                return lista
            else:
                print("Error. Responda s | n.")
    elif os.path.exists('Ejercicio 001/tareas.pckl'):
        print("Punto de carga detectado para archivo .pckl")
        while True:
            cargar=input("¿Desea cargar los datos guardados? s/n >>> ").lower()
            if cargar == 's':
                ruta_actual=os.getcwd()
                ruta_absoluta=os.path.join(ruta_actual, 'Ejercicio 001/tareas.pckl')
                print(f"Cargando datos del fichero pckl guardado en la ruta {ruta_absoluta}.")
                fichero = open(ruta_absoluta, 'rb')
                datos=pickle.load(fichero)
                fichero.close()
                print("Fichero cargado con éxito. Transfiriendo datos al núcleo de la aplicación.")
                return datos
            elif cargar == 'n':
                lista=[]
                print("Continuando a la aplicación principal sin datos cargados.")
                return lista
            else:
                print("Error. Responda s | n.")

    else:
        lista=[]
        print("No se han detectado archivos para cargar serialización del programa.")
        return lista

def ElegirSerializacion():
    ruta_actual=os.getcwd()
    ruta_absoluta=os.path.join(ruta_actual, 'Ejercicio 001/configuracionUsuario.json')

    if os.path.exists(ruta_absoluta):
        return None
    else:
        print("El sistema de guardado se establece de dos maneras:\n1. archivos .pckl.\n2. archivos .json")
        while True:
            formato=input("Elije el número que acompaña a la elección (1) | (2) >>> ")
            if formato == '1':
                print("Formato de guardado cambiado a archivos .pckl")
                esPckl=True
                with open('Ejercicio 001/configuracionUsuario.json', 'w') as configuracion:
                    json.dump(esPckl, configuracion)
                break
            elif formato == '2':
                print("Formato de guardado cambiado a archivos .json")
                esPckl=False
                with open('Ejercicio 001/configuracionUsuario.json', 'w') as configuracion:
                    json.dump(esPckl, configuracion)
                break
            else:
                print("Formato inválido. Asegúrese de escoger entre (1) o (2).")
                continue
def AgregarTareas()->list:
    #nombre, fecha_limite, estado (pendiente o completada)
    listaTareas=[]
    while True:
        nombre=input("Escribe por favor el nombre de la nueva tarea >>> ")
        if nombre != '':
            break
        else:
            print("Error. El nombre de la tarea no puede ser una cadena vacía.")
    while True:
        fecha_limite=input("Detalla la fecha límite de la tarea en el siguiente formato (DD/MM/AAAA) >>> ")
        if len(fecha_limite)==10 and fecha_limite[2]=='/' and fecha_limite[5]=='/' and fecha_limite[:2].isdigit() and fecha_limite[3:5].isdigit() and fecha_limite[6:].isdigit():
            fechaLim=fecha_limite.split('/')
            listaAux=[]
            for elto in fechaLim:
                elto=int(elto)
                listaAux.append(elto)
            if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=2024 and listaAux[2]<=2025: #Calendario 2024/2025
                print("Fecha correctamente validada. Registrando.")
                break
            else:
                print("Error. La fecha debe seguir el formato del calendario 2024/2025.")
        else:
            print("Error. Formato de fecha inválido.")
    while True:
        estado=input("La tarea solo puede estar en dos estados: (P)endiente y (C)ompletada.\nEscoja entre las dos letras >>> ").lower()
        if estado == 'p':
            estado='Pendiente'
            print(f"Estado de la tarea configurado a {estado}.")
            break
        elif estado == 'c':
            estado='Completada'
            print(f"Estado de la tarea configurado a {estado}.")
            break
        else:
            print("Error. Sólo se permite escoger entre los dos estados facilitados.")
    if nombre and fecha_limite and estado:
        print("Datos cargados y listos para guardarse en el registro.")
        dTareas={'nombre':nombre,
                 'fecha_limite': fecha_limite,
                 'estado': estado}
        listaTareas.append(dTareas)
        print("Guardando...")
        print("¡Datos guardados!\nVolviendo al menú principal.")
        return listaTareas
    else:
        print("Hubo un error inesperado. Volviendo al menú principal.")
        return None
    #filtrar aquellas tareas que tengan tareas pendientes primero
def ModificarTarea(listaTareas: list) -> list:
    while True:
        # Filtrar tareas pendientes
        listaPendientes = []
        for elemento in listaTareas:
            for tareas in elemento:
                if tareas['estado'] == 'Pendiente':
                    listaPendientes.append(tareas)

        if listaPendientes:
            # Mostrar tareas pendientes
            for elemento in listaPendientes:
                print(f"Nombre tarea: {elemento['nombre']}\t\t\tEstado: {elemento['estado']}")

            nombresTareas=[]
            for elemento in listaPendientes:
                nombresTareas.append(elemento['nombre'])


            while True:
                modificar = input("Escriba de manera literal y sin equivocarse el nombre de la tarea que quiera completar >>>")

                if modificar != '' and modificar in nombresTareas:
                    # Modificar estado de la tarea seleccionada
                    for elemento in listaTareas:
                        for tareas in elemento:
                            if tareas['nombre'] == modificar and tareas['estado'] == 'Pendiente':
                                tareas['estado'] = 'Completada'
                                print("Tarea modificada a 'completada' con éxito")

                                # Eliminar la tarea completada de la lista de tareas pendientes
                                nombresTareas.remove(modificar)
                                break
                    break  # Salir del bucle interno después de completar la tarea

                elif modificar == '':
                    print("Error. No pueden existir cadenas vacías.")
                elif modificar != '' and modificar not in nombresTareas:
                    print("Error. La tarea no existe en la base de datos.")

            # Preguntar si desea modificar más tareas
            masTareas = input("¿Desea modificar más tareas? s/n >>> ")
            if masTareas.lower() == 's':
                continue  # Continuar con el proceso si la respuesta es 's'
            else:
                return listaTareas  # Salir de la función y devolver la lista de tareas

        else:
            print("Ya no quedan más tareas pendientes. Volviendo al menú principal.")
            return listaTareas  # Si no hay tareas pendientes, devolver la lista y salir



def EliminarTarea(listaTareas: list) -> list:
    #Se filtran ahora las tareas que están completadas:
    while True:
        listaTareasCompletadas=[]
        for elto in listaTareas:
            for subelto in elto:
                if subelto['estado']=='Completada':
                    listaTareasCompletadas.append(subelto)
        if listaTareasCompletadas: #si hay aún elementos en la lista de tareas completadas:
            for elto in listaTareasCompletadas:
                print(f"Nombre tarea: {elto['nombre']} \t\t\t Estado: {elto['estado']}")
            nombresCompletadas=[]
            for elto in listaTareasCompletadas:
                nombresCompletadas.append(elto['nombre'])
            while True:
                eliminar=input("Escribe de manera literal el nombre de la tarea completada para eliminarla del sistema >>> ")
                if eliminar!= '' and eliminar in nombresCompletadas:
                    for elto in listaTareas:
                        for subelto in elto:
                            if subelto['nombre']==eliminar:
                                listaTareas.remove(elto)
                                nombresCompletadas.remove(eliminar)
                                print(f"Tarea {eliminar} eliminada con éxito.")
                                break
                    break
                elif eliminar=='':
                    print("Error. La cadena no puede estar vacía.")
                elif eliminar!=''and eliminar not in nombresCompletadas:
                    print("Error. La tarea no existe en la base de datos.")

            masTareas = input("¿Desea modificar más tareas? s/n >>> ")
            if masTareas.lower() == 's':
                continue  # Continuar con el proceso si la respuesta es 's'
            else:
                return listaTareas  # Salir de la función y devolver la lista de tareas

        else:
            print("Ya no quedan más tareas completadas. Volviendo al menú principal.")
            return listaTareas  


def ListarTareas(listaTareas:list) -> list:
    #recorreremos la lista completa hasta mostrar los estados de las tareas de manera elegante
    if listaTareas:
        numerador=0
        for elemento in listaTareas:
            for subelemento in elemento:
                numerador+=1
                print(f"{numerador}. Tarea: {subelemento['nombre']}\f Fecha límite: {subelemento['fecha_limite']}\f Estado: {subelemento['estado']}", end="\n")
    else:
        print("¡Vaya! ¡Parece que aún no hay ninguna tarea! ¿Qué tal si agregas nuevas tareas?")

def CambiarFormato():
    directorio_trabajo=os.getcwd()
    directorioConfiguracion=os.path.join(directorio_trabajo, 'Ejercicio 001/configuracionUsuario.json')
    print("Abriendo el archivo de configuración de guardados:")
    with open(directorioConfiguracion, 'r') as archivo:
        datos=json.load(archivo)
    if datos == True:
        while True:
            print("El formato actual es .pckl - ¿Deseas cambiarlo?")
            cambiar=input("s | n >>> ").lower()
            if cambiar == 's':
                datos=False
                with open(directorioConfiguracion, 'w') as archivo:
                    json.dump(datos, archivo)
                print("Datos cambiados. Formato de entrada: json")
                break
            if cambiar == 'n':
                print("El programa seguirá gestionando los guardados en el formato pckl.")
                break
            else:
                print("Error. Escoja adecuadamente entre s o n.")
    else:
        while True:
            print("El formato actual es .jason - ¿Deseas cambiarlo?")
            cambiar=input("s | n >>> ").lower()
            if cambiar == 's':
                datos=True
                with open(directorioConfiguracion, 'w') as archivo:
                    json.dump(datos, archivo)
                print("Datos cambiados. Formato de entrada: pckl")
                break
            if cambiar == 'n':
                print("El programa seguirá gestionando los guardados en el formato json.")
                break
            else:
                print("Error. Escoja adecuadamente entre s o n.")

def GuardarDatos(tareas:list) -> list:
    #Se carga primero la configuración de guardado elegida por el usuario la primera vez que hizo uso de la aplicación
    directorio_trabajo=os.getcwd()
    directorio_archivo=os.path.join(directorio_trabajo, 'Ejercicio 001/configuracionUsuario.json')
    with open(directorio_archivo, 'r') as archivoGuardado:
        esPickl=json.load(archivoGuardado)
    if esPickl:
        directorio_pckl=os.path.join(directorio_trabajo, 'Ejercicio 001/tareas.pckl')
        archivoGuardadoPckl= open (directorio_pckl, 'wb')
        pickle.dump(tareas, archivoGuardadoPckl)
        archivoGuardadoPckl.close()
    if not esPickl:
        directorio_json=os.path.join(directorio_trabajo, 'Ejercicio 001/tareas.json')
        with open (directorio_json, 'w') as archivoGuardadoJson:
            json.dump(tareas, archivoGuardadoJson, sort_keys=True, indent=4)
    #funcion de lectura de archivo de guardado de la configuracion de usuarios

#programa prncipal

if __name__=='__main__':
#espacio para carga de otras funciones  
    tareas=DetectarSerializacion()
    defectoPickl=ElegirSerializacion()
    esPickl=None
#mainloop - menu de la aplicación 
    while True:
        print("------------------------------------")
        print("Menú principal de la aplicación")
        print("------------------------------------")
        print()
        print(" ----------")
        print("| Opciones |")
        print(" ----------")
        print("1. Agregar tareas.\n2. Modificar estados de las tareas.\n3. Eliminar tareas.\n4. Listar tareas.\n5. Cambiar formato de serialización.\n6. Guardar y salir del programa.")
        print()
        try:
            eleccion=int(input("Escoja entre los números que representan las distintas funciones del programa >> "))
        except:
            print("Error. La entrada debe ser numérica y deben estar sezgadas a las opciones que aparecen en el menú.")
        else:
            match eleccion:
                case 1 :
                    while True:
                        print("Agregando tareas...")
                        nuevaTarea=AgregarTareas()
                        tareas.append(nuevaTarea)
                        break
                case 2 : 
                        print()
                        print("----------------------------")
                        print("Listado de tareas pendientes")
                        print("----------------------------")
                        print()
                        ModificarTarea(tareas)
                        continue
                case 3 :
                        print("Eliminando tareas completadas...")
                        EliminarTarea(tareas)
                        continue
                case 4:
                        print("Listando tareas actuales...")
                        ListarTareas(tareas)
                        continue
                case 5:
                        print("Cambiando formato de serialización...")
                        CambiarFormato()
                        continue
                case 6:
                    while True:
                        print("Se procede a salir de la aplicación.\n¿Desea guardar los datos actuales?")
                        guardar=input('s/n >>> ').lower()
                        if guardar == 's':
                            GuardarDatos(tareas)
                            exit()
                        elif guardar == 'n':
                            print("Saliendo de la aplicación sin guardar los cambios realizados.")
                            exit()
                        else:
                            print("Error. Seleccione correctamente (s) para guardar y salir o (n) para salir sin guardar cambios.")

                case _:
                    print("Error. Seleccione entre los números que figuran entre las distintas opciones del programa.")
                    continue

