import pygame
import time
import math

pygame.init()
clock = pygame.time.Clock()

W_W = 1920
W_H = 1080
BRUSH_SIZE = 2
BRUSH_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((W_W, W_H))

splashImage = pygame.image.load("desireCreativeLogo.png").convert()
image_rect = splashImage.get_rect(center=(W_W // 2, W_H // 2))

showSplashScreen = True
splash_duration = 10
splash_start_time = time.time()

showAnimEditor = False

def animEditor():
    pass
    
def brushTool(screen, color, startPos, endPos, size):
    distance = math.hypot(endPos[0] - startPos[0], endPos[1] - startPos[1])
    circles = int(distance / size) + 1
    for i in range(circles):
        x = startPos[0] + (endPos[0] - startPos[0]) * i / circles
        y = startPos[1] + (endPos[1] - startPos[1]) * i / circles
        pygame.draw.circle(screen, color, (int(x), int(y)), size)

running = True
prevPos = None

screen.fill((255, 255, 255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not showSplashScreen:
        mousePressed = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        
        if mousePressed[0]:
            if prevPos is None:
                prevPos = mousePos
            brushTool(screen, BRUSH_COLOR, prevPos, mousePos, BRUSH_SIZE)
            prevPos = mousePos
        else:
            prevPos = None
        
    if showSplashScreen:
        current_time = time.time()
        if current_time - splash_start_time > splash_duration:
            showSplashScreen = False
            showAnimEditor = True

    if showSplashScreen:
        screen.fill((255, 255, 255))
        screen.blit(splashImage, image_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
