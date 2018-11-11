from random import randint
import pygame

pygame.init()
size = (548, 962)
screenmode = pygame.display.set_mode(size)
done = 0
clock = pygame.time.Clock()

def Score(score):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Memory collected: " + str(score), True, (0, 0, 0))
    screen.blit(text, [0, 0])

def end():
    font = pygame.font.SysFont(None,30)
    text = font.render("Oh no! You ran out of memory", True, (255, 0 ,0))
    screen.blit(text, [120,250])

def floppybird(x, y):
    pygame.draw.circle(screen, (0, 0, 255), [x,y], 20)

def column(x, y, xsize, ysize):
    pygame.draw.rect(screen, (0, 255, 0), [x,y,xsize, ysize])
    pygame.draw.rect(screen, (0, 255, 0), [x, int(y + ysize + 150), xsize, ysize+391])#length*0.714

x = 250
y = 250
speed_y = 0
column_xlocation = 545
column_ylocation = 0
column_xsize = 80
column_ysize = randint(0, 673)#0.7*height
column_speed = 2
score = 0

while done != 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speed_y = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                speed_y = 5;

    screen = pygame.Surface((screenmode.get_width(), screenmode.get_height()))
    screen.fill((255, 255, 255))
    screen = screen.convert()
    column(column_xlocation, column_ylocation, column_xsize, column_ysize)
    Score(score)
    floppybird(x, y)
    column_xlocation -= column_speed
    y += speed_y
    if y > 800:#~0.94*height
        end()
        column_speed = 0
        speed_y = 0
    if x > column_xlocation and x < column_xlocation + 3:
        score = score + 1

    if column_xlocation < -50:
        column_xlocation = 545
        column_ysize = randint(0, 673)#~0.7*height

    if x + 20 > column_xlocation and x - 50 < column_xlocation + column_xsize and (y + 20 < column_ysize or y - 20 < column_ysize):
        end()
        column_speed = 0
        speed_y = 0

    screenmode.blit(screen, (0,0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
