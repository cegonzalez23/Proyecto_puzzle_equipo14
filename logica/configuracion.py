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
