import pygame
pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
color = (255,255, 255)
screen = pygame.display.set_mode([WIDTH,HEIGHT])

icon = pygame.image.load("app_image.gif")
pygame.display.set_icon(icon)
pygame.display.set_caption("Hover Paint")




run = True
while run:
    timer.tick(fps)
    screen.fill(color)

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
