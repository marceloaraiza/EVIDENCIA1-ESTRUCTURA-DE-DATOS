from tabulate import tabulate
import datetime

salas_num=[1,2,3,4]
reservaciones={}
clientes={}
salas={}
lista_reservaciones=[]

def num_salas():
    print("SALAS PARA RESERVACIONES: [1] [2] [3] [4]")

def menu_principal():
    print("xxxxxxxxxxxxMENU PRINCIPALxxxxxxxxxxxx")
    print("[1] REGISTRAR RESERVACION DE SALA.")
    print("[2] MODIFICAR EL NOMBRE DEL EVENTO DE UNA RESERVACIÓN.")
    print("[3] CONSULTAR LAS RESERVACIONES EXISTENTES PARA UNA FECHA ESPECIFICA.")
    print("[4] REGISTRAR UN NUEVO CLIENTE.")
    print("[5] REGISTRAR UNA NUEVA SALA.")
    print("[6] SALIR.")

def capturafechareserva():
    while True:
        cadena_fecha_reservacion = input("INGRESE LA FECHA DE RESERVACIÓN EN EL FORMATO (DD/MM/AAAA): \n")
        #Comprueba que la fecha de reservacion sea existente.
        fecha_reservacion = datetime.datetime.strptime(cadena_fecha_reservacion, "%d/%m/%Y")
        #A la fecha de reservacion le quita dos dias.
        fecha_reservacion_procesada = (fecha_reservacion - datetime.timedelta(days=+2)).date()
        #Extrae la fecha actual del sistema.
        fecha_actual = datetime.date.today()

        if fecha_reservacion_procesada>=fecha_actual:
            break
        else:
            print("LA RESERVACIONES SOLO SE PUEDEN REALIZAR COMO MINIMO CON DOS DIAS DE ANTICIPACIÓN. ")
            continue
    return fecha_reservacion.strftime('%d/%m/%Y')

def actualizar_reserva():
    while True:
        llave_reservaciones = int(input("INGRESE LA LLAVE PRIMARIA DEL EVENTO QUE SE VA MODIFICAR: \n"))
        if llave_reservaciones in reservaciones:
            for llave,valores in reservaciones.items():
                nvo_nombre = input("INGRESE EL NUEVO NOMBRE DEL EVENTO \n").upper()
                fecha_modificada = capturafechareserva()
                if llave==llave_reservaciones:
                    reservaciones[llave]=(nvo_nombre,valores[1],valores[2],valores[3],fecha_modificada)
        else:
            print("RESERVACIÓN NO ENCONTRADA")

        return print("NOMBRE Y FECHA DE LA RESERVACIÒN MODIFICADAS.")


switch = True

while switch:
    menu_principal()
    opcion = int(input("INGRESE EL NUMERO DE OPCION DEL MENU PRINCIPAL QUE SE DESEA REALIZAR: \n"))

    if opcion==1:
        #Busca la llave mas alta de el diccionario reservaciones, sino encuentra, toma como valor mas alto el 0.
        generador_llave_reservaciones=max(list(reservaciones.keys()),default=0) + 1

        while True:
            #Numero de sala.
            num_salas()
            num_sala=int(input("INGRESE EL NUMERO DE SALA QUE SE DESEA RESERVAR \n"))
            if num_sala in salas_num:
                print("EL NUMERO DE SALA CAPTURADO.")
                break
            else:
                print("EL NUMERO DE SALA NO EXISTE.")
                continue

        while True:
            #Buscar sala existente.
            clave_sala=int(input("INGRESE LA CLAVE DE LA SALA REGISTRADA DONDE SE HARA LA RESERVACIÓN: \n"))
            if clave_sala in salas:
                print("SALA EXISTENTE.")
                break
            else:
                print("SALA NO EXISTE.")
                continue

        while True:
            #Buscar cliente registrado.
            clave_cliente=int(input("INGRESE LA CLAVE DEL CLIENTE REGISTRADO QUE REALIZA LA RESERVACIÓN: \n"))
            if clave_cliente in clientes:
                print("CLIENTE EXISTE.")
                nom_cliente = clientes[clave_cliente]
                break
            else:
                print("CLIENTE NO EXISTE.")
                continue

        #Captura el turno de la fecha de reservacion.
        turno = input("INGRESE EL TURNO DEL EVENTO: [M] MATUTINO [V] VESPERTINO [N] NOCTURNO \n").upper()

        #Captura la fecha de reservacion de sala.
        fecha_reservacion = capturafechareserva()

        #Captura el nombre del evento a registrar.
        nombre_evento=input("INGRESE EL NOMBRE DEL EVENTO: \n").upper()

        #Desempaqueta el diccionario de las reservaciones, recorre cada reservacion y
        #revisa que no se repita sala, dia y turno. Si esto pasa no se completa la reservacion.
        for clave, datos in list(reservaciones.items()):
            if (num_sala,turno,fecha_reservacion) == (datos[1],datos[3],datos[4]):
                print("NO SE PUEDE TENER DOS RESERVACIONES AL MISMO TIEMPO")
                break
        else:
            print("TURNO Y SALAS DISPONIBLES")
            reservaciones[generador_llave_reservaciones]=(nombre_evento,num_sala,nom_cliente,turno,fecha_reservacion)
            print(f"LA PRIMARY KEY DE LA RESERVACIÓN {nombre_evento} ES: {generador_llave_reservaciones}.")

    elif opcion==2:
        actualizar_reserva()

    elif opcion==3:
        #consultar reservaciones de una fecha especifica
        fecha_consulta = input("INGRESE LA FECHA DE LAS RESERVACIÓNES PARA CONSULTAR EN EL FORMATO (DD/MM/AAAA): \n")
        print(f"REPORTE DE RESERVACIONES AL DIA {fecha_consulta}")
        for clave, datos in list(reservaciones.items()):
            if datos[4]==fecha_consulta:
                lista_reservaciones.append(datos)
            else:
                print("FECHA NO ENCONTRADA.")
        print (tabulate(list(lista_reservaciones),headers=["NOMBRE EVENTO","SALA","CLIENTE","TURNO","FECHA"],tablefmt='grid'))
        #Limpia los datos de la lista..
        lista_reservaciones.clear()
    elif opcion == 4:
        nombre_cliente = input("INGRESE EL NOMBRE DEL CLIENTE QUE SE VA REGISTRAR: \n").upper()
        generador_llave_cliente=max(list(clientes.keys()),default=0) + 1
        clientes[generador_llave_cliente]= (nombre_cliente)
        print("CLIENTE REGISTRADADO CORRECTAMENTE. ")
        print(f"LA PRIMARY KEY DEL CLIENTE {nombre_cliente} ES: {generador_llave_cliente}.")
    
    elif opcion == 5:
        #Pide al usuario el nombre de la sala.
        nombre_sala = input("INGRESE EL NOMBRE DE LA SALA QUE SE VA REGISTRAR: \n").upper()
        #Pide al usuario la capacidad de personas de la sala.
        cupo_sala = int(input("INGRESE LA CAPACIDAD DE PERSONAS DE LA SALA: \n"))
        #Busca la llave mas alta de el diccionario salas, sino encuentra, toma como valor mas alto el 0.
        generador_llave_sala=max(list(salas.keys()),default=0) + 1
        #Registra la informacion de la sala en el diccionario salas.
        salas[generador_llave_sala]= (nombre_sala,cupo_sala)
        print("SALA REGISTRADA CORRECTAMENTE. ")
        print(f"LA PRIMARY KEY DE LA SALA {nombre_sala} ES: {generador_llave_sala}.")

    elif opcion == 6:
        break