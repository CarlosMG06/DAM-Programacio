import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Bucle de l'aplicació
def main():
    global im_shinnosuke, im_shiro
    is_looping = True

    im_shinnosuke = pygame.image.load('./assets/exercici002/shinnosuke.png')
    im_shinnosuke = scale_image(im_shinnosuke, target_width=100)

    im_shiro = pygame.image.load('./assets/exercici002/shiro.png')
    im_shiro = scale_image(im_shiro, target_width=75)

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    global im_shinnosuke

    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)
    
    screen.blit(im_shinnosuke, (325, 160))
    screen.blit(im_shiro, (225, 205))

    pygame.display.update()

def scale_image(im_shinnosuke, target_width=None, target_height=None):

    original_width, original_height = im_shinnosuke.get_size()
    aspect_ratio = original_height / original_width

    if target_width and not target_height:  # Escalar per ample mantenint la proporció
        new_width = target_width
        new_height = int(target_width * aspect_ratio)
    elif target_height and not target_width:  # Escalar per altura mantenint la proporció
        new_height = target_height
        new_width = int(target_height / aspect_ratio)
    elif target_width and target_height:  # Escalar deformant la imatge
        new_width = target_width
        new_height = target_height
    else:
        raise ValueError("Especifica almenys un dels dos paràmetres: target_width o target_height.")

    scaled_im_shinnosuke = pygame.transform.scale(im_shinnosuke, (new_width, new_height))
    return scaled_im_shinnosuke

if __name__ == "__main__":
    main()