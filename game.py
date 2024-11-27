import pygame
import random
import time

snake_speed = 15

windox_x = 720
windox_y = 800

#colors
black = pygame.Color(0, 0, 0)
white = pygame.color(255, 255, 255)
red = pygame.color(255, 0, 0)
green = pygame.color(0, 255, 0)
blue = pygame.color(0, 0, 255)

pygame.init() #initialization of pygame

pygame.display.set_caption('Snek')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [100, 50]

#initial body of snake
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

#starting score
score = 0

def show_score(choice, color, font, size):

  score_font = pygame.font.SysFont(font, size)

score_surface = score_font.render('Score: ' + str(score), True, color)

score_rect = score_surface.get_rect()

game_window.blit(score_surface, score_rect)

def game_over():

  my_font = pygame.font.SysFont('times new roman', 50)

game_over_surface = my_font.render('Your Score is: ' + str(score), True, red)

#create rectangular object for text
game_over_rect = game_over_surface.get_rect()

#set position of text
game_over_rect.midtop = (window_x/2, window_y/4)

#draw text on screen
game_window.blit(game_over_surface, game_over_rect)

#program quits after 2 secs.
time.sleep(2)

#pygame library deactivation
pygame.quit()

#quit program
quit()

#Main
while True:
  
for event in pygame.event.get():
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_UP:
      change_to = 'UP'
      if event.key == pygame.K_DOWN:
        change_to = 'DOWN'
        if event.key == pygame.K_LEFT:
          change_to = 'LEFT'
          if event.key == pygame.K_RIGHT:
            change_to = 'RIGHT'

#Prevent snake from moving two directions simultaneously
if change_to == 'UP' and direction != 'DOWN':
  direction == 'UP
if change_to == 'DOWN' and direction != 'UP':
  direction == 'DOWN'
if change_to == 'LEFT' and direction != 'RIGHT':
  direction == 'LEFT'
if change_to == 'RIGHT' and direction != 'LEFT:
  direction == 'RIGHT'

#Moving snake
if direction == 'UP':
  snake_position[1] -= 10
if direction == 'DOWN':
  snake_position[1] += 10
if direction == 'LEFT':
  snake_position[0] -= 10
if direction == 'RIGHT':
  snake_position[0] += 10

#Snake body growth mechanism
#Incrementation by 10
snake_body.insert(0, list(snake_position))
if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
  score += 10
  fruit_spawn = False
else:
  snake_body.pop()

if not fruit_spawn:
  fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True
game_spawn.fill(black)

for pos in snake_body: 
  pygame.draw_rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
  pygame.draw_rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

#Game Over condition
if snake_position[0] < 0 or snake_position[0] > window_x-10:
  game_over()
if snake_position[1] < 0 or snake_position[1] > window_y-10:
  game_over()

for block in snake_body[1:]:
  if snake_position[0] == block[0] and snake_position[1] == block[1]: game_over()

show_score(1, white, 'times new roman', 20)

pygame.display.update()

