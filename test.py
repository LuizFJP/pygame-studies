import pygame
from pygame.locals import *
from sys import exit

pygame.init()

width = 640
height = 480

rectX = width/2
rectY = height/2

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogão')
clock = pygame.time.Clock()

while True:
  clock.tick(30)
  screen.fill((0,0,0))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
    '''if event.type == KEYDOWN:
      if event.key == K_a:
        rectX -= 20'''

    if pygame.key.get_pressed()[K_a] and rectX > 0:
      rectX -= 20
    if pygame.key.get_pressed()[K_d] and rectX < 600:
      rectX += 20
    if pygame.key.get_pressed()[K_w] and rectY > 0:
      rectY -= 20
    if pygame.key.get_pressed()[K_s] and rectY < 425:
      rectY += 20
  pygame.draw.rect(screen, (246, 0, 89), (rectX, rectY, 40, 50))

  pygame.display.update()