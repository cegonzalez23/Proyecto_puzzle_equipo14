import os

def obtener_tamaño():
    try:
        cant_colum_filas = int(input("Ingresar cantidad de columnas/filas del rompecabezas, hasta 5: "))
        if cant_colum_filas > 5 or cant_colum_filas < 2:
            print("Tamaño no válido. Se establecerá una configuración por defecto de 3x3")
            return 3
        return cant_colum_filas
    except ValueError:
        print("La entrada no es válida. Se establecerá una configuración por defecto de 3x3")
        return 3


#Verificar reglamento
if os.path.exists("reglamento.txt"):
    def mostrar_reglamento():
        with open('reglamento.txt', 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print(contenido)
    mostrar_reglamento()
else:
    print("No se encontró el archivo 'reglamento.txt'.")