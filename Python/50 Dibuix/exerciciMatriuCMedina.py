import os

import pygame.draw_py
import pygame.freetype
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
import random

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Window Title')

matriu = [[str(random.randint(0,9)) for _ in range(10)] for _ in range(10)]
font = pygame.font.SysFont("Courier New", 50)
square_clicked = False

# Variables de l'estat del ratolí
mouse_pos = { "x": -1, "y": -1 }
mouse_down = False

# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    global mouse_pos, mouse_down
    mouse_inside = pygame.mouse.get_focused()  # El ratolí està dins de la finestra?

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos["x"], mouse_pos["y"] = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
    return True

# Fer càlculs
def app_run():
    global mouse_pos,mouse_down,square_clicked

    if mouse_down:
        if (50 < mouse_pos["x"] < 550 and 
            50 < mouse_pos["y"] < 550):
            square_clicked = True
            index_x = int(mouse_pos["x"]//50-1)
            index_y = int(mouse_pos["y"]//50-1)
            n = matriu[index_x][index_y]
            if matriu[index_x+1][index_y] == n: matriu[index_x+1][index_y] = ""
            if matriu[index_x][index_y+1] == n: matriu[index_x+1][index_y] = ""
            if index_x > 0:
                if matriu[index_x-1][index_y] == n: matriu[index_x+1][index_y] = ""
            if index_y > 0:
                if matriu[index_x][index_y-1] == n: matriu[index_x+1][index_y] = ""
            matriu[index_x][index_y] = ""
    else:
        square_clicked = False

# Dibuixar
def app_draw():
    global matriu

    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    for x in range(50,501,50):
        for y in range(50,501,50):
            if (square_clicked and 
                x < mouse_pos["x"] < x+50 and
                y < mouse_pos["y"] < y+50):
                pygame.draw.rect(screen,GREEN,pygame.Rect(x,y,50,50))
            else:
                text = font.render(matriu[int(x/50-1)][int(y/50-1)],True,BLACK)
                screen.blit(text,(x+12.5,y))

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()
