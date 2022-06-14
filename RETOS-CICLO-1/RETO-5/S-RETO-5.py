import pandas as pd
# ruta file csv
rutaFileCsv ="https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true"

def listaPeliculas(rutaFileCsv: str) -> str:
    if rutaFileCsv.split(".")[-1] != "csv":
        try:
            archivo_csv = pd.read_csv(rutaFileCsv)
            sub_grupo_peliculas = archivo_csv[["Country","Language","Gross Earnings"]]
            ganancias_pais_lenguaje = sub_grupo_peliculas.pivot_table(index=["Country","Language"])
            return ganancias_pais_lenguaje.head(10)
        except:
            print("Error al leer el archivo de datos.")
    else:
        print("Extensión inválida.")
