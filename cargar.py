peliculas = {}

def leer_doc():
    while True:
        archivo = input("\nIngrese el nombre del archivo: ")
        try:    
            with open(archivo + ".lfp", encoding="utf-8") as file: 
                for linea in file:
                        #strip borra espacios y split los separa segun el dato provisto
                    valores = linea.strip().split(";")
                    if len(valores) == 4:  
                        pelicula, actores, año, genero = valores 
                        if pelicula in peliculas:
                            # Si la película ya existe en el diccionario, verifica si cada actor ya está presente en la lista de actores
                            actor = actores.strip().split(",")
                            for i in actor:
                                if i not in peliculas[pelicula]["actores"]:
                                    peliculas[pelicula]["actores"].append(actor)
                        else:
                            # Si la película no existe, crea una nueva entrada en el diccionario
                            peliculas[pelicula] = {
                                "actores": actores.strip().split(","),
                                "año": int(año),
                                "genero": genero
                            }
                    else:
                        print("Formato de línea incorrecto:", linea.strip())
            print("\n...Carga Exitosa...")
            print("-------------------")
        except FileNotFoundError:
            print("El documento no existe o se escribió de manera incorrecta")
        break

print("Esto imprimira este texto ")

