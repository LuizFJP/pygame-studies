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

xSnake = width/2
ySnake = height/2
xApple = 100
yApple = 400

counterCollider = 0
fontScore = pygame.font.SysFont('Arial', 20, True, True)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogão')
clock = pygame.time.Clock()
positionSnake = []

def increaseSnake(positionSnake):
  for XandY in positionSnake:
    pygame.draw.rect(screen, (23, 118, 181), (XandY[0], XandY[1], 20, 20))

initialSize = 0
velocity = 10
xControl = 20
yControl = 0

while True:
  clock.tick(30)
  screen.fill((15,2,60))
  scoreText = f'Colliders: {counterCollider}'
  scoreRendered = fontScore.render(scoreText, True, (240, 240, 240))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()

    ##################### PINK SQUARE MOVEMENT ######################
    if event.type == KEYDOWN:
      if event.key == K_a and xControl != velocity:
        xControl = -velocity
        yControl = 0
      if event.key == K_d and xControl != -velocity:
        xControl = velocity
        yControl = 0
      if event.key == K_w and yControl != velocity:
        xControl = 0
        yControl = -velocity
      if event.key == K_s and yControl != -velocity:
        xControl = 0
        yControl = velocity

    xSnake += xControl
    ySnake += yControl
    snake = pygame.draw.rect(screen, (23, 118, 181), (xSnake, ySnake, 20, 20))
    apple = pygame.draw.rect(screen, (124, 0, 0), (xApple, yApple, 20, 20))

    if snake.colliderect(apple):
      xApple = randint(40, 600)
      yApple = randint(50, 430)
      counterCollider += 1
      initialSize += 1
      pygame.mixer.Sound.play(collisionMusic)

    headSnakeList = []
    headSnakeList.append(xSnake)
    headSnakeList.append(ySnake)
    positionSnake.append(headSnakeList)
    increaseSnake(positionSnake)
 
    if(len(positionSnake) > initialSize):
      del positionSnake[0]

    screen.blit(scoreRendered, (500, 40))
    pygame.display.update()