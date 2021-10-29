import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
backgroundMusic = pygame.mixer.music.load("./audio-media/backSound.wav")
pygame.mixer.music.play(-1)
collisionMusic = pygame.mixer.Sound('./audio-media/colisao.wav')

width = 640
height = 480

rectX = width/2
rectY = height/2
purpleRectX = 100
purpleRectY = 400

counterCollider = 0
fontScore = pygame.font.SysFont('Arial', 20, True, True)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogão')
clock = pygame.time.Clock()

while True:
  clock.tick(30)
  screen.fill((0,0,0))
  scoreText = f'Colliders: {counterCollider}'
  scoreRendered = fontScore.render(scoreText, True, (240, 240, 240))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
    
    ##################### PINK SQUARE MOVEMENT ######################
    if pygame.key.get_pressed()[K_a] and rectX > 0:
      rectX -= 20
    if pygame.key.get_pressed()[K_d] and rectX < 600:
      rectX += 20
    if pygame.key.get_pressed()[K_w] and rectY > 0:
      rectY -= 20
    if pygame.key.get_pressed()[K_s] and rectY < 425:
      rectY += 20

    redRect = pygame.draw.rect(screen, (246, 0, 89), (rectX, rectY, 40, 50))
    purpleRect = pygame.draw.rect(screen, (69, 0, 246), (purpleRectX, purpleRectY, 40, 50))

    if redRect.colliderect(purpleRect):
      purpleRectX = randint(40, 600)
      purpleRectY = randint(50, 430)
      counterCollider += 1
      pygame.mixer.Sound.play(collisionMusic)

    screen.blit(scoreRendered, (500, 40))
    pygame.display.update()