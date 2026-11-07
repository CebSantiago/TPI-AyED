########################################## CARGADO DE ARCHIVOS EN VARIABLES ##########################################
archivo_funcion = open("DB/funciones.txt", "r+")
funciones = archivo_funcion.readlines()
archivo_funcion.close()
archivo_obras = open("DB/obras.txt", "r+")
obras = archivo_obras.readlines()
archivo_obras.close()

########################################## FUNCIONES DE FUNCIONES XD ##########################################
def listar_funciones():    
    for i in range(1,len(funciones)):
        funcion= funciones[i].split("-")
        nombre_obra = obras[int(funcion[1])].split("-")
        print("-"*155)
        print(f"ID:{funcion[0]} - Nombre de la obra o espectáculo:{nombre_obra[1]}  -Fecha:{funcion[2]} -Horario:{funcion[3]} -Sala:{funcion[4]} -Precio de platea:${funcion[5]} - Precio de palco:${funcion[6]}")
        print("-"*155)
        
def buscar_funcion_por_id(id):
        funcion= funciones[id].split("-")
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
        print("No hubo coincidencias")

### pruebas ###
listar_funciones()
buscar_funcion_por_id(2)
buscar_funcion_por_nombre("qq")
buscar_funcion_por_nombre("la")

