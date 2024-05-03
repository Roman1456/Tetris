import pygame
from pygame import *
from Brick import Brick

window = pygame.display.set_mode((500,700))
fps = pygame.time.Clock()

brick1 = []
brick1.append(Brick(300,390,200,200, "Papka/pixil-frame-0 (1).png"))
brick1.append(Brick(100,250,200,200, "Papka/pixil-frame-0.png"))
brick1.append(Brick(50,400,200,200, "Papka/pixil-frame-1.png"))
brick1.append(Brick(250,300,200,200, "Papka/pixil-frame-2.png"))




game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

        if event.type == pygame.QUIT:
            pygame.quit()



    for brick in brick1:
        brick.draw(window)

    pygame.display.flip()
    fps.tick(60)