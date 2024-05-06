import pygame
import random
from random import *
from pygame import *
from Brick import Brick


window = pygame.display.set_mode((500,700))
fps = pygame.time.Clock()

backround = pygame.transform.scale(
    pygame.image.load("Papka/download.jpg"),(500,700)
)

brick1 = []

for i in range(1):
    brick1.append(Brick(300,390,200,200, "Papka/pixil-frame-0 (1).png",5))
    brick1.append(Brick(100,250,200,200, "Papka/pixil-frame-0.png",5))
    brick1.append(Brick(50,400,200,200, "Papka/pixil-frame-1.png",5))
    brick1.append(Brick(250,300,200,200, "Papka/pixil-frame-2.png",5))
    brick1.append(Brick(100,400,200,200,"Papka/pixil-frame-3.png",5))
    brick1.append(Brick(56,50,200,200, "Papka/pixil-frame-4.png",5))
    brick1.append(Brick(350,500,200,200, "Papka/pixil-frame-5.png",5))




game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

        if event.type == pygame.QUIT:
            pygame.quit()

        if 



    window.blit(backround, (0, 0))
    for brick in brick1:
        brick.draw(window)
        brick.move()
    pygame.display.flip()
    fps.tick(60)