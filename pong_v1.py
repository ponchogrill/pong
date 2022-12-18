import pygame
import sys
 
FPS = 60
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
 
clock = pygame.time.Clock()
sc = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT))
 
# радиус будущего круга
r = 20
# координаты круга
ball_x = SCREEN_WIDTH//2
ball_y = SCREEN_HEIGHT // 2
#скорости мячя
ball_speed_x = 3
ball_speed_y = 1
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #передвигаем мяч по экрану
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    #выход за края экрана
    #левый
    if ball_x <= r:
        ball_speed_x = -ball_speed_x
    #правый
    if ball_x >= SCREEN_WIDTH -r:
        #летел на право-полетел на лево
        ball_speed_x = -ball_speed_x
    if ball_y <= r:
        ball_speed_y = -ball_speed_y
    #правый
    if ball_y >= SCREEN_HEIGHT -r:
        #летел на право-полетел на лево
        ball_speed_y = -ball_speed_y

 
    # заливаем фон
    sc.fill(WHITE)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball_x, ball_y), r)
    # обновляем окно
    pygame.display.update()
    clock.tick(FPS)

