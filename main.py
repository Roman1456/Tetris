import pygame
from pygame import *


window = pygame.display.set_mode((500,700))
fps = pygame.time.Clock()


#backround = pygame.transform.scale(
  #  pygame.image.load("Papka/"),(700,500)
#)


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()







   # window.blit(backround,(0,0))


    pygame.display.flip()
    fps.tick(60)