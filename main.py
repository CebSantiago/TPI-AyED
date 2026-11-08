########################################## CARGADO DE ARCHIVOS EN VARIABLES ##########################################
archivo_funcion = open("DB/funciones.txt", "r+")
funciones = archivo_funcion.readlines()
archivo_funcion.close()
archivo_obras = open("DB/obras.txt", "r+")
obras = archivo_obras.readlines()
archivo_obras.close()
archivo_salas = open("DB/salas.txt", "r+")
salas = archivo_salas.readlines()
archivo_salas.close()

########################################## FUNCIONES DE FUNCIONES XD ##########################################
def listar_funciones():    
    for i in range(1,len(funciones)):
        funcion= funciones[i].split("-")
        nombre_obra = obras[int(funcion[1])].split("-")
        print("-"*155)
        print(f"ID:{funcion[0]} - Nombre de la obra o espectáculo:{nombre_obra[1]}  -Fecha:{funcion[2]} -Horario:{funcion[3]} -Sala:{funcion[4]} -Precio de platea:${funcion[5]} - Precio de palco:${funcion[6]}")
        print("-"*155)
        
def buscar_funcion_por_id(id):
    if id.isdigit() == False:
        print("Upss, parece que solo se reciben valores numericos")
    else:
        if int(id)>len(funciones):
            print("Upss, parece que no tenemos ninguna obra con esa ID")
        else:
            funcion= funciones[int(id)].split("-")
            nombre_obra = obras[int(funcion[1])].split("-")
            print("-"*155)
            print(f"ID:{funcion[0]} - Nombre de la obra o espectáculo:{nombre_obra[1]}  -Fecha:{funcion[2]} -Horario:{funcion[3]} -Sala:{funcion[4]} -Precio de platea:${funcion[5]} - Precio de palco:${funcion[6]}")
            print("-"*155)

def buscar_funcion_por_nombre(input):
    encontrado = False
    largo_input =len(input)
    for i in range(1,len(funciones)):
        funcion= funciones[i].split("-")
        obra = obras[int(funcion[1])].split("-")
        nombre_obra= obra[1]
        
        chequeo_nombre_obra = nombre_obra[0:int(largo_input)]
        if input.lower() == chequeo_nombre_obra.lower():
            print("-"*155)
            print(f"ID:{funcion[0]} - Nombre de la obra o espectáculo:{nombre_obra}  -Fecha:{funcion[2]} -Horario:{funcion[3]} -Sala:{funcion[4]} -Precio de platea:${funcion[5]} - Precio de palco:${funcion[6]}")
            print("-"*155)
            encontrado = True
    if encontrado == False:
        print("Upss, parece que no tenemos obras que comiencen con ese nombre")

def listar_obras():
    for i in range(1,len(obras)):
        obra= obras[i].split("-")
        print("-"*155)
        print(f"ID:{obra[0]} - Nombre de la obra o espectáculo:{obra[1]}  -Genero:{obra[3]}")
        print("-"*155)
        
def listar_salas():
    for i in range(1,len(salas)):
        sala= salas[i].split("-")
        print("-"*155)
        print(f"ID:{sala[0]} - Descripcion:{sala[1]}")
        print("-"*155)
        
def registrar_funcion():
    id = len(funciones)
    id_obra = ""
    fecha = ""
    hora= ""
    id_sala=""
    precio_plat=""
    precio_palco = ""
    listar_obras()
    listar_salas()
    

def menu_funciones():
    opcion = ""

    while opcion != "6":

        print("\n======================================")
        print("        Teatro CaPaz S.A.")
        print("======================================")
        print("1. Registrar una nueva funcion")
        print("2. Consultar funciones registradas")
        print("3. Buscar funcion por ID")
        print("4. Buscador de funciones por nombre")
        print("5. Ordenar funciones por ...")
        print("6. Salir")
        print("======================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            #()
            pass
        elif opcion == "2":
            listar_funciones()
        elif opcion == "3":
            id_pedido = input("Ingrese el ID de la funcion que desea visualizar: ")
            buscar_funcion_por_id(id_pedido)
        elif opcion == "4":
            nombre_pedido = input("Ingrese el nombre o fragmento de nombre de la funcion que desea visualizar: ")            
            buscar_funcion_por_nombre(nombre_pedido)
        elif opcion == "5":
            pass
        elif opcion == "6":
            print("Gracias por utilizar el sistema.")

        else:
            print("Opción incorrecta. Intente nuevamente.")

def menu():
    opcion = ""

    while opcion != "8":

        print("\n======================================")
        print("        Teatro CaPaz S.A.")
        print("======================================")
        print("1. Administrar Funciones")
        print("2. Consultar ubicaciones")
        print("3. Realizar una venta")
        print("4. Consultas y reportes")
        print("5. Salir")
        print("======================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_funciones()
        elif opcion == "2":
            #()
            pass
        elif opcion == "3":
            #()
            pass
        elif opcion == "4":
            #()
            pass
        elif opcion == "5":
            print("Gracias por utilizar el sistema.")

        else:
            print("Opción incorrecta. Intente nuevamente.")


menu()


