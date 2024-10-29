import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)  

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Direcció del moviment
dir_x = "none"
dir_y = "none"

# Posició de l'objecte
pox_x = 100
pox_y = 100

ample = 15
alt = 15

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
    global dir_x, dir_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.KEYDOWN:  # Tecla premuda
            if event.key == pygame.K_UP:
                dir_y = 'up'
            elif event.key == pygame.K_DOWN:
                dir_y = 'down'
            elif event.key == pygame.K_LEFT:
                dir_x = 'left'
            elif event.key == pygame.K_RIGHT:
                dir_x = 'right'
        elif event.type == pygame.KEYUP:  # Tecla alliberada
            if event.key == pygame.K_UP:
                if dir_y == 'up':
                    dir_y = 'none'
            elif event.key == pygame.K_DOWN:
                if dir_y == 'down':
                    dir_y = 'none'
            elif event.key == pygame.K_LEFT:
                if dir_x == 'left':
                    dir_x = 'none'
            elif event.key == pygame.K_RIGHT:
                if dir_x == 'right':
                    dir_x = 'none'
    return True

# Fer càlculs
def app_run():
    global dir_x, dir_y, pox_x, pox_y, ample, alt

    delta_time = clock.get_time() / 1000.0  # Convertir a segons
    
    speed = 50  # píxels per segon
    displacement = speed * delta_time

    if (dir_x == "right"):
        pox_x = pox_x + displacement
        if (pox_x > 200 - ample):
            pox_x = 200 - ample
    elif (dir_x == "left"):
        pox_x = pox_x - displacement
        if (pox_x < 100):
            pox_x = 100

    if (dir_y == "down"):
        pox_y = pox_y + displacement
        if (pox_y > 200 - alt):
            pox_y = 200 - alt
    elif (dir_y == "up"):
        pox_y = pox_y - displacement
        if (pox_y < 100):
            pox_y = 100

# Dibuixar
def app_draw():
    global pox_x, pox_y

    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Draw limits
    pygame.draw.rect(screen, BLUE, pygame.Rect(100, 100, 100, 100), 2)

    # Draw moving object
    pygame.draw.rect(screen, ORANGE, pygame.Rect(pox_x, pox_y, ample, alt))

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()