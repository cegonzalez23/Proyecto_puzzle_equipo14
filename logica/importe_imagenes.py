from PIL import Image
import os

def partir_imagen(ruta_imagen, filas, columnas, carpeta_salida="piezas"):
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
    img = Image.open(ruta_imagen)

    ancho, alto = img.size
    ancho_pieza = ancho // columnas
    alto_pieza = alto // filas
    piezas = []

    for f in range(filas):
        fila_piezas = []
        for c in range(columnas):
            izquierda = c * ancho_pieza
            arriba = f * alto_pieza

            # --- cambios Celes: no me dejaba agregar una imágen mas grande, por lo que hago estos ajustes 
            # Si es la última columna, derecha = ancho 
            if c == columnas - 1:
                derecha = ancho
            else:
                derecha = izquierda + ancho_pieza
            # Si es la última fila, abajo = alto 
            if f == filas - 1:
                abajo = alto
            else:
                abajo = arriba + alto_pieza

            caja = (izquierda, arriba, derecha, abajo)
            pieza = img.crop(caja)
            ruta_pieza = os.path.join(carpeta_salida, f"pieza_{f}_{c}.png")
            pieza.save(ruta_pieza)
            fila_piezas.append(ruta_pieza)
        piezas.append(fila_piezas)

    piezas[-1][-1] = "-" # espacio vacio
    return piezas
