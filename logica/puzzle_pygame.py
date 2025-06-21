import pygame
import sys
import tkinter as tk
from tkinter import filedialog
from configuracion import obtener_tamaño
from importe_imagenes import partir_imagen
from matriz import matriz_imagen_aleatoria
from movimientos import mover

TAM_CELDA = 150  # Tamaño de cada celda en píxeles, podemos agreandarla

def seleccionar_imagen():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    ruta_imagen = filedialog.askopenfilename(
        title="Selecciona una imagen para el rompecabezas",
        filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    root.destroy()
    return ruta_imagen

def cargar_imagenes(matriz, tam_celda):
    imagenes = []
    for fila in matriz:
        fila_img = []
        for pieza in fila:
            if pieza == "-":
                fila_img.append(None)
            else:
                img = pygame.image.load(pieza)
                img = pygame.transform.scale(img, (tam_celda, tam_celda))
                fila_img.append(img)
        imagenes.append(fila_img)
    return imagenes

def main():
    pygame.init()
    tamaño = obtener_tamaño()
    ruta_imagen = seleccionar_imagen()
    if not ruta_imagen:
        print("No se seleccionó ninguna imagen. Cerrando el juego.")
        return
    piezas = partir_imagen(ruta_imagen, tamaño, tamaño)
    matriz = matriz_imagen_aleatoria(piezas)
    imagenes = cargar_imagenes(matriz, TAM_CELDA)

    ancho = tamaño * TAM_CELDA
    alto = tamaño * TAM_CELDA
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Rompecabezas")

    clock = pygame.time.Clock()
    running = True
    paused = False
# cambio de celes: le agrego esto porque cuando lo probaba no tenia un mensaje de salida y se me colgaba la terminal
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused  # Pausa/reanuda
                if not paused:
                    if event.key == pygame.K_w:
                        mover(matriz, 'w')
                    elif event.key == pygame.K_s:
                        mover(matriz, 's')
                    elif event.key == pygame.K_a:
                        mover(matriz, 'a')
                    elif event.key == pygame.K_d:
                        mover(matriz, 'd')
                    imagenes = cargar_imagenes(matriz, TAM_CELDA)

        screen.fill((50, 50, 50))

        # Mensaje de pausa
        if paused:
            font = pygame.font.SysFont(None, 60)
            texto = font.render("PAUSA", True, (255,255,255))
            screen.blit(texto, (ancho//2 - texto.get_width()//2, alto//2 - texto.get_height()//2))

        if not paused:
            for f, fila in enumerate(matriz):
                for c, pieza in enumerate(fila):
                    img = imagenes[f][c]
                    if img:
                        rect = img.get_rect(topleft=(c * TAM_CELDA, f * TAM_CELDA))
                        screen.blit(img, rect)
                    else:
                        pygame.draw.rect(screen, (100, 100, 100), (c * TAM_CELDA, f * TAM_CELDA, TAM_CELDA, TAM_CELDA))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
